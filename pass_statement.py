list = [1,2,3,4,5]  
flag = 0  
for i in list:  
    print("Current element:",i,end=" ");  
    if i==3:  
        pass;  
        print("\nWe are inside pass block\n");  
        flag = 1;  
    if flag==1:  
        print("\nCame out of pass\n");  
        flag=0;  
#pass statement
"""
Pass Statement
The pass statement is a null operation since nothing happens when it is executed.
It is used in the cases where a statement is syntactically needed but we don't want to use any executable statement at its place.

For example, it can be used while overriding a parent class method in the subclass but don't want to give its specific implementation in the subclass.

Pass is also used where the code will be written somewhere but not yet written in the program file.

The syntax of the pass statement is given below.
"""
