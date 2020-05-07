FROM iexechub/sconecuratedimages-iexec:cli-alpine AS scone

FROM iexechub/sconecuratedimages-iexec:python-3.7.3-alpine-3.10

COPY --from=scone   /opt/scone/scone-cli    /opt/scone/scone-cli
COPY --from=scone   /usr/local/bin/scone    /usr/local/bin/scone
COPY --from=scone   /opt/scone/bin          /opt/scone/bin

### this file is a temporary work around and it will
### be removed in the next releases but it is required
### by the iExec plateform for now.
COPY ./utils/signer.py /signer/signer.py

################################

### install apk packages
RUN apk add --no-cache bash build-base gcc libgcc

### install python3 dependencies
RUN SCONE_MODE=sim pip3 install attrdict python-gnupg web3 python-geohash Geohash

### copy the code inside the image
COPY ./src /app/.

################################

###  protect file system with scone
COPY ./utils/protect-fs.sh /protect-fs.sh
RUN bash /protect-fs.sh /app
RUN rm /protect-fs.sh /keytag

### Prepare dataset folder before starting the enclave.
### The entrypoint should match the params attribute
### written on the blockchain (the --params option of
### "iexec app run" command).
ENTRYPOINT unzip -o /iexec_in/$IEXEC_DATASET_FILENAME -d /iexec_in && python /app/app_heatmap.py
