FROM python:3.11-slim-bookworm AS stage-1
WORKDIR /builder
COPY requirements.txt .
RUN pip3 wheel --no-cache-dir --no-deps --wheel-dir /builder/wheels -r requirements.txt

FROM python:3.11-slim-bookworm AS stage-2
WORKDIR /ansible
ARG TZ=Asia/Jerusalem
ARG ANSIBLE_EXTRA_COLLECTIONS="community.general ansible.posix community.postgresql community.docker"
ENV PYTHONUNBUFFERED=1
ENV ANSIBLE_CONFIG=./ansible.cfg
ENV ANSIBLE_FORCE_COLOR=true
ENV ANSIBLE_HOST_KEY_CHECKING=false
ENV ANSIBLE_COLLECTIONS_PATH=/usr/share/ansible/collections
ENV ANSIBLE_LIBRARY=/usr/share/ansible/plugins/modules
COPY --from=stage-1 /builder/wheels /wheels
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y sshpass \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && mkdir -m 600 ~/.ssh \
    && pip3 install --no-cache /wheels/* \
    && ansible-galaxy collection install ${ANSIBLE_EXTRA_COLLECTIONS}
CMD ["/usr/bin/tail", "-f", "/dev/null"]
