num = [-2,1,-3,4,-1,2,1,-5,4]
i=0
sum=0
maxsum=num[0]
while i<len(num):
    if sum<0:
        sum=0
    sum=sum+num[i]
    maxsum=max(maxsum,sum)
    i=i+1
print(maxsum)

        