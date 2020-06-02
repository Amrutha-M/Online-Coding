#Python program to print 1st and last #element of a list using slice method

l = []
n = int(input("Enter the size of list\n"))
print("Enter the list elements\n")
for i in range(n):
  l1 = int(input())
  l.append(l1)
print(l[slice(0,n+1,n-1)])


Output:
Enter the size of list
4
Enter the list elements
1
2
3
4
[1, 4]