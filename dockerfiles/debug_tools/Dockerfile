FROM debian:bookworm-slim
WORKDIR /root
COPY . /root/
ARG TZ=Asia/Jerusalem
ARG PKCTL=0.5.7
ARG EXTRA_PACKAGES="postgresql-client ncdu ntpdate openssh-client mc jq curl git wget whois telnet iproute2 dnsutils iputils-ping netcat-openbsd net-tools nmap inetutils-traceroute nano"
ENV TOKEN_PATH="/var/run/secrets/kubernetes.io/serviceaccount/token"
ENV CA_CERT_PATH="/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
ENV KUBECONFIG="/tmp/kubeconfig"
ENV KUBE_EDITOR="nano"
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y ${EXTRA_PACKAGES} \
    && chmod +x make_kubeconfig.sh \
    && rm -rf /var/lib/apt/lists/* \
    && wget -q https://dl.min.io/client/mc/release/linux-amd64/mc \
    && chmod +x mc \
    && mv mc /usr/local/bin/minc \
    && curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/kubectl \
    && curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 \
    && chmod 700 get_helm.sh \
    && ./get_helm.sh \
    && rm get_helm.sh \
    && wget -q https://gitlab.com/api/v4/projects/38089511/packages/generic/pkctl/${PKCTL}/pkctl-${PKCTL} \
    && mv pkctl-0.5.7 /usr/local/bin/pkctl \
    && chmod +x /usr/local/bin/pkctl \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

CMD ["/usr/bin/tail", "-f", "/dev/null"]
