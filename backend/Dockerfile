FROM python:3.7-alpine
RUN mkdir /home/code
WORKDIR /home/code
COPY requirements.txt /home/code
RUN apk add build-base
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install -r requirements.txt
