FROM python:3.10-slim-bookworm AS stage-1
WORKDIR /builder
COPY requirements.txt .
RUN pip3 wheel --no-cache-dir --no-deps --wheel-dir /builder/wheels -r requirements.txt

FROM python:3.10-slim-bookworm AS stage-2
ENV PYTHONUNBUFFERED=1
COPY --from=stage-1 /builder/wheels /wheels
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y iproute2 \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --no-cache /wheels/* 
WORKDIR /app
COPY ipv6_monitor.py /app/
CMD ["python", "/app/ipv6_monitor.py"]
