ARG TAG
FROM hashicorp/terraform:${TAG}
ARG EXTRA_PACKAGES="curl wget zip"
RUN apk update \
    && apk add --no-cache ${EXTRA_PACKAGES} \
    && wget -q https://dl.min.io/client/mc/release/linux-amd64/mc \
    && chmod +x mc \
    && mv mc /usr/local/bin/minc