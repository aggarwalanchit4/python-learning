def greatest(a, b, c):

    if a > b and a > c:
        print(f"{a} is greatest among {a}, {b} and {c}")

    elif b > a and b > c:
        print(f"{b} is greatest among {a}, {b} and {c}")

    else:
        print(f"{c} is greatest among {a}, {b} and {c}")


greatest(10, 11, 12)
greatest(12, 11, 10)
greatest(11, 12, 10)
