t=input()
numbers = input("Enter numbers separated by space ")
numberList = numbers.split()
print("\n")
print("All entered numbers ", numberList)
sum1 = 0
for num in numberList:
    sum1 += int(num)

average = sum1 / len(numberList)
print(max(numberList))
print(min(numberList))
print("Average of all entered numbers = ", average)
