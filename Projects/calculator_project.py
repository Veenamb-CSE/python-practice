def main(num1):
    operators=["+","-","*","/"]
    for symbol in operators:
        print(symbol)
    s=(input("pick an operator"))
    num2=int(input("what's next number?:"))
    if s=="+":
        return num1+num2
    elif s=="-":
        return num1-num2
    elif s=="*":
        return num1*num2
    elif s=="/":
        return num1/num2
    else:
        return print("invalid operator")
while True:

    num1 = int(input("What's the first number?: "))

    result = main(num1)

    while True:

        ans = input(
            f"Type 'y' to continue calculating with {result}, "
            "or type 'n' to start a new calculation: "
        )

        if ans == "y":
            result = main(result)

        elif ans == "n":
            break