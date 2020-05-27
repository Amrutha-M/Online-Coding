#Python program to check if a number is palindrome


num = int(input("Enter the number\n"))
n =num
rev=  0
while(n>0):
    rem = n%10
    rev = (rev*10)+rem
    n = n//10
if(rev == num):
    print("The number is palindrome")
else:
    print("The number is not a palindrome")


Output:
Enter the number
787
The number is palindrome

Enter the number
6789
The number is not a palindrome