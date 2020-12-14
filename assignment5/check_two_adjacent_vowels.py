import re

list = []
n = int(input("How many characters do you want to enter? = "))
for k in range(0, n):
    el = input("Word #{0} = ".format((k + 1)))
    list.append(el)

regexp = '[aeiouAEIOU]{2}'
for i in range(0, len(list)):
    if re.match(regexp, str(list[i])):
        print(str(list[i]))
