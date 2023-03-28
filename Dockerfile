FROM python:3.9

RUN ln -s /bin/true /usr/bin/systemctl \
    && apt-get update \
    && apt-get install -y \
       vim redis-server postgresql

COPY Makefile requirements.txt $PROJECT_ROOT/

RUN make vendor

COPY . $PROJECT_ROOT
