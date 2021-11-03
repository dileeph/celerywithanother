FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install supervisor -y && \
    mkdir -p /var/log/supervisor && \
    mkdir -p /etc/supervisor/conf.d

COPY requirements.txt /tmp/pip-tmp/
COPY app/supervisor.conf /etc/supervisor.conf
COPY app/flask_infohealth.conf /etc/supervisor/conf.d/flask_infohealth.conf 
COPY app/celery.conf /etc/supervisor/conf.d/celery.conf 
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp


ENV DB_HOST=
ENV DB_USER=
ENV DB_PASSWORD=
ENV DB_PORT=
ENV DB_NAME=
ENV SQS_QUEUE=<queue_full_path_without_https://>
## only for scheduler - run every 15 minutes
ENV BATCH_SCHEDULE="hour=*&minute=*/2"
RUN sudo ln -sf /usr/bin/python3 /usr/bin/python
RUN python --version
COPY . /
WORKDIR /app

RUN chmod a+x bootstrap.sh

CMD ["supervisord", "-c", "/etc/supervisor.conf"]
EXPOSE 5000