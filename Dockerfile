#!/bin/bash
FROM python:3.10 AS local
EXPOSE 8005

ARG timezone="Asia/Seoul"
RUN echo ${timezone} > /etc/timezone \
 && ln -sf /usr/share/zoneinfo/${timezone} /etc/localtime

RUN apt-get -y update  \
    && apt-get -y upgrade \
    && apt-get install -y wait-for-it

WORKDIR /backend
COPY ./ /backend
RUN pip install -r requirements.txt

FROM local AS production
ENTRYPOINT ["./entrypoint.sh"]
