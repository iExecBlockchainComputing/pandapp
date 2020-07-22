from pymongo import MongoClient
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import json

def test1():
    client = MongoClient("mongodb://app1user:app1pwd@172.17.0.2:27017/?authSource=data")
    db=client.data
    infos = db.app1View.find()

    for row in infos:
        print(row)

    
def testCryptoCreateStore():
    # Generate keys
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Write keys (store)
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open('private_key.pem', 'wb') as f:
        f.write(pem)

    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open('public_key.pem', 'wb') as f:
        f.write(pem)   


def testCryptoPrepareInput():
    with open("public_key.pem", "rb") as key_file, open("input_data.json") as input_file:
        # get input_file
        data = input_file.read()
        bytes_data = data.encode('utf-8')
        
        # load key
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

        # encrypt
        encrypted = public_key.encrypt(
            bytes_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    with open("encrypted_data.data", "wb") as f:
        f.write(encrypted)


def testCryptoReadDecrypt():
    # load encrypted data
    with open("encrypted_data.data", "rb") as f:
        encrypted = f.read()

    # load private (decryption) key
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    
    # decrypt
    original = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    data = json.loads(original.decode('utf8'))
    print(original)
    print(data)


if __name__ == "__main__":
    # testCryptoCreateStore()
    # testCryptoPrepareInput()
    testCryptoReadDecrypt()
