ARG TAG
FROM hashicorp/terraform:${TAG}
ARG EXTRA_PACKAGES="curl"
RUN apk update \
    && apk add --no-cache ${EXTRA_PACKAGES}