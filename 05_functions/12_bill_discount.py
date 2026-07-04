def bill(amount):
    if  5000 <= amount :
        total = amount - ((20/100)*amount)
        print(f"Final Amount :{total}")
    elif 2000 <= amount < 5000 :
        total = amount - ((10/100)*amount)
        print(f"Final Amount :{total}")
    else :
        print(f"{amount}")
bill(1000)
bill(30000)
