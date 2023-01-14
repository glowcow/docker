ARG TAG
ARG ETCD_VER=${TAG}
FROM hashicorp/terraform:${TAG}
ENV TZ=Asia/Jerusalem

RUN apk update \
    && apk add --no-cache tzdata curl