ARG TAG
ARG ETCD_VER=${TAG}
FROM hashicorp/terraform:${TAG}
ARG EXTRA_PACKAGES="tzdata curl"
ENV TZ=Asia/Jerusalem
RUN apk update \
    && apk add --no-cache ${EXTRA_PACKAGES}