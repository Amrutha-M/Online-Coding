"""Python Program to Map Two Lists into a Dictionary Steps: Get n rollnos through keyboard and put it in list L and respective test marks in list M. Write the program takes two lists and maps two lists into a dictionary D ."""



n = int(input("Enter the size\n"))
l = []
l1 = []
for i in range(0,n):
  rol = int(input("Enter the roll number\n"))
  marks = int(input("Enter the marks\n"))
  l.append(rol)
  l1.append(marks)
d = dict(zip(l,l1))
print(d)
  


Output:
Enter the size
3
Enter the roll number
1
Enter the marks
25
Enter the roll number
2
Enter the marks
26
Enter the roll number
3
Enter the marks
30
{1: 25, 2: 26, 3: 30}