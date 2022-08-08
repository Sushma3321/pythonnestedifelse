list=["abca","xyz","xyzx","sts"]
i=0
sum=0
while i<len(list):
    if list[i][0]==list[i][-1]:
        sum=sum+1
    i=i+1
print(sum)
