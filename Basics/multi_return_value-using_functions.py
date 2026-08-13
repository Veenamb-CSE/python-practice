# example 1
def format_name(f_name, l_name):
    if f_name =="" and l_name=="":
        return ""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f" result: {formated_f_name} {formated_l_name}"


print(format_name(input("Enter your first name: "), input("Enter your last name: ")))
age=int(input("Enter your age: "))
# example 2
def canBuyAlcohol(age):
    if type(age) != int:
        return ""

    if age >= 18:
        return True
    else:
        return False
canBuyAlcohol(age)
print(canBuyAlcohol(age))
