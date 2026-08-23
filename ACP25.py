import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

characters = lower + upper + numbers

password = ""

length = int(input("Enter password length"))

for i in range(length):
    password += random.choice(characters)

print("Random Password:", password)