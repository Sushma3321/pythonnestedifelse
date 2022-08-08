list=["sushma","pavani","rani"]

i=0
a=[]
while i<len(list):
    b=list[i][0].upper()
    a.append(b)
    i=i+1
c="."
d=c.join(a)
print([d])
