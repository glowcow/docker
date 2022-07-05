FROM debian:bullseye-slim
RUN apt-get update && \
    apt-get install -y curl iproute2 dnsutils && \
    rm -rf /var/lib/apt/lists/*
CMD ["/usr/bin/tail", "-f", "/dev/null"]
