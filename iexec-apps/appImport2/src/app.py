import os
import sys
import json
from pymongo import MongoClient
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

iexec_out = os.environ['IEXEC_OUT']
iexec_in = os.environ['IEXEC_IN']

print("STARTING APP")


# Get DB credentials from the dataset
dbCredentials = ""
with open(iexec_in + '/db_credentials.txt', 'r') as dataset:
    dbCredentials = dataset.read()


# Get private key to decrypt input data
with open(iexec_in + "/private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

        
# load decrypt and format input data
with open(iexec_in + "/encrypted_data.data", "rb") as f:
    encrypted = f.read()

original = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

inputData = json.loads(original.decode('utf8'))
print("inputData: ", inputData)

connectionStr = 'mongodb://{}@172.17.0.2:27017/?authSource=data'.format(dbCredentials)
client = MongoClient(connectionStr)
db=client.data
status = db.localisations.insert_one(inputData) # {UUID: 1, position: 33, apps: [1, 2]}
print("status: ", status)
client.close()



# Append some results
# with open(iexec_out + '/result.txt', 'w+') as fout:
#     fout.write("PROCESSING (export) APP2 results: \n\n")
#     for row in infos:
#         fout.write(str(row)+"\n")




# Declare everything is computed
with open(iexec_out + '/determinism.txt', 'w+') as fout:
    fout.write("It is.")
with open(iexec_out + '/computed.json', 'w+') as f:
    json.dump({ "deterministic-output-path" : iexec_out + '/determinism.txt' }, f)

print("ENDING APP")
