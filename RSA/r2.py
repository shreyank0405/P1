import rsa
(public_key,private_key)=rsa.newkeys(512)
message="Secret"
encrypted=rsa.encrypt(message.encode(),public_key)
print("Encrypted-", encrypted)
decrypted=rsa.decrypt(encrypted,private_key).decode()
print("Decrypted-", decrypted)

