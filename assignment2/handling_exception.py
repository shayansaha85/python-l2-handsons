import time

i=1
try:
    while(i<5):
        time.sleep(1)
        print(i)
        i+=1
except KeyboardInterrupt:
    print("KeyboardInterrupt")
else:
    print("No exception")
finally:
    print("This is the final block")


try:
    name = shayan
    print("Hi " + name)
except NameError:
    print("NameError")
else:
    print("No exception")
finally:
    print("This is the final block")


try:
    a=25
    b = 0
    ans = a/b
    print(ans)
except ArithmeticError:
    print("ArithmeticError")
else:
    print("No exception")
finally:
    print("This is the final block")