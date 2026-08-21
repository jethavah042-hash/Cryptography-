p = int(input("Enter Value of p: "))
g = int(input("Enter Value of g: "))


hardik_private_key = int(input("Enter Hardik's Private Key: "))
avesh_private_key = int(input("Enter Avesh's Private Key: "))

hardik_public_key = pow(g, hardik_private_key, p)
avesh_public_key = pow(g, avesh_private_key, p)

print("Hardik's Public Key: ", hardik_public_key)
print("Avesh's Public Key: ", avesh_public_key)

hardik_shared_secret = pow(avesh_public_key, hardik_private_key, p)
avesh_shared_secret = pow(hardik_public_key, avesh_private_key, p)  

print("Hardik's Shared Secret: ", hardik_shared_secret)
print("Avesh's Shared Secret: ", avesh_shared_secret)
