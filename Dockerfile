FROM python:3.6
LABEL maintainer "Yugo <yugo132@gmail.com>"

WORKDIR /app

COPY . /app

RUN apt-get update

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY app ./
COPY migrations ./
COPY feedback.py ./
COPY config.py ./ 

COPY ./boot.sh ./entrypoint.sh
RUN chmod a+x ./entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
