num = int(input("Enter a 4 digit number: "))

count = 0
temp = num
product = 1

while temp > 0:
    count +=1
    temp //= 10


for i in range(count):
    digit = num % 10
    for j in range(1):
        if i == 1 or i == 2:
            product *= digit
    num //=10

print("Mid Point: ", product)