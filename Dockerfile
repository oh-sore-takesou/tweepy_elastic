FROM python:3.5.2
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

ENV CONSUMER_KEY <YOUR TWITTER APP CONSUMER_KEY>
ENV CONSUMER_SECRET <YOUR TWITTER APP CONSUMER_SECRET>
ENV ACCESS_TOKEN <YOUR TWITTER APP ACCESS_TOKEN>
ENV ACCESS_SECRET <YOUR TWITTER APP ACCESS_SECRET>
