Amount = int(input("Enter the amount to withdraw: "))

notes100 = Amount//100
notes50 = (Amount%100)//50
notes10 = ((Amount%100)%50)//10

print(notes100, notes50, notes10)