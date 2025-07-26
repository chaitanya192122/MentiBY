sub1= int(input("telugu marks : "))
sub2= int(input("english marks : "))
sub3= int(input("math marks : "))
sub4= int(input("phy marks : "))
sub5= int(input("chemistery marks : "))
avg=((sub1+sub2+sub3+sub4+sub5)/500)*100

if sub1<35 or sub2<35 or sub3<35 or sub4<35 or sub5<35:
    print("Fail")
elif avg>=75:
    print("Excellent")
elif avg>=60:
    print("Very Good")
elif avg>=40:
    print("good")
else:
    print("Pass")