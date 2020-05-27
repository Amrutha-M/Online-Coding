#Python program to print all integers that aren't divisible either by 2 or 3 and lie between 1 and 50



a = [i for i in range(1,51) if(i%2!=0 and i%3!=0)]
print(a)


Output:
[1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]