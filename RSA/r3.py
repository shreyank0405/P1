import rsa
(public_key,private_key)=rsa.newkeys(513)
(private_key1)=rsa.newkeys(512)
message="Secret"
encrypted=rsa.encrypt(message.encode(),public_key)
print("Encrypted-", encrypted)
decrypted=rsa.decrypt(encrypted,private_key1).decode()
print("Decrypted-", decrypted)

print(public_key)
print(private_key1)