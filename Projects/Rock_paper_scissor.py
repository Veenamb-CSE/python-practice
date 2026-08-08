import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
num= [0,1,2]
name = int(input("enter your choice for 0 rock,1 paper,2 scissors"))
if name == 0 :
    print(rock)
elif name == 1 :
    print(paper)
elif name == 2 :
    print(scissors)
else:
    print("invalid number")
computer_choice = random.choice(num)
print(f"computer choice is {computer_choice}")
if computer_choice == 0 :
    print(rock)
elif computer_choice == 1 :
    print(paper)
else :
    print(scissors)
if (name ==0 and computer_choice == 2)or (name==1 and computer_choice == 0) or (name==2 and computer_choice == 1):
    print("you win")
elif (name==0 and computer_choice ==1) or (name==1 and computer_choice ==2) or (name==2 and computer_choice ==0):
    print("you loss")
elif name == computer_choice:
    print("game draw")