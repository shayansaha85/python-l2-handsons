import math


def factorial(n):
    ans=1
    for i in range(1,(n+1)):
        ans = ans*i
    print("Factorial : {0}".format(ans))


def find_log10(n):
    if float(n)>0:
        ans = math.log10(float(n))
        print(f"log10({n}) = {ans}")
    else:
        print("Please enter value greater than 0")


def degree_to_radian(n):
    ans =  float(n)*(math.pi/180)
    print("{0} Degrees = {1} radians".format(n,ans))


def find_sin_cos_tan(n):
    n_in_radians = float(n)*(math.pi/180)
    sinValue = math.sin(n_in_radians)
    cosValue = math.cos(n_in_radians)
    tanValue = math.tan(n_in_radians)
    print("sin({0}) = {1}".format(n,sinValue))
    print("cos({0}) = {1}".format(n, cosValue))
    print("tan({0}) = {1}".format(n, tanValue))

