FROM python:3.8-slim-bullseye AS stage-1
WORKDIR /builder
COPY requirements.txt .
RUN pip3 wheel --no-cache-dir --no-deps --wheel-dir /builder/wheels -r requirements.txt

FROM python:3.8-slim-bullseye AS stage-2
WORKDIR /ansible
ENV PYTHONUNBUFFERED=1
ENV ANSIBLE_CONFIG=./ansible.cfg
RUN apt-get update \
    && apt-get install -y sshpass \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime \
    && echo "Europe/Moscow" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && mkdir -m 600 ~/.ssh
COPY --from=stage-1 /builder/wheels /wheels
RUN pip3 install --no-cache /wheels/*
CMD ["/usr/bin/tail", "-f", "/dev/null"]