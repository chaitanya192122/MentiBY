eUnits = int(input("entger no.of units used: "))

if eUnits<=100:
    print("you use ",eUnits," units : ",eUnits*2,"Rs")
elif eUnits>100 and eUnits<=200:
    print("you use ",eUnits," units : ",eUnits*3,"Rs")
else:
    print("you use ",eUnits," units : ",eUnits*5,"Rs")
