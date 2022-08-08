string=input("enter number")
i=0
while i<len(string):
    j=0
    while j<len(string):
        print(string[i:j+1])
        j=j+1
    i=i+1


