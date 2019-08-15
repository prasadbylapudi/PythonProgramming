def List(List1):
    List1.append(20);
    List1.append(30);
    print("list inside function",List1);


List1=[10,40,50,60]

#calling the function
List(List1);
print("list out side the function=",List1);



"""
In python, all the functions are called by reference, i.e., all the changes made to the reference inside the function revert back to the original value referred by the reference.

However, there is an exception in the case of mutable objects since the changes made to the mutable objects like string do not revert to the original string rather, a new string object is made, and therefore the two different objects are printed.

"""
