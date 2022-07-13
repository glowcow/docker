FROM debian:bullseye-slim
RUN apt-get update \
    && apt-get install -y curl iproute2 dnsutils netcat net-tools nmap inetutils-traceroute nano vim \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime \
    && echo "Europe/Moscow" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

ARG DOCKER_CHANNEL=stable
ENV DOCKER_VERSION=19.03.15
RUN curl -fsSLO https://download.docker.com/linux/static/${DOCKER_CHANNEL}/x86_64/docker-${DOCKER_VERSION}.tgz \
  && tar xzvf docker-${DOCKER_VERSION}.tgz --strip 1 -C /usr/local/bin docker/docker \
  && rm -f docker-${DOCKER_VERSION}.tgz

CMD ["/usr/bin/tail", "-f", "/dev/null"]