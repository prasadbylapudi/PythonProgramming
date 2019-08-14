Months = set(["January","February", "March", "April", "May", "June"])  
print("\nprinting the original set ... ")  
print(Months)  
print("\nRemoving items through discard() method...");  
Months.discard("Feb"); #will not give an error although the key feb is not available in the set  
print("\nprinting the modified set...")  
print(Months)  
print("\nRemoving items through remove() method...");  
Months.remove("Jan") #will give an error as the key jan is not available in the set.   
print("\nPrinting the modified set...")  
print(Months)  


#difference between the remove and discard
#If the key to be deleted from the set using discard() doesn't exist in the set, the python will not give the error
#On the other hand, if the item to be deleted from the set using remove() doesn't exist in the set, the python will give the error.

