def calculate(n1,n2,operator):
    if operator=='+':
        return n1+n2
    elif operator=='-':
        return n1-n2
    elif operator=='*':
        return n1*n2
    elif operator=='/':
        if n2==0:
            return "Error: Invalid operator"
        return n1/n2
    else:
        return "Error: Invalid operator"
n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))
operator=input("Enter the operator(+,-,*,/):")
result=calculate(n1,n2,operator)
print(f"The result is:{result}")
