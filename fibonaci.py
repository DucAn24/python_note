def fibonacci(n):
    """
    Tính số Fibonacci thứ n (bắt đầu từ 0)
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(2) = 1
    fibonacci(3) = 2
    ...
    """
    if n < 0:
        raise ValueError("n phải >= 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Sử dụng vòng lặp để tính Fibonacci
    a, b = 0, 1  # fibonacci(0) và fibonacci(1)
    for _ in range(2, n + 1):
        a, b = b, a + b  # Cập nhật: a = b, b = a + b
    return b

n = int(input())
print(fibonacci(n))