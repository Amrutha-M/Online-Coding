"""Python program to find product of two arrays and count number of zeros in that array if any"""

l = [1,2,3,0,5,9,]
l1 = [2,3,4,5,1,0]
l2 =[]
for i,j in zip(l,l1):
    l2.append(i*j)
print(l2)
c =0
for i in l2:
  if(i==0):
    c = c+1
print("Number of 0's in the multiplied list : ",c)


Output:
The multiplied list :  [2, 6, 12, 0, 5, 0]
Number of 0's in the multiplied list :  2