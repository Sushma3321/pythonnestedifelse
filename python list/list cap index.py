# a=PaVaN
# 
# [0,2,4]


a="PaVaN"
b=[]
i=0
while i<len(a):
    if a[i]==a[i].upper():
        b.append(i)
    i=i+1
print(b)