import random
import string
length=int(input("Enter the size for password..."))
numbers=input("can we include numbers(yes/no)?..").lower()
symbols=input("can we include symbols(yes/no)?..").lower()
characters=string.ascii_letters
if numbers == 'yes':
    characters += string.digits
if symbols == 'yes':
    characters += string.punctuation
password=""
for i in range(length):
    password += random.choice(characters)
print("YOUR GENERATED  PASSWORD🔑: ",password)


