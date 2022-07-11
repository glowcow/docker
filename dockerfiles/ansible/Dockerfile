FROM python:3.8-slim-bullseye AS builder
WORKDIR /builder
COPY requirements.txt .
RUN pip3 wheel --no-cache-dir --no-deps --wheel-dir /builder/wheels -r requirements.txt

FROM python:3.8-slim-bullseye AS final
WORKDIR /ansible
ENV PYTHONUNBUFFERED=1
RUN apt-get update \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime \
    && echo "Europe/Moscow" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata
COPY --from=builder /builder/wheels /wheels
RUN pip3 install --no-cache /wheels/*
CMD ["/usr/bin/tail", "-f", "/dev/null"]

