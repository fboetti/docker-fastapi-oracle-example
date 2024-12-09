FROM python:3.11

COPY ./src/requirements.txt src/requirements.txt
RUN python3 -m pip install -r src/requirements.txt

# -- Configuring timezone -- #
ENV TZ=Europe/Rome
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/timezone

# Install Oracle Instant Client. It's necessary to install the Oracle Instant Client to connect to the Oracle database.
ENV ORACLE_INSTANT_CLIENT_VERSION=23.6.0.24.10
ENV ORACLE_HOME=/opt/oracle

RUN apt-get update && apt-get install -y libaio1 wget && \
    wget https://download.oracle.com/otn_software/linux/instantclient/2360000/instantclient-basic-linux.x64-${ORACLE_INSTANT_CLIENT_VERSION}.zip && \
    mkdir -p $ORACLE_HOME && \
    unzip instantclient-basic-linux.x64-${ORACLE_INSTANT_CLIENT_VERSION}.zip -d $ORACLE_HOME && \
    rm instantclient-basic-linux.x64-${ORACLE_INSTANT_CLIENT_VERSION}.zip && \
    ln -s $ORACLE_HOME/instantclient_*/* $ORACLE_HOME && \
    echo "$ORACLE_HOME" > /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig

# Add Oracle libraries to the library path
ENV LD_LIBRARY_PATH=$ORACLE_HOME

EXPOSE 8000

WORKDIR /usr/src/backend

ENTRYPOINT ["python", "run.py"]

CMD ["run", "--reload", "--run-migrations"]
