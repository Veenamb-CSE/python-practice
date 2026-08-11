import random
# example 1
def greet():
    print("Hello World")
    print("hi veena ")
    print("hello vinoda")
greet()
# example 2
name1 = input("what is your name? ")
friend = input("what is your friend's name? ")
def greet_with_name(name1,friend):
    print(f"hi, my name is  {name1} and my friend name is  {friend}")
greet_with_name(name1,friend)
# example 3
age=random.randint(1,91)
x=(90-age)*52
def life(x):
    print(f"you have left with {x} weeks.")
life(x)