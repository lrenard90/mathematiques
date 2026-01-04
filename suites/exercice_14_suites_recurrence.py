def suite_recursive(n):
    if n == 0:
        return 2
    return 2*suite_recursive(n-1) - 3

print("suite_recursive(15) =", suite_recursive(15))
print("suite_recursive(20) =", suite_recursive(20))
print("suite_recursive(25) =", suite_recursive(25))