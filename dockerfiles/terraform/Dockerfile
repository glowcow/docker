ARG TAG
FROM hashicorp/terraform:${TAG}
ARG EXTRA_PACKAGES="curl wget zip"
RUN apk update \
    && apk add --no-cache ${EXTRA_PACKAGES}