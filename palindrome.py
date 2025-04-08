#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file will be used for grading.
#Correct answer for this file: 

def palindrome(word):
    return word == word[::-1]

with open("words.txt") as file:
    words = [line.strip().lower() for line in file if line.strip()]

palindromes = [word for word in words if palindrome(word)]

print("The total number of palindromes within the list:", len(palindromes))

#end of script