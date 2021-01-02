FROM python:3.8-alpine

RUN apk add --no-cache make gcc g++ zlib-dev
WORKDIR /
ADD hecil-master.tar.gz /

RUN mv Hecil-master Hecil && \
    cd Hecil && \
    cd bwa-src && \
    make && \
    cp bwa .. 

ENV PATH $PATH:/Hecil
