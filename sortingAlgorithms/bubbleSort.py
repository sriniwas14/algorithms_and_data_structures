sorted = False
numbers = [9, 4, 7, 3]
n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):
        if(numbers[j]> numbers[j+1]):
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)