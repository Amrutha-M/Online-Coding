"""Python program to print frequency of alphabets in a string in a specific format"""


s = input("Enter the string\n")
s = sorted(s)
a = {}
for i in s:
  if i in a:
    a[i] += 1
  else:
    a[i] = 1
for key,val in a.items():
  print(key,val)        
    

Output:
Enter the string
python
h 1
n 1
o 1
p 1
t 1
y 1