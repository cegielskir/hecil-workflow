FROM python:3.8-alpine

RUN apk add --no-cache make gcc g++ zlib-dev nodejs npm
WORKDIR /
ADD hecil-master.tar.gz /

RUN mv Hecil-master Hecil && \
    cd Hecil && \
    cd bwa-src && \
    make && \
    cp bwa .. 

ENV PATH $PATH:/Hecil

ARG hf_job_executor_version=1.1.4

ENV HYPERFLOW_JOB_EXECUTOR_VERSION=$hf_job_executor_version

RUN npm install -g @hyperflow/job-executor@${HYPERFLOW_JOB_EXECUTOR_VERSION}