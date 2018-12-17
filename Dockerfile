FROM python:3.6
LABEL maintainer "Yugo <yugo132@gmail.com>"

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install libpq postgresql-dev gcc python3-dev musl-dev build-base

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY app ./
COPY migrations ./
COPY search.py ./
COPY config.py ./ 

COPY ./boot.sh ./entrypoint.sh
RUN chmod a+x ./entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
