"""Problem statement:
Take a list of length 3 containing integers, find out which is larger, first or last one and set all the elements in the list to be that value. Print the updated list"""

l = [1,2,3]
l1 = []
n = max(l[0],l[-1])
for i in range(len(l)):
  l1.append(n)
print(l1)


Output:
[3, 3, 3]