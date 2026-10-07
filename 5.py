#input a number and check for even or odd.
#The whole process should continue till the user wants.

ans = 'y'
while ans == 'y':
    Num = int(input("Enter a number: "))
    if Num%2 == 0:
        print (Num," is an even number")
    else:
        print (Num," is an odd number")
    ans = input("Enter y to continue: ")
print ("Program ends here")
