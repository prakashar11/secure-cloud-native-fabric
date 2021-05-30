FROM node:12-alpine

RUN apk update && \
    apk add gcc 

RUN apk add zip
RUN apk add musl-dev

RUN apk add python3
RUN apk add python3-dev

RUN pip3 install --upgrade pip
RUN pip3 install wheel

# first install the requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt 

# WORKDIR /
# ENTRYPOINT ["python3", ""]

