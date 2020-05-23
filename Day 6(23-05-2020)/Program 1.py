#Python program to print positive numbers #in a list
#Given a list of numbers, write a Python #program to print all positive numbers in #given list.

a = []
n = int(input("Enter the size of list\n"))
print("Enter the list elements\n")
#print("The postive numbers are")
for i in range(n):
  num = int(input())
  a.append(num)
print("The postive numbers are\n")
for num in a:
  if(num>0):
    print(num)


Output:

 Enter the size of list
5
Enter the list elements
1
-56
-5
3
6
The postive numbers are
1
3
6