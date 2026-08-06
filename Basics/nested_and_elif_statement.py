print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill =0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int (input("enter yor age"))
    if age <=12 :
        bill=5
        print("ticket 5$")
    elif age <=18 :
        bill=7
        print("ticket 7$")
    else :
        bill=12
        print("ticket 12$")
    wants_photo=(input("you want to take photo or not give y for yes n for no"))
    if wants_photo == "y" :
        bill +=3

    print(f"your final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")