"""Python program to count number of strings

Description:
Write a Python program to count the number of strings, provided string length is 2 or more and the first and last character are same from a given list of strings."""


l = []
c = 0
n = int(input("Enter the number of elements\n"))
print("Enter the elements\n")
for i in range(n):
  l1 = str(input())
  l.append(l1)
for i in l:
    if(i[0] == i[-1]):
      c = (c+1)
print("The number of strings 1st and last character same\n",c)

Output:
Enter the number of elements
3
Enter the elements

hia
aba
363
The number of strings 1st and last character same
 2