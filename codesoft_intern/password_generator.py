'''password generator'''
import random
import string
lenpassword=int(input("Enter the desired length of the password:"))
symbols=['~','@','!','#','$','*','_','-',':',';','$','/','.']
numbers=[1,2,3,4,5,6,7,8,9,0]
list1=list(string.ascii_uppercase)
for i in string.ascii_lowercase:
    list1+=[i]
for n in numbers:
    list1+=[n]
for s in symbols:
    list1+=[s]
for p in range(lenpassword):
    character=random.choice(list1)
    print(character,end="")