a=[5,4,0,1,9]
i=0
c=[]
while i<len(a):
    b=a[i]+a[-(i+1)]
    c.append(b)
    if len(c)==2:
        break
    i=i+1
print(c)