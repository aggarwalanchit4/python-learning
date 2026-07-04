def fact(x):
    result=1
    for i in range(1,(x+1),1):
        result=result*i
    print(result)
fact(3)
fact(9)

def fact(n):

    x = 1

    for i in range(1, n+1):
        x = x * i

    return x

print(fact(8))
