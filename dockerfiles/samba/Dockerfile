FROM debian:bullseye-slim
ARG TZ=Asia/Jerusalem
ARG TAG
ARG EXTRA_PACKAGES="samba"
ARG SMB_USER="pi_smb"
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y ${EXTRA_PACKAGES}=2:${TAG}+dfsg-2 \
    && useradd --system --no-create-home --shell /usr/sbin/nologin ${SMB_USER} \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata
EXPOSE 137 138 139 445

CMD ["/usr/sbin/smbd", "--foreground", "--no-process-group", "--log-stdout", "--configfile", "/etc/samba/smb.conf"]
