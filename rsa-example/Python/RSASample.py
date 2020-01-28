# import cryptography
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.primitives import hashes

# with open("./keys/public_key.pem", "rb") as key_file:
#     public_key = serialization.load_pem_public_key(
#         key_file.read(),
#         backend=default_backend()
#     )
# message = b'This is test!'
# encrypted = public_key.encrypt(message,
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# )
# print(encrypted)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.Hash import SHA
from Crypto import Random
from base64 import b64encode
from base64 import b64decode

class RSA_Cipher:
#   def generate_key(self,key_length):
#     assert key_length in [1024,2048,4096]
#     rng = Random().read
#     self.key = RSA.generate(key_length,rng)

  def encrypt(self,data):
    public_key= RSA.import_key(open('./keys/public_key.pem').read())
    plaintext = b64encode(data.encode('utf-8'))
    rsa_encryption_cipher = PKCS1_OAEP.new(public_key, hashAlgo=SHA256)
    ciphertext = rsa_encryption_cipher.encrypt(plaintext)
    return b64encode(ciphertext).decode()

  def decrypt(self,data):
    ciphertext = b64decode(data.encode())
    private_key= RSA.import_key(open('./keys/private_key.pem').read())
    rsa_decryption_cipher = PKCS1_OAEP.new(private_key, hashAlgo=SHA256)
    plaintext = rsa_decryption_cipher.decrypt(ciphertext)
    return plaintext
    #return b64decode(plaintext).decode()

  def decrypt_secondary(self,data):
    ciphertext = b64decode(data.encode())
    private_key= RSA.import_key(open('./keys/private_key.pem').read())
    rsa_decryption_cipher = PKCS1_v1_5.new(private_key)
    dsize = SHA.digest_size
    sentinel = Random.new().read(15+dsize)
    plaintext = rsa_decryption_cipher.decrypt(ciphertext, sentinel)
    return plaintext
  
  def encrypt_secondary(self,data):
    public_key= RSA.import_key(open('./keys/public_key.pem').read())
    plaintext = b64encode(data.encode('utf-8'))
    rsa_encryption_cipher = PKCS1_OAEP.new(public_key, hashAlgo=SHA256)
    ciphertext = rsa_encryption_cipher.encrypt(plaintext)
    return b64encode(ciphertext).decode()

cipher = RSA_Cipher()
# cipher.generate_key(1024) #key length can be 1024, 2048 or 4096
#encryptedData = cipher.encrypt("This is test")
encryptedData='pJsTGcG9DqFZmYb2rQVv9XLLj6EnslUKK8B+gOMA2yXHxOsyQW8+2PS9NZqsMatP5yH4ly/q3jGRJM4X3bgjQM06sId9yoCkfVV+fsoOzA+NpqrPKaRdW+3lM+OkCFVJNgIcs48ofgcW5fCK/iVIBnIbZ2pBoeoJNJte2D5KJtl8colkGUGlFtC3mDxSFDq18BLA6ClFQMGatp0KAwjYsQB568h6RFpE6Q7iN3C2j7y6oXd+GDqSJvoSBIM2y/kAHuLFZb/jAIOZEbvGhkvoyotTiWa0N5/vZdn+3gqxH1DggoDW2bSyGP1aBIayqRPcr5Rn/S9EInT3MLlUiuR/oQ=='
decryptedData = cipher.decrypt_secondary(encryptedData)
# print(encryptedData)
print(decryptedData)



# Check this out https://stackoverflow.com/questions/44223479/how-to-use-rsa-or-similar-encryption-in-python-3