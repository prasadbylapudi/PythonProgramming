class Details:  
    age = 19;
    name = "Prasad"  
  
details = Details()  
print('The age is:', getattr(details, "age")) ; 
print('The age is:', details.age);
#The python getattr() function returns the value of a named attribute of an object. If it is not found, it returns the default value.


