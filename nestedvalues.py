a = input("What is your medical condition? ")
if a=="Y":
    print("you can take the exam")
else:
    b = int(input("What is your attendance? "))
    if b>=75:
        print("You can take the exam")
    else:
        print("Not allowed to take the exam")