FROM python:3.6
LABEL maintainer "Yugo <yugo132@gmail.com>"

ENV PYTHONUNBUFFERED 1

ENV FLASK_APP feedback.py
ENV FLASK_CONFIG production

WORKDIR /app

COPY . /app

RUN apt-get update

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY app /app/app
COPY migrations /app/migrations
COPY feedback.py /app/feedback.py
COPY config.py /app/config.py 

COPY ./entrypoint.sh /app/entrypoint.sh

RUN chmod a+x ./entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/app/entrypoint.sh"]
