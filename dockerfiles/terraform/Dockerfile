ARG TAG
ARG ETCD_VER=${TAG}
ARG EXTRA_PACKAGES="tzdata curl"
FROM hashicorp/terraform:${TAG}
ENV TZ=Asia/Jerusalem

RUN apk update \
    && apk add --no-cache ${EXTRA_PACKAGES}