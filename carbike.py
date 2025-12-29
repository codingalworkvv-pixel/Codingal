a = int(input("Select your ride: Press 1 for bike, Press 2 for car "))
if a==1:
    print("You have chosen a bike! ")
    b = int(input("Select your bike: Yamaha(1) or Ducati(2) "))
    if b==1:
        print("You have chosen Yamaha")
    elif b==2:
        print("You have chosen Ducati")
    else:
        print("Invalid")
elif a==2:
    print("You have chosen a car")
    c = int(input("Choose your car: Toyota(1) and Hyundai(2)"))
    if c==1:
        print("You have chosen Toyota")
    elif c==2:
        print("You have chosen Hyundai")
    else:
        print("Invalid")
else:
    print("Invalid Selection")