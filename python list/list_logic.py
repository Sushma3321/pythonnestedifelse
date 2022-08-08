n=int(input("enter number"))
i=0
while n>0:
    digit=n%10
    sum=digit*digit
    n=n//10
    d=n*n
    print(d,end=" ")
    print(sum)
    break
    
    