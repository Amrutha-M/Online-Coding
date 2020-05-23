Write Python Program to Reverse a Given Number This is a Python Program to reverse a given number. Problem Description The program takes a number and reverses it and store it in another variable and show it

Program: 

n = int(input("Enter the number\n"))
m = 0
while(n!=0):
  rem = n%10
  m = m*10 + rem
  n = n//10
print("The rever number is\n",m)


    
Output :
Enter the number
3456
The rever number is
6543