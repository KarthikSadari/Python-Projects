#Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!','#','$','%','&','/','(',')','*',':',';','<','>','?','@','[',']','^','_','{','|','}','~']
numbers = ['1','2','3','4','5','6','7','8','9','0']

print("Welcome to the Password Generator!!!!")

i_letter = int(input("How many latters would you want in your password: "))
i_symbol = int(input("How many symbls would you want in your password: "))
i_number = int(input("How many numbers would you want in your password: "))

password_list = []

for i in range(1,i_letter+1):
    char = random.choice(letters)
    password_list += char
    
for i in range(1,i_symbol+1):
    symb = random.choice(symbols)
    password_list += symb
    
for i in range(1,i_number+1):
    nums = random.choice(numbers)
    password_list += nums

    
random.shuffle(password_list) #This line shuffles the list items


password = ""

for k in password_list:
    password += k
    
print("Here is Your Password: ",password)
 