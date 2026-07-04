for i in range(2, 21 , 2):
    print(i)

def even(k):
    for i in range(1,k+1,1):
        if i%2==0:
            print(i)

even(10)

def odd(k):
    for i in range(1,k+1,1):
        if i%2!=0:
            print(i)

odd(10)
