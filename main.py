import random

character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
long = int(input("how long is the password ? "))

for i in range(long):
    password += random.choice(character)

print(password)
