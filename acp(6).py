num = float(input("Enter a decimal number: "))
bin = ""

while num > 0:
    bin = str(num%2) + bin
    num = num // 2

print("Binary number is:", bin)