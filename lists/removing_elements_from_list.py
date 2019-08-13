List=[1,2,3,4,5,6,7,89];
print("this is original list");
print(List);
List.remove(1);#here it is not index,it is element,u need to give element.
print("this is after removal of first element");
print(List);



#NOTE:
"""
What is the difference between the remove, del and pop in python?

remove:
remove removes the first matching value, not a specific index:

del:
del removes the item at a specific index:


pop:
pop removes the item at a specific index and returns it.


and also their error modes are different too;

