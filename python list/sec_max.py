numbers = [50, 40, 23,70,  56, 12, 5, 10, 7]
max=numbers[0]
i=0
second_max=numbers[0]
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    elif numbers[i] >second_max  and max>second_max:
        second_max=numbers[i]
    i=i+1
print(second_max)