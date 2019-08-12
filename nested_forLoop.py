n=int(input("enter no of rows to print"));
i,j=0,0;#i,j=0;it can't work here.
for i in range(0,n):
    print(" ");#print() also u can use
    for j in range(0,i+1):
        print("*",end="");#without the end="" output should print in single column
        #it can't print like the star pattern.
        
