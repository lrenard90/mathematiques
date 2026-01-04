def suite(n):
    if n == 0:
        return 8
    return 0.75*suite(n-1) + 3

print("suite(100) =", suite(100))