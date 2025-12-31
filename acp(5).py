x = int(input("Enter the number: "))
n = int(input("Enter the power: "))

ans = 1
for i in range(n):
    ans = ans * x

print("Result:", ans)
