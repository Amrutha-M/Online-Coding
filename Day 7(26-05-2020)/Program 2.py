#This is a Python Program to read a number n and print and compute the series “1+2+…+n=”.
#Problem Description
#The program takes a number n and prints and computes the series “1+2+…+n=”.



n = int(input("Enter the number\n"))
series_sum= []
for i in range(1,n+1):
  series_sum.append(i)
  if(i==n):
    print(i,end="")
  else:
    print(i,end="+")
print("=",sum(series_sum))

Output:
Enter the number
5
1+2+3+4+5= 15