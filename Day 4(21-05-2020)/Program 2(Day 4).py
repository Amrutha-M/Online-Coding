#Python program to print right angled triangle
n = int(input("Enter the number"))
for i in range(0,n+1):
  for j in range(n-i,0,-1):
    print(j,end ="")
  print("\r")


Output:
Enter the number7
7654321

654321

54321

4321

321

21

1