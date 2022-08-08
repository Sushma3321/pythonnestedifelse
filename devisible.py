num=int(input("Enter the number:"))
if num>=1500 and  num<=2700:
    if num%5==0 and num%7==0:
        print("Divisible by both")
    else:
        print("one or both condition is false")
else:
    print("Invalid")
