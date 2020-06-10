"""Python program to find number of even and odd numbers"""


tuple = (1,2,3,4,5,6,7)
c,c1=0,0
for i in tuple:
  if(i%2==0):
    c = c+1
  else:
    c1 = c1+1
print("The count of even numbers is : ",c)
print("The count of odd numbers is : ",c1)


Output:
The count of even numbers is :  3
The count of odd numbers is :  4