# Python Program to Reverse a String Using Recursion

def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]

mystr =str(input("enter the sting"))
print("The Given String  is: ", mystr)
print("Reversed String is: ", reverse(mystr))

output:
enter the stingpython
The Given String  is:  python
Reversed String is:  nohtyp
