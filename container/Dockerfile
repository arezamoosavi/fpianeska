FROM ubuntu:latest

# Install OpenJDK 8
RUN \
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*


RUN apt-get update && apt-get install -y software-properties-common

# Install Python3
RUN \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y curl python3.7 python3.7-dev python3.7-distutils python3-pip python3-virtualenv && \
    rm -rf /var/lib/apt/lists/*

# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
# RUN update-alternatives --set python /usr/bin/python3.7

# install python2
RUN \
    add-apt-repository ppa:deadsnakes/ppa &&  apt-add-repository universe &&\
    apt-get update && apt-get install -y curl python2 python2.7 python2.7-dev && \
    rm -rf /var/lib/apt/lists/*


RUN update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
RUN update-alternatives --set python /usr/bin/python2.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_FORMAT=legacy

RUN apt-get update -y && apt-get install -y libzbar-dev bash gcc git libc-dev curl wget vim nano
RUN apt-get update -y && apt-get install -y build-essential

RUN apt-get update -y && apt-get install -y ranger caca-utils highlight atool w3m poppler-utils mediainfo

RUN apt-get update && apt-get install -y iputils-ping telnet openssh-client net-tools \
    man unzip vim-tiny bc openssh-server thrift-compiler

RUN apt-get install -y netcat && apt-get autoremove -y
RUN apt-get update && apt-get clean

# install scala
RUN wget --no-verbose https://downloads.lightbend.com/scala/2.11.8/scala-2.11.8.tgz
RUN tar -xzvf scala-2.11.8.tgz
RUN mv scala-2.11.8 /opt/scala
ENV SCALA_HOME=/opt/scala
ENV PATH=$PATH:$SCALA_HOME/bin

#install sbt
RUN wget --no-verbose https://dl.bintray.com/sbt/native-packages/sbt/0.13.13/sbt-0.13.13.tgz
RUN tar -xzvf sbt-0.13.13.tgz
RUN mv sbt-launcher-packaging-0.13.13 /opt/sbt

ENV SBT_HOME=/opt/sbt
ENV PATH=$PATH:$SBT_HOME/bin

RUN sbt sbtVersion

#Install hadoop
RUN wget https://downloads.apache.org/hadoop/core/hadoop-3.2.1/hadoop-3.2.1.tar.gz
RUN tar -xzvf hadoop-3.2.1.tar.gz
RUN mv hadoop-3.2.1 /opt/hadoop

# install spark
RUN wget --no-verbose https://downloads.apache.org/spark/spark-2.4.6/spark-2.4.6-bin-hadoop2.7.tgz
RUN tar -xzvf spark-2.4.6-bin-hadoop2.7.tgz
RUN mv spark-2.4.6-bin-hadoop2.7 /opt/spark

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin

# download maven
RUN wget --no-verbose https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.2.5/apache-maven-3.2.5-bin.tar.gz
RUN tar -xzvf apache-maven-3.2.5-bin.tar.gz
RUN mv apache-maven-3.2.5 /opt/maven

# define environment variables for maven
ENV M2_HOME=/opt/maven
ENV PATH=$PATH:$M2_HOME/bin

ENV MAVEN_HOME=/opt/maven
ENV PATH=$PATH:$MAVEN_HOME/bin
RUN mvn --version

RUN rm -rf scala-2.11.8.tgz spark-2.4.6-bin-hadoop2.7.tgz sbt-0.13.13.tgz \
    apache-maven-3.6.0-bin.tar.gz hadoop-3.2.1.tar.gz

ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin
ENV CLASSPATH=$HADOOP_HOME/lib:$CLASSPATH
ENV HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
ENV HADOOP_OPTS="-Djava.library.path=$HADOOP_COMMON_LIB_NATIVE_DIR"
ENV LD_LIBRARY_PATH=$HADOOP_HOME/lib/native

ENV PATH=$PATH:$SPARK_HOME/sbin
RUN mkdir -p /opt/spark/history
COPY container/spark-defaults.conf /opt/spark/conf/spark-defaults.conf

#Workiingg
RUN mkdir -p /opt/project
COPY ./src ./opt/project

COPY container/run.sh /run.sh
RUN chmod a+rwx /run.sh

WORKDIR /opt/project
# ENTRYPOINT bash /opt/spark/sbin/start-master.sh ; bash /opt/spark/sbin/start-slave.sh spark://localhost:7077