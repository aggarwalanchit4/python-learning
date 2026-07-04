def atm(balance , debit):
    if debit <= balance:
        print(f"Amount reamining : {balance-debit}")
    else:
        print("insufficient balance")
atm(1000,500)
