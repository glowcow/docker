FROM debian:bookworm-slim
ARG TAG
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y transmission-daemon=${TAG}-2.1+deb12u1 \
    && rm -rf /var/lib/apt/lists/*
EXPOSE 9091
ENTRYPOINT ["/usr/bin/transmission-daemon"]
CMD ["-f", "--log-error", "-g", "/etc/transmission-daemon"]
