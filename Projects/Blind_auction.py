logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
dictionary={}
def max_amount(dic):
    maximum=0
    winner=""
    for i in dic:
        if dic[i]>maximum:
            maximum=dic[i]
            winner=i
    print(f"the winner is {winner} and the maximum amount is {maximum} ")
con=True
while con:
    name=input("enter your name: ")
    amount=int(input("enter your amount: "))
    dictionary[name]=amount
    final_ans=input("if you  any person is there say 'yes'.otherwise say 'no")
    if final_ans=="yes":
        print("\n"*20)
    elif final_ans=="no":
        con=False
        max_amount(dictionary)

