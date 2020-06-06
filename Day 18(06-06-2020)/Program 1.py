# The program takes a string and removes the nth index character from the non-empty string

s=str(input("enter the string"))
n=int(input("enter the nth index to remove"))
first_part = s[:n] 
last_part = s[n+1:]
res=first_part + last_part
print(res)

output:
enter the stringpython
enter the nth index to remove3
pyton
