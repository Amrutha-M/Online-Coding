"""Python program to Count the Number of Vowels Present in a String using Sets"""


s = str(input("Enter the string : "))
v = set("aeiouAEIOU")
c =0
for i in s:
  if i in v:
      c = c+1
print("Number of vowels : ",c)


Output:
Enter the string : python is good
Number of vowels :  4