"""Write a python function that will take a string and checks whether it is a palindrome or not. Return If it a palindrome, print true else print false"""


s = str(input("Enter the string\n"))
a = s[::-1]
if a==s:
  print("True")
else:
  print("False")

Output:
Enter the string
pas
False

Enter the string
pap
True