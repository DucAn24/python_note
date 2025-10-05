def factorial(n):
    """
    Tính giai thừa của n (n!)
    factorial(0) = 1
    factorial(1) = 1
    factorial(2) = 2
    factorial(3) = 6
    factorial(4) = 24
    ...
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n phải là số nguyên không âm")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input())
print(factorial(n))
