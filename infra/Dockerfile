FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y python3-dev build-essential pipenv jq

RUN mkdir -p /usr/src/iris

WORKDIR /usr/src/iris

COPY . .

#RUN jq -r '.default | to_entries[] | .key + .value.version' Pipfile.lock > requirements.txt

RUN pip3 install -r infra/requirements.txt

CMD ["gunicorn", "src:app", "-w", "4", "-b", ":8080", "-k", "uvicorn.workers.UvicornWorker"]
