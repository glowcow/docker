FROM debian:bullseye-slim
ARG TZ=Asia/Jerusalem
ARG TAG
ARG EXTRA_PACKAGES="transmission-daemon"
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y ${EXTRA_PACKAGES}=${TAG} \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata
EXPOSE 9091

CMD ["/usr/bin/transmission-daemon", "-f", "--log-error", "-g", "/etc/transmission-daemon"]
