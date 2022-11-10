

grade=88
grade=int(input("enter your grade: "))
if grade >=90:
    print("A grade")
    grade=int(input("enter your grade: "))
elif grade >= 80:
    print("B grade")
    grade=int(input("enter your grade: "))
elif grade >= 70:
    print("C grade")
    grade=int(input("enter your grade: "))
elif grade >= 65:
    print("D grade")
    grade=int(input("enter your grade: "))
else:
    print("your result is very poor")