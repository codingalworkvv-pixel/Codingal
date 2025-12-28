a = int(input("Enter speed: "))
b = int(input("Enter speed: "))
c = int(input("Enter speed: "))

avgspeed = (a+b+c)/3
print(avgspeed)

if avgspeed > a and avgspeed > b and avgspeed > c:
    print("Average speed is greater than a, b and c")
elif avgspeed > a and avgspeed > b:
    print("Average speed is greater than a and b only")
elif avgspeed > a and avgspeed > c:
    print("Average speed is greater than a and c only")
elif avgspeed > b and avgspeed > c:
    print("Average speed is greater than b and c only")
elif avgspeed > a:
    print("Average speed is greater than a only")
elif avgspeed > b:
    print("Average speed is greater than b only")
elif avgspeed > c:
    print("Average speed is greater than c only")
else:
    print("Invalid")