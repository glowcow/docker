FROM debian:bookworm-slim
WORKDIR /etcdctl
ARG TAG
ARG ETCD_VER=${TAG}
ARG GOOGLE_URL=https://storage.googleapis.com/etcd
ARG GITHUB_URL=https://github.com/etcd-io/etcd/releases/download
ARG DOWNLOAD_URL=${GOOGLE_URL}

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /tmp/etcd-v${ETCD_VER}-linux-amd64.tar.gz \
    && rm -rf /tmp/etcd-download-test && mkdir -p /tmp/etcd-download-test \
    && curl -L ${DOWNLOAD_URL}/v${ETCD_VER}/etcd-v${ETCD_VER}-linux-amd64.tar.gz -o /tmp/etcd-v${ETCD_VER}-linux-amd64.tar.gz \
    && tar xzvf /tmp/etcd-v${ETCD_VER}-linux-amd64.tar.gz -C /usr/bin --strip-components=1 \
    && rm -f /tmp/etcd-v${ETCD_VER}-linux-amd64.tar.gz \
    && rm /usr/bin/etcd

CMD ["/usr/bin/tail", "-f", "/dev/null"]
