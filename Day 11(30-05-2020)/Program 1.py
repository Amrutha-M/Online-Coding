#python program to print the pattern


def star(n):
  for i in range(0,n):
    for j in range(i-1,n-1):
      print("* ",end="")
      print("\r")
n = int(input("Enter the number\n"))
star(n)

Output:
Enter the number
5
* * * * * 

* * * * 

* * * 

* * 

*