FROM python:3.8.6-alpine3.12
RUN TERM=linux && export TERM
USER root
RUN apk add --update --no-cache mariadb-connector-c-dev \
	&& apk add --no-cache --virtual .build-deps \
		mariadb-dev \
		gcc \
		musl-dev \
    && apk del .build-deps \
    && apk add ca-certificates bash tzdata sudo curl wget openssh git \
    gcc g++ make libffi-dev openssl-dev libtool \
    && echo "Asia/Shanghai" > /etc/timezone && \
    cp -r -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    rm -rf /var/cache/apk/*   /tmp/*
WORKDIR /data/genshin-im
ADD . /data/genshin-im/
RUN bash -ex bin/install.sh dev
CMD ["./bin/start.sh"]
