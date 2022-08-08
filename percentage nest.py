a=int(input("enter classes"))
b=int(input("enter the attend classes"))
percentage=int(input("enter percentage"))
gender=input("enter the gender")
if percentage>75 and gender=="f":
    print("you can write exam")
elif percentage<=75 and gender=="m":
    print("you can write exam")
else:
    print("your not eligible")