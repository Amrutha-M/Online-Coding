"""Python program to check whether the given number is fibonacci or not"""


def fib(n):
    if(n == 0):
      return 0
    elif(n == 1):
      return 1
    else:
      return (fib(n - 2) + fib(n - 1))
n = 20
a = [fib(i) for i in range(n)]
z = int(input("Enter the number\n"))
if z in a:
  print(z,"is a fibonacci number")
else:
  print(z,"is not a fibonacci number")


Output:
Enter the number
8
8 is a fibonacci number

Enter the number
10
10 is not a fibonacci number