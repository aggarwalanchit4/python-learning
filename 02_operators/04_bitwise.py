#bitwise and
print(2&3)
#bitwise or
print(2 | 3)
#bitwise xor
print(2 ^ 3)

#to check given number is power of 2

n = int(input("Enter number: "))

if n>0 and (n & (n - 1)) == 0:
    print(n, "is a power of 2")
else:
    print(n, "is not a power of 2")
