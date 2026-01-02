str = input("Please enter your string: ")
char = input("Please enter a character: ")
count = 0
i = 0

while i < len(str):
    if str[i] == char:
        count = count + 1
    i = i + 1

print("The number of times the character occurs in this string is,", count)