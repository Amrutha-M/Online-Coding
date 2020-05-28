#Python program to print the greatest #number in a list
#Note: No usage of sort()


l = []
n = int(input("Enter the size of the list\n"))
print("Enter the elements")
for i in range(n):
  x = int(input())
  l.append(x)
print("The greatest number in the list is = ", max(l))


Output:
Enter the size of the list
4
Enter the elements
56
76
23
68
The greatest number in the list is =  76