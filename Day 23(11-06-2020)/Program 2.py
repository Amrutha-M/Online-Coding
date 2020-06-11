"""Write a python function that converts a string to all uppercase, provided it contains at least 2 uppercase characters in the first 4 characters. Else print the string as it is"""


def upp(s):
  c =0
  for i in s:
    if i.upper() == i:
      c = c+1
  if(c>=2):
    print("The output string is : ",s.upper())
  else:
    print("The output string is : ",s)
s = str(input("Enter the string : "))
upp(s)


Output:
Enter the string : HeLlo
The output string is :  HELLO

Enter the string : hello
The output string is :  hello