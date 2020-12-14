import re

# digit at the beginning of the string and a digit at the end of the string
# A string that contains only whitespace characters or word characters
# A string containing no whitespace characters

# statement 1
pattern1 = '^\d.*.\d$'
str1 = '3abykjhss7'
result1 = re.match(pattern1,str1)
if result1:
    print("Statement 1 matched")
else:
    print("Statement 1 did not match")

# statement 2
pattern2 = '^\s|^[a-zA-Z]'
str2 = '   shayan'
result2 = re.match(pattern2,str2)
if result2:
    print("Statement 2 matched")
else:
    print("Statement 2 did not match")


# statement 3
pattern3 = '^((?!\s).)*$'
str3 = 'heywhatsup'
result3 = re.match(pattern3,str3)
if result3:
    print("Statement 3 matched")
else:
    print("Statement 3 did not match")