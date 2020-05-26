#Python Program to read a number n and #print the number of digits in it


a = int(input("Enter the number\n"))
c = 0
while(a>0):
  a = a//10
  c = c+1
print("The number of digits = ", c)


Output:
Enter the number
123
The number of digits =  3