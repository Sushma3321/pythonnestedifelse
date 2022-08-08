print("welcome  to bank world")
pin=2224
balance=5000
transaction=("balance enquiry","withdraw","deposit","quit")
pin=int(input("enter pin"))
if pin==2224:
    print("choos your transaction")
    print("1.balance enquiry")
    print("2.withdraw")
    print("3.deposit")
    print("quit")
    trans=input("transaction")
    language=input("enter language")
    if trans=="balance enquiry":
        if balance>0:
            print("your balance is",balance)
        else:
            print("nothing")
    elif trans=="withdraw":
        withdraw=int(input("enter withdraw amount"))
        if balance>withdraw:
            print("sucess your amount is now",balance-withdraw)
        else:
            print("insufiecient  balance")
    elif trans=="deposit":
        deposit=int(input("eneter deposit amount"))
        total_balnce=balance+deposit
        if balance>0:
            print("sucess your balnce is noe",total_balnce)
        else:
            print("something is wrong")
    elif trans=="quit":
        print("thanks for using bank")
else:
    print("wrong pin try again")

