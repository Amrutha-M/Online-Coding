"""Python program to combine strings

DESCRIPTION:
Take two strings, return a string of the form short+long+short, with the shorter string on the outsides and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0)."""


def combined_str(s1,s2):
  if len(s1)>len(s2):
    a = s2+s1+s2
    print("'{}'".format(a))
  else:
    a = s1+s2+s1
    print("'{}'".format(a))     
s1= str(input("Enter the 1st string\n"))
s2= str(input("Enter the 2nd string\n"))
combined_str(s1,s2)


Output:
Enter the 1st string
Hi
Enter the 2nd string
Hello
'HiHelloHi'