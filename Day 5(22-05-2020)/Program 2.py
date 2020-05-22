#Python Program to find sum of array
#Given an array of integers(take input from #keyboard), find sum of its elements.
a = []
n = int(input("Enter the size of array\n"))
print("Enter the array elements\n")
for i in range(n):
  num = int(input())
  a.append(num)
print("The sum is = ", sum(a))

Output: 
Enter the size of array
4
Enter the array elements
1
2
3
4
The sum is =  10