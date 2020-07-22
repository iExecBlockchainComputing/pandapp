FROM sconecuratedimages/public-apps:python-3.7.3-alpine3.10-scone3.0

### install python3 dependencies you need
RUN apk update && apk add gcc libffi-dev openssl-dev
RUN SCONE_MODE=sim pip3 install pymongo cryptography

COPY ./src /app

###  protect file system with Scone
COPY ./protect-fs.sh ./Dockerfile /build/
RUN sh /build/protect-fs.sh /app

ENTRYPOINT ["python", "/app/app.py"]
