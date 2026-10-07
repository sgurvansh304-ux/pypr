Gender = str(input("Enter Gender (M/F): "))
Age = int(input("Enter Age: "))

if Gender == "M" and Age >= 21:
    print("Eligible for Marriage")
elif Gender == "F" and Age >= 18:
    print("Eligible for Marriage")
else:
    print("Not Eligible for Marriage")
