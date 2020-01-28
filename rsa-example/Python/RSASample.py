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
from Crypto.Hash import SHA256
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

cipher = RSA_Cipher()
# cipher.generate_key(1024) #key length can be 1024, 2048 or 4096
#encryptedData = cipher.encrypt("This is test")
encryptedData='K7Vd4XkZNd+nMXBCY99pVy2aojpD1DnxhwY3DnV45ikGJpGke2GF7FcObdU4JXQ6rb5ckhHFVAyTCDn/d0BI7chwHNKS/5cDFoiyizBbzXSSKPyE3eFIntwjN7zq/fUgDDFPyWIQUlSLWwWMSQfbJrXT3SInRkSjMUbB4P6a348vwQHFQ2uXuPFp3sGEeLKPMuFmHH2B0d4pMB3RqoH3YMIkcsEJBLOr13aDF8YOs2sE6EQ0OpXEyN+CBQ3qUuwguDi9PEGpud7wH38ks6raeuDenxbRnLgEm12ZDvR88EzTWiLxMSH0hjPSWZl27azMNFj98EvgsOsoZHt6OMCntQ=='
decryptedData = cipher.decrypt(encryptedData)
# print(encryptedData)
print(decryptedData)



# Check this out https://stackoverflow.com/questions/44223479/how-to-use-rsa-or-similar-encryption-in-python-3