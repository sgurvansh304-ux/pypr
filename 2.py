N1 = int(input("Enter the first number: "))
N2 = int(input("Enter the second number: "))
N3 = int(input("Enter the third number: "))

if N1 >= N2 and N1 >= N3:
    print("The largest number is: ", N1)
elif N2 >= N1 and N2 >= N3:
    print("The largest number is: ", N2)
else:
    print("The largest number is: ", N3)
