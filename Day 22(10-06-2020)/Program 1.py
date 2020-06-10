"""Python program to find length of list using recursion"""


def length(l):
    if l == []:
      return 0
    else:
      return 1 + length(l[1:])
l = [1,2,3,4,5]
print("Length is: ", length(l))



Output:
Length is:  5