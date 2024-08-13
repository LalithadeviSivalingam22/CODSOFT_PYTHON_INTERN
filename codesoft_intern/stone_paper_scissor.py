'''random modulue'''
import random

'''def '''

def Game():
  print("1.Stone")
  print("2.Scissor")
  print("3.Paper")
  Userchoice=int(input("Enter your choice (choose 1,2,3):"))
  list1=[1,2,3]

  '''User choice'''

  if(list1[0]==Userchoice):
    print("Userchoice:Stone")
  elif(list1[1]==Userchoice):
    print("userchoice:scissor")
  else:
    print("userchoice:paper")

  '''Computer choice'''

  list2=["Stone","scissor","paper"]
  item=random.sample(list2,1)
  for i in item:
    computerchoice=i
    print("computerchoice:",computerchoice)
  
  '''display result'''
  
  if list2[Userchoice-1]==computerchoice:
    print('game tie')
  elif Userchoice=='paper' and computerchoice=='scissors':
    prin('user loss')
  elif Userchoice=='paper' and computerchoice=='stone':
    print('user win')
  elif Userchoice=='stone' and computerchoice=='paper':
    print('user loss')
    print(loss) 
  elif Userchoice=='scissors' and computerchoice=='paper':
    print('user win')
  elif Userchoice=='stone' and computerchoice=='scissor':
   print('user win')
  else:
    print('user loss')
  
  ''' play again'''

  Userwise=input("if u want to play(say yes 0r no):").lower()
  if Userwise=='yes':
       Game()
  else:
       exit()

'''def call'''

Game()