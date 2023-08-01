FROM debian:bookworm-slim
ARG TZ=Asia/Jerusalem
ARG EXTRA_PACKAGES="postgresql-client openssh-client mc jq curl git wget whois telnet iproute2 dnsutils iputils-ping netcat-openbsd net-tools nmap inetutils-traceroute nano"
ENV TOKEN_PATH="/var/run/secrets/kubernetes.io/serviceaccount/token"
ENV CA_CERT_PATH="/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y ${EXTRA_PACKAGES} \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

CMD ["/usr/bin/tail", "-f", "/dev/null"]
