FROM perl:5.32.0 as data

RUN apt update -y
RUN apt install -y nodejs npm

RUN mkdir /data
WORKDIR /data

ADD hecil-data.tar.gz .

ARG NUMBER_OF_CONTIGS=100
ARG LENGTH_OF_CONTIGS=10
ARG NUMBER_OF_SPLITS=10

RUN ./fastq_generate.pl $(( 10 * ${NUMBER_OF_CONTIGS})) $(( 10 * ${LENGTH_OF_CONTIGS} )) > ref.fastq && \
    ./fastq_generate.pl ${NUMBER_OF_CONTIGS} ${LENGTH_OF_CONTIGS} ref.fastq > query.fastq && \
    ./convert_fastq.py ref.fastq > ref.fasta && \
    ./make_hecil_workflow -l ref.fasta -s query.fastq -len ${LENGTH_OF_CONTIGS} -n ${NUMBER_OF_SPLITS} -ps 2 -rs ${NUMBER_OF_CONTIGS}

RUN npm install -g https://github.com/hyperflow-wms/hflow-tools/archive/master.tar.gz && \
    hflow-convert-makeflow hecil.mf > workflow.json

RUN python prepare-workflow.py