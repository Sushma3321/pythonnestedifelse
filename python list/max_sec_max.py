numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=numbers[0]
second_max=numbers[0]
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    if numbers[i]>second_max and numbers[i]!=max:
        second_max=numbers[i]
    i+=1
print(second_max)

