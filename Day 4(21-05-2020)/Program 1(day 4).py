#Write a menu program in Python to find Area-Circle, Circumference-Circle, Area- Square, Circumference-Square using functions with menu choice
#Create seperate functions for each choice of menu


def arcir(r):
  print("Area of circle = ", 3.14*r*r, " cm²")
def crcir(r):
  print("Circumference of circle = ", 2*3.14*r, " cm ")
def arsq(s):
  print("Area of square = ", s*s, " cm²")
def crsq(s):
  print("Circumference of square = ", 4*s, " cm")
print("Menu: \n")
print("1.Area of Circle\n")
print("2.Circumference of Circle\n")
print("3.Area of Square\n")
print("4.Circumference of Square\n")
ch = int(input("Enter your choice\n"))
if(ch==1):
  r = int(input("Enter the radius\n"))
  arcir(r)
if(ch==2):
  r = int(input("Enter the radius\n"))
  crcir(r)
if(ch==3):
  s = int(input("Enter the side\n"))
  arsq(s)
if(ch==4):
  s = int(input("Enter the side\n"))
  crsq(s)
if(ch>4 or ch<=0):
  print("Invalid Choice")

Output:
Menu: 

1.Area of Circle

2.Circumference of Circle

3.Area of Square

4.Circumference of Square

Enter your choice
1
Enter the radius
6
Area of circle =  113.03999999999999  cm²


Menu: 

1.Area of Circle

2.Circumference of Circle

3.Area of Square

4.Circumference of Square

Enter your choice
2
Enter the radius
6
Circumference of circle =  37.68  cm 


Menu: 

1.Area of Circle

2.Circumference of Circle

3.Area of Square

4.Circumference of Square

Enter your choice
3
Enter the side
4
Area of square =  16  cm²


Menu: 

1.Area of Circle

2.Circumference of Circle

3.Area of Square

4.Circumference of Square

Enter your choice
4
Enter the side
4
Circumference of square =  16  cm