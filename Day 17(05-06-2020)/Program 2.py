#Python Program to Take in the Marks of 5 Subjects and Display the Grade using if ... elif construct without using and operator for finding the range

sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=float((sub1+sub2+sub3+sub4+sub4)/5)
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")


output:
Enter marks of the first subject: 90
Enter marks of the second subject: 98
Enter marks of the third subject: 87
Enter marks of the fourth subject: 99
Enter marks of the fifth subject: 92
Grade: A
