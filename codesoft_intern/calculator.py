'''Basic calculator'''
NUM1=int(input("Enter a number:"))
NUM2=int(input("Enter a number:"))
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
list1=[1,2,3,4]
Userchoice=int(input("What operation wants you to be performed choose(1,2,3,4):"))
'''def'''
def cal():
      if(Userchoice==list1[0]):
        print("Sum of Two numbers:",NUM1+NUM2)
      elif(Userchoice==list1[1]):
        print("Subtraction of two numbers:",NUM1-NUM2)
      elif(Userchoice==list1[2]):
        print("Multiplication of two numbers:",NUM1*NUM2)
      else:
        print("Division of two numbers:",NUM1/NUM2)
'''def call'''
cal()