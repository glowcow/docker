FROM debian:bullseye-slim
ARG TZ=Europe/Moscow
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-client mc curl telnet iproute2 dnsutils iputils-ping netcat net-tools nmap inetutils-traceroute nano vim \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

CMD ["/usr/bin/tail", "-f", "/dev/null"]
