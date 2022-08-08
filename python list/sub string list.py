

string=input("enter the string")

i=0
list=[]
while i<len(string):
    j=1
    while j<len(string):
        a=string[i:j]
        list.append(a)
        if a=="":
            break
        if a not in list:
            break
        j=j+1
      
    i=i+1
print(len(list))
print(list)




   