#program to reverse the digits of a number
Num = int(input("Enter a number: "))
Dig = 0
while Num>0:
    R = Num%10
    Dig = (Dig*10)+R
    Num //= 10
print(Dig)
