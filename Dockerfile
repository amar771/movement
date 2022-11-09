FROM python:3.8-alpine

WORKDIR /uber-movement
ADD . .

RUN pip install -I .

ENTRYPOINT [ "python", "main.py" ]
CMD [ "ingest-movement" ]