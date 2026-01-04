def suite_recursive(n):
    if n == 0:
        return 3
    return 4*suite_recursive(n-1) - 6

print("suite_recursive(13) =", suite_recursive(13))

def suite_recursive_print(n):
    if n == 0:
        u = 3
        print(f"U({n}) = 3")
    else:
        u = 4*suite_recursive_print(n-1) - 6
        print(f"U({n}) = 4U({n-1}) - 6 = {u}")
    return u

print("suite_recursive_print(13) =", suite_recursive_print(13))

def suite_iterative(n):
    u = None
    for i in range(0, n):
        if i == 0:
            u = 3
            print("Iteration", i+1, ": U(0) = 3")
        u = 4*u - 6
        print("Iteration", i+2, ":", f"U({i+1}) = {u}")
    return u

print("suite_iterative(13) =", suite_iterative(13))