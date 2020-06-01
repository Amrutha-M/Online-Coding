#Write a Python program which accepts a #sequence of comma-separated numbers #from user and generate a list and a tuple #with those numbers.


l = input("Enter the numbers : ")
list = l.split(",")
tuple = tuple(list)
print(list,"\n",tuple)


Output : 
Enter the numbers : 1,2,3,4
['1', '2', '3', '4'] 
('1', '2', '3', '4')