#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

with open("numbers.txt") as file:
    numbers = [float(line) for line in file]

totalCount = len(numbers)
totalSum = sum(numbers)
totalAverage = totalSum / totalCount
highestNumber = max(numbers)
lowestNumber = min(numbers)

print(f"The total amount of numbers in the list: {totalCount}")
print(f"The sum of all numbers in the list: {totalSum}")
print(f"The average of all numbers in the list: {totalAverage}")
print(f"The highest number within the list: {highestNumber}")
print(f"The lowest number within the list: {lowestNumber}")

#end of script