FROM debian:bookworm
ARG TZ=Asia/Jerusalem
ARG TAG
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y transmission-daemon=${TAG}-2.1+deb12u1 \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata
EXPOSE 9091

CMD ["/usr/bin/transmission-daemon", "-f", "--log-error", "-g", "/etc/transmission-daemon"]
