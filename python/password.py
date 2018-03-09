import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWQYZ1234567890!@#$%^&*()'
password = ''
i = 0

while i < 20:
    password = password + random.choice(characters)
    i = i + 1

print(password)
