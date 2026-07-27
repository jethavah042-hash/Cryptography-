import hashlib
message = input("Enter the message to hash: ")

h= hashlib.sha256(message.encode()).hexdigest()
print("Hash Value:", h)       