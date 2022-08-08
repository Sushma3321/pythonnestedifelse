a=[10,18,15]
i=0
s=0
while i<len(a):
    if a[i]%5!=0:
        s=s+a[i]
        i=i+1
    i=i+1
print(s)
