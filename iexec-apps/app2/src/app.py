import os
import sys
import json
from pymongo import MongoClient

iexec_out = os.environ['IEXEC_OUT']
iexec_in = os.environ['IEXEC_IN']

print("STARTING APP")


# Eventually use some confidential assets
dbCredentials = ""
if os.path.exists(iexec_in + '/dataset.txt'):
    with open(iexec_in + '/dataset.txt', 'r') as dataset:
        dbCredentials = dataset.read()

connectionStr = 'mongodb://{}@172.17.0.2:27017/?authSource=data'.format(dbCredentials)
client = MongoClient(connectionStr)
db=client.data
infos = db.app2View.find()
client.close()



# Append some results
with open(iexec_out + '/result.txt', 'w+') as fout:
    fout.write("PROCESSING (export) APP2 results: \n\n")
    for row in infos:
        fout.write(str(row)+"\n")




# Declare everything is computed
with open(iexec_out + '/determinism.txt', 'w+') as fout:
    fout.write("It is.")
with open(iexec_out + '/computed.json', 'w+') as f:
    json.dump({ "deterministic-output-path" : iexec_out + '/determinism.txt' }, f)

print("ENDING APP")