a = int(input("What units have you consumed? "))
if a<=50:
    print("You have to pay", a*2.60+50)
elif a>50 and a<100:
    print("You have to pay", a*3.25+35)
elif a>100 and a<200:
    print("You have to pay", a*5.26+45)
elif a>200:
    print("You have to pay", a*8.45+75)
    