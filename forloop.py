for i in range(10,0,-1):
    print(i)

# \n is a new-line character:

a = int(input("Enter the number who's sum you want to find: "))
sum = 0
for i in range(0, a-1):
    sum = sum+i
    print("\n",sum)
