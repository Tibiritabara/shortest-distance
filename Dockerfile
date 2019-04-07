FROM python:3.7

ARG text_file=words.txt
ENV TEXT_FILE ${text_file}
RUN apt-get update
RUN apt-get install -y python python-pip python-dev
RUN pip install pipenv
ADD . /app
WORKDIR /app
RUN pipenv install --system --deploy --ignore-pipfile
