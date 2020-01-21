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
encryptedData='ulSFKYGNaCnwLaQyNFDdsPXgtK6vu2ayX8rhxJg3vstll1p5O7QZRXs5Kz5dwbTVbQgQdEg/rTn4XEOe56hkyXnttb/gN/V2pUf1gblWES51/447XCRHeJom3hEcult49ho4J6DnPeyBIUtIwoDDUImCBSn7xu4SiQ1ayhH1l4TqBa+nCDEbyyENGrD/xMcdAE6nbJ3bkWBxcOhe+kfm0k/BQEUHTGSEThpxzV4sLFkbNx/mKjLOazjnxL/A204Un62UzI+o7sksh7cL1Uc27W3Tqs/D6JWbyxsgh15PdwcurFzRW+yPNEFu6bxibHDAOeg4OfFbEDXJYJjG975r4Q=='
decryptedData = cipher.decrypt(encryptedData)
# print(encryptedData)
print(decryptedData)



# Check this out https://stackoverflow.com/questions/44223479/how-to-use-rsa-or-similar-encryption-in-python-3