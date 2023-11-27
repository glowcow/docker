FROM debian:bookworm
ARG TAG
ARG SMB_USER="pi_smb"
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y samba=2:${TAG}+dfsg-0+deb12u1 \
    && useradd --system --no-create-home --shell /usr/sbin/nologin ${SMB_USER} \
    && rm -rf /var/lib/apt/lists/*
EXPOSE 137 138 139 445

CMD ["/usr/sbin/smbd", "--foreground", "--no-process-group", "--configfile", "/etc/samba/smb.conf"]
