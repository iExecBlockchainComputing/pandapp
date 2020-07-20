import os
import sys
import json
from pymongo import MongoClient

iexec_out = os.environ['IEXEC_OUT']
iexec_in = os.environ['IEXEC_IN']

print("STARTING APP")


# Get DB credentials from the dataset
dbCredentials = ""
if os.path.exists(iexec_in + '/dataset.txt'):
    with open(iexec_in + '/dataset.txt', 'r') as dataset:
        dbCredentials = dataset.read()


# Get the infos to insert from args
assert len(sys.argv) > 3, 'Error: Missing data to import.'
# for data in sys.argv[1:]:
#     print(data)

# Format data for input
apps = []
for app in sys.argv[3:]:
    apps.append(int(app))

inputData = {"UUID": int(sys.argv[1]), "position": int(sys.argv[2]), "apps": apps}
# print("inputData: ", inputData)

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
