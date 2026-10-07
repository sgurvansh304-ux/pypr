# Program to add natural
# numbers up to
# sum = 1+2+3+.....+n

n = int(input("Enter the value of n: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i += 1
print("The sum is", sum)
