# for loop concept
# example 1
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
# example 2
num = [1,2,3,4,5,6,7,8,9,10]
for n in num:
    print(n)
print(num)
# find the highest score using for loop
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
maximum = max(student_scores)
print(maximum)
max=0
for n in student_scores:
    if max<n:
        max=n
print(max)
# for loop using range function
sum =0
for n in range(1,101):
    sum +=n
print(sum)
for n in range(1,11,1):
    print(n)