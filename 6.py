def division(numerator,divisor):
    try:
        result=numerator/divisor
        return result
    except ZeroDivisionError:
        return "Error:Division by zero is not allowed."
numerator=float(input("Enter the numerator:"))
divisor=float(input("Enter the divisor:"))
result=division(numerator,divisor)
print(result)

