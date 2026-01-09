num = int(input("Enter a number: "))
cntr = 0

if num == 0:
    cntr = 1
else:
    while num != 0:
        cntr+=1
        num//=10
print(cntr)