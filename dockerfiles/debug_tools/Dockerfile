FROM debian:bullseye-slim
RUN apt-get update \
    && apt-get install -y curl iproute2 dnsutils netcat net-tools nmap inetutils-traceroute nano vim \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime \
    && echo "Europe/Moscow" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata
CMD ["/usr/bin/tail", "-f", "/dev/null"]
