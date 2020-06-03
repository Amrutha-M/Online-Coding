"""Python program to print prime numbers in the given range"""


n = int(input("Enter the 1st number\n"))
m = int(input("Enter the 2nd number\n"))
for i in range(n,m+1):
  if i>1 :
    for j in range(2,i):
      if((i%j)==0):
        break
    else:
      print(i)
        
Output:
Enter the 1st number
100
Enter the 2nd number
200
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199