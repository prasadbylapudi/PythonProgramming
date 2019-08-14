#The frozen sets are the immutable form of the normal sets, i.e., the items of the frozen set can not be changed and therefore it can be used as a key in dictionary.
#fronzen set is a immutable
#fronzen set is used as key in dictionary
#we can not perform the add(),remove(),pop() on this frozenset
Frozenset = frozenset([1,2,3,4,5])   
print(type(Frozenset))  
print("\nprinting the content of frozen set...")  
for i in Frozenset:  
    print(i);  
Frozenset.add(6) #gives an error since we cannot change the content of Frozenset after creation   
