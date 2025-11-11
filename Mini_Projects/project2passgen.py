import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','M','N','O','P','Q','R','S','T','U','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','10']
symbols=['@','!','#','$','%','^','&','*','(',')']

print('hey WELCOME TO PASSWORDV GENERATOR')
no_letters=int(input("how many letters you want"))
no_symbols=int(input("how many symbols you want"))
no_numbers=int(input("how many numbers you want"))

password=[]
for i in range(1,no_letters+1):
    char = random.choice(letters)
    password +=char

for i in range(1,no_symbols+1):
    char = random.choice(symbols)
    password +=char

for i in range(1,no_numbers+1):
    char = random.choice(numbers)
    password +=char

#print(password)

random.shuffle(password)
#print(password)

npassword=""
for char in password:
    npassword += char
print(npassword)  




    
