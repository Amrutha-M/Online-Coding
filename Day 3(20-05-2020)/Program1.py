Python Program to Exchange the Values of Two Numbers using ^ (exclusive or operator)



Program:



x=int(input("x= "))

y=int(input("y= "))

print ("Before Swapping: x = ", x, " y =", y)

x = x ^ y;

y = x ^ y;

x = x ^ y;

print ("After Swapping: x = ", x, " y =", y)



Output:

x= 54

y= 68

Before Swapping: x =  54  y = 68

After Swapping: x =  68  y = 54