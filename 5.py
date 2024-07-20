def fibonacci(n):
    if n<0:
        raise ValueError("Input should be non-negative integer")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=int(input("Enter the position:"))
print(f"Fibonacci number at position {n} is {fibonacci(n)}")