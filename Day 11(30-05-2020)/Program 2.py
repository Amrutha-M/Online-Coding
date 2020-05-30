#python program to delete an element at #the given position


s = str(input("Enter the string\n"))
n = int(input("Enter the position of element to be deleted\n"))
m  = len(str(s))
s1 = ""
for i in range(m):
  if(i!=n-1):
    s1 = s1 + s[i]
print(s1)


Output:
Enter the string
python
Enter the position of element to be delete 
2
pthon