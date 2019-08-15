"""
In the large projects, sometimes we may not know the number of arguments to be passed in advance.
In such cases, Python provides us the flexibility to provide the comma separated values which are internally treated as tuples at the function call.

However, at the function definition, we have to define the variable with * (star) as *<variable - name >.
"""
#defining the function
def printme(*names):
    print("type of passed arguments",type(names));
    print("printing passed arguments");
    for i in names:
        print(i);
#calling function
printme("prasad","naveen","prabhas","darling","munna");
