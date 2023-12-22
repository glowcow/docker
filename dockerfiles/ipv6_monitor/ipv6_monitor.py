import subprocess
import re
import time
import requests
import yaml
import datetime

def load_config(filename):
    with open(filename, 'r') as stream:
        return yaml.safe_load(stream)

def get_global_ipv6_address(interface):
    try:
        result = subprocess.run(['ip', '-6', 'addr', 'show', interface], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        match = re.search(r'inet6 ([0-9a-f:]+(?<!fe80))(?:/\d+)', output)
        if match:
            return match.group(1)
        else:
            return "No global IPv6 address found."
    except FileNotFoundError:
        return "The 'ip' command is not found on this system."

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    requests.post(url, data=data)

def update_godaddy_dns(api_key, api_secret, domain, record_type, names, data):
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    success = True
    for name in names:
        url = f"https://api.godaddy.com/v1/domains/{domain}/records/{record_type}/{name}"
        payload = [{
            "data": data,
            "ttl": 600
        }]
        response = requests.put(url, json=payload, headers=headers)
        if response.status_code != 200:
            print(f"Failed to update DNS record for {name}: {response.text}")
            success = False
    return success

def monitor_global_ipv6_address(interval, interface, bot_token, chat_id, api_key, api_secret, domain, record_names):
    last_known_ipv6 = None
    while True:
        current_ipv6 = get_global_ipv6_address(interface)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if current_ipv6 not in ["No global IPv6 address found.", "The 'ip' command is not found on this system."] and current_ipv6 != last_known_ipv6:
            message = f"{current_time} | IPv6 address changed to {current_ipv6}"
            if update_godaddy_dns(api_key, api_secret, domain, "AAAA", record_names, current_ipv6):
                message += " and DNS records updated successfully."
            else:
                message += " but failed to update one or more DNS records."
            print(message)
            send_telegram_message(bot_token, chat_id, message)
            last_known_ipv6 = current_ipv6
#        else:
#            print(f'{current_time} | {current_ipv6}')
        time.sleep(interval)

def main():
    # Load configuration variables
    config = load_config('config.yaml')

    # Use the loaded configuration
    interf = config.get('interface')
    interv = config.get('interval')
    telegram_config = config.get('telegram', {})
    godaddy_config = config.get('godaddy', {})

    bot_token = telegram_config.get('bot_token')
    chat_id = telegram_config.get('chat_id')
    api_key = godaddy_config.get('api_key')
    api_secret = godaddy_config.get('api_secret')
    domain = godaddy_config.get('domain')
    record_names = godaddy_config.get('record_names')

    # Run the monitor function
    monitor_global_ipv6_address(interv, interf, bot_token, chat_id, api_key, api_secret, domain, record_names)

if __name__ == "__main__":
    main()
