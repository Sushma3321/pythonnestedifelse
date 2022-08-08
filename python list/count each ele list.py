list=[9,9,2,4,4,8,7,7,2,8,9,6,3,9]
i=0
c=[]
h=[]
while i<len(list):
    a=list.count(list[i])
    b=list[i],a
    c.append(b)
    if c[i] not in h:
        h.append(c[i])
    i=i+1
print(h)