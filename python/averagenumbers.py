numbers = [3, 4, 8, 7, 1]
running_sum = 0

for i in range(len(numbers)):
    print(numbers[i])
    running_sum = running_sum + numbers[i]

print(running_sum)

average = running_sum / len(numbers)

print(average)
