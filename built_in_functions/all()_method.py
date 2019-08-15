"""
The python all() function accepts an iterable object (such as list, dictionary, etc.). It returns true if all items in passed iterable are true. Otherwise, it returns False.
If the iterable object is empty, the all() function returns True.
"""
# all values true  
k = [1, 3, 4, 6]  
print(all(k))  
  
# all values false  
k = [0, False]  
print(all(k))  
  
# one false value  
k = [1, 3, 7, 0]  
print(all(k))  
  
# one true value  
k = [0, False, 5]  
print(all(k))  
  
# empty iterable  
k = []  
print(all(k)) 
