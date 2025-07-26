tside1=int(input("enter length of a : "))
tside2=int(input("enter length of b : "))
tside3=int(input("enter length of c : "))
if tside1==tside2==tside3:
    print("Equilateral")
elif tside1==tside2 or tside2==tside3 or tside3==tside1:
    print("Isosceles")
elif tside1!=tside2!=tside3:
    print("Scalene")
else:
    print("Invalide Triangle")
