import hashlib
message = input("Enter the message to hash: ")

h= hashlib.md5(message.encode()).hexdigest()
print("Hash Value:", h)       