name=input("enter your name")
age=int(input("enter your age"))
gender=input("eneter your gender")
if age>=18:
    if gender=='m':
        print('hello mr.',name,'welcome')
    else:
        print("hello mrs.',name,'welcome")
else:
    print("your not eligible")