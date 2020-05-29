#Take a string as input and find the #number of uppercase and lower case #letters in the string and print the count.
#Note: any spaces has to be ignored

s = str(input("Enter the string"))
c=0
v=0
for i in s:
  if(i.islower()):
    c = c+1
  if(i.isupper()):
    v = v+1
print("Upper case characters : ",v)
print("Lower case characters : ",c)

Output:
Enter the stringThis is Python
Upper case characters :  2
Lower case characters :  10