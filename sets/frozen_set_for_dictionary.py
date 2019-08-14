#The frozen sets are the immutable form of the normal sets, i.e., the items of the frozen set can not be changed and therefore it can be used as a key in dictionary.
#fronzen set is a immutable
#fronzen set is used as key in dictionary
#we can not perform the add(),remove(),pop() on this frozenset
Dictionary = {"Name":"John", "Country":"USA", "ID":101}   
print(type(Dictionary))  
Frozenset = frozenset(Dictionary); #Frozenset will contain the keys of the dictionary  
print(type(Frozenset))  
for i in Frozenset:   
    print(i)  
