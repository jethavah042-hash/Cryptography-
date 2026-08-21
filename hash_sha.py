import hashlib
message = input("Enter the message to hash: ")

h= hashlib.sha1(message.encode()).hexdigest()
print("Hash Value:", h)       