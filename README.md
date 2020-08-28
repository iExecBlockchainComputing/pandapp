# PandApp
A privacy preserving data pooling service to help against pandemic spread


## Presentation
PandApp is (for now) a PoC introducing the possibility to securely manage and
valorize user data through the use of a sconified (run inside an SGX container)
Mongo Database and several iExec DApps to manage the access.
  
The goal is to allow any volonteer user to share some private data (localisations) and to choose which service (iExec DApp) can use them.


Here is what the architecture should look like:
![A quick visualisation of how PandApp works](https://github.com/iExecBlockchainComputing/pandapp/raw/v2/diagram.JPG)

---
## Deployment
### Database
The MongoDB is prepared here using a `docker-compose.yml` file to setup the docker container and some data to have the permissions already defined and some test data.

These are the users, corresponding roles and privileges :
| User ID  | User password  | Role name  | Privileges |
|----------|----------------|------------|------------|
| root          | root        | NA           | admin (all rights) (should be deleted when going to production) |
| app1user      | app1pwd     | app1Role     | find (read) on app1 view only                                   |
| app2user      | app2pwd     | app2Role     | find (read) on app2 view only                                   |
| appInputUser  | appinputpwd | appInputRole | insert (write) on localisations                                 |

To start the DB, check the `docker-compose.yml` file, change the volume mapping according to the location of the `/db/` folder and if needed specify the ports to use. 
`command: -c "mongod --auth"` is used to start the DB with authentification enabled.
You can the start the container:
```shell
docker-compose up
```

You should be able to connect to the DB using:
```
mongo 172.17.0.2:27017 --authenticationDatabase "data" -u app2user -p
```
or
```
mongo 172.17.0.2:27017 --authenticationDatabase "admin" -u "root" -p
```
> Don't forget to change `172.17.0.2:27017` to the IP and port your DB is listening to.

---
### iExec Datasets
We will use iExec applications to acess the DB, but we cannot store the DB credentials inside these applications. This is why each app needs a dataset containing the credentials specific to this app. This dataset being also restricted to be used only with this application.

> __Note :__ The _AppImport2_ application's dataset also needs to contain the private key used to decrypt users' data

You can find the files used to generate the datasets inside `/appXX/confidential-assets`.
> `/appImport2/confidential-assets/encrypted_data.data` is not part of a dataset but is an example of a user's input data once encrypted.

---
### iExec Apps
For this PoC, I featured 4 iExec apps: 
 * _App1_ and _App2_ are the service apps: they are here to fetch data from the DB and if needed execute some computations on these data;
 * _AppImport_ is sort of a beta version for _AppImport2_: it's just here test importing data inside the DB from some arguments (so it's not secured);
 * Finally _AppImport2_ is the secured version of the app to import data into the DB: it gets the data from a manually encrypted input file, so it also needs to manually decrypt this file;
 
 Before starting to deploy the applications, don't forget to adapt -- inside the `/appXX/src/app.py` file -- the Mongo connection string with the IP and port of your own DB
 ```python
 connectionStr = 'mongodb://{}@172.17.0.2:27017/?authSource=data'.format(dbCredentials)
 ```
 
All the source code is available in this repository, you can build the applications using the `build` script available, and  check out the deployment steps from https://docs.iex.ec/for-developers/confidential-computing/create-your-first-sgx-app or even https://github.com/iExecBlockchainComputing/private-code-valorisation_tutorial/wiki.

#### Test workspace
As you may have noticed there is in each application folder a `test-workspace` folder that can help you  test your application locally.

---
### Python Helpers
For imputing data in the DB, we need too manually encrypt these data before uploading them to the app. This is why there is this `python_helpers` folder: it contains everything needed to generate the pub/priv key pair, encrypt and decrypt some data from some json file.

---

Hoping you can find here everything you need to understand this PandApp PoC, if not do not hesitate to join iExec through slack or any other channel !


