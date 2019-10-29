numbers = [9, 4, 7, 3]

for i in range(len(numbers)):
    minIndex = i

    for j in range(i+1, len(numbers)):
        if(numbers[minIndex]>numbers[j]):
            minIndex=j

    numbers[i], numbers[minIndex] = numbers[minIndex], numbers[i]

print(numbers)