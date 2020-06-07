"""Python program to square each odd number in the list

Description:
Take a list of numbers and square each odd number in the list. Print output as comma separated sequence."""

l = []
n = int(input("Enter the size of the list\n"))
for i in range(n):
  l1 = int(input())
  l.append(l1)
print("The squares of odd numbers")
for i in l:
  if(i%2!=0):
    if i==n:
      print(i*i)
    else:
      print(i*i,end = ",")

Output:
Enter the size of the list
5
1
2
3
4
5
The squares of odd numbers
1,9,25