#Python program to print all Prime #numbers in an Interval
#Given two positive integer start and end. #The task is to write a Python program #toprint all Prime numbers in an Interval.


start = int(input("Enter the first number\n"))
end = int(input("Enter the last number\n"))
print("The prime numbers in the given range are : \n")
for i in range(start,end+1):
  if (i>1):
    for j in range(2,i):
      if(i%j==0):
        break
    else:
        print(i,"\n")
  

Output:
Enter the first number
2
Enter the last number
20
The prime numbers in the given range are : 

2 

3 

5 

7 

11 

13 

17 

19