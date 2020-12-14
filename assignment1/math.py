import cal

try:
    a = int(input("Enter a number for finding factorial = "))
    cal.factorial(a)
except Exception:
    print("Please enter a valid value")

d = input("Enter a degree value for finding out the sin/cos/tan functions = ")
cal.find_sin_cos_tan(d)