#python program which takes a string as #an input from user and print only the #consonants in the string format



s = str(input("Enter the string\n"))
c =""
for val in s:
  if(val=='a' or val=='e' or val=='o' or val=='u' or val=='i'):
    continue
  else:
    c = c+ str(val)
print(c)

Output:
Enter the string
I love python
I lv pythn