#python program to delete duplicate #elements from the list



#by giving input within 
l = [1,2,3,4,4,5,5,6]
l1 = set(l)
l = list(l1)
print(l)
print(" ")
#by taking inputs from user
l2 = []
n = int(input("Enter the size of list\n"))
print("Enter the elements of list")
for i in range(n):
  x = int(input())
  l2.append(x)
l3 = set(l2)
l2 = list(l3)
print(l2)


Output:
[1, 2, 3, 4, 5, 6]
 
Enter the size of list
4
Enter the elements of list
1
1
2
3
[1, 2, 3]