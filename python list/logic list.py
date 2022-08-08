list=[1,2,3,4,5,6,7,8,9,10]
a="sushma"
c=[]
i=0
while i<len(list):
    if list[i]%2==0:
        c.append(a)
    else:
        c.append(list[i])
    i=i+1
print(c)