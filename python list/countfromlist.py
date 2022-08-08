# Write a code, that counts the numbers between 20 and 40 and then print its count.

list=[50, 40, 23, 70, 56, 12, 5, 10, 7]
index=0
count=0
while index<len(list):
    numbers=list[index]
    if numbers>20 and numbers<40:
        count=count+1
    index=index+1
print(count) 