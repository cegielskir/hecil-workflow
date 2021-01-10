FROM perl:5.32.0 as data

ARG NUMBER_OF_CONTIGS=100
ARG LENGTH_OF_CONTIGS=10

RUN mkdir /work_dir
WORKDIR /work_dir

ADD hecil-data.tar.gz .

RUN ./fastq_generate.pl $(( 10 * ${NUMBER_OF_CONTIGS})) $(( 10 * ${LENGTH_OF_CONTIGS} )) > ref.fastq && \
    ./fastq_generate.pl ${NUMBER_OF_CONTIGS} ${LENGTH_OF_CONTIGS} ref.fastq > query.fastq && \
    ./convert_fastq.py ref.fastq > ref.fasta && \
    ./make_hecil_workflow -l ref.fasta -s query.fastq -len ${LENGTH_OF_CONTIGS} -p ${LENGTH_OF_CONTIGS} -ps 2 -rs ${NUMBER_OF_CONTIGS}


FROM mhart/alpine-node:8

RUN mkdir /work_dir
WORKDIR /work_dir

COPY --from=data /work_dir/* ./

RUN npm install -g https://github.com/hyperflow-wms/hflow-tools/archive/master.tar.gz && \
    hflow-convert-makeflow hecil.mf > workflow.json