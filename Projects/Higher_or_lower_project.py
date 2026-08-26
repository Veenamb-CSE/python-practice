import random
from game_data import data
from art import logo,vs
print(logo)
A = random.choice(data)
print(A)
print(f"compare A:{A["name"]},a {A["description"]}, from {A["country"]}")
B = random.choice(data)
print(vs)
print(B)
print(f"Against B:{B["name"]},a {B["description"]}, from {B["country"]}")
score=0
loop=True
while loop:
    ans = input("Who has more followers? Type 'A' or 'B': ")
    if ans=="A":
        if A["follower_count"]>B["follower_count"]:
            A=A
            B=random.choice(data)
            print(f"compare A:{A["name"]},a {A["description"]}, from {A["country"]}")
            print(f"Against B:{B["name"]},a {B["description"]}, from {B["country"]}")
            score+=1
            print(f"You're right! Current score:{score}")
        else:
            print(f"Sorry, that's wrong. Final score:{score}")
            loop=False
    elif ans=="B":
        if A["follower_count"]<B["follower_count"]:
            A=B
            B=random.choice(data)
            print(f"compare A:{A["name"]},a {A["description"]}, from {A["country"]}")
            print(f"Against B:{B["name"]},a {B["description"]}, from {B["country"]}")
            score+=1
            print(f"You're right! Current score:{score}")
        else:
            print(f"Sorry, that's wrong. Final score:{score}")
            loop=False
    else:
        print("please enter either 'A' or 'B': ")
        break






