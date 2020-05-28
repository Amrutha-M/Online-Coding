#Python program to find digital root of a #number


n = int(input("Enter the digit\n"))
def digital_root(n): 
    m  = len(str(n))
    s=0 
    for i in range(m):
        s = s+ n%10
        n = n//10
    print(s)
    if(len(str(s))>1):
        return(digital_root(s))
    
print(digital_root(n))

    
Output:
Enter the digit
162536738292
54
9

Enter the digit
0
0