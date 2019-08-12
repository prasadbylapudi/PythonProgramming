#Python expandstabs() method replaces all the characters by sepecified spaces. By default a single tab expands to 8 spaces which can be overridden according to the requirement.

#We can pass 1, 2, 4 and more to the method which will replace tab by the these number of space characters.


#tabsize : It is optional and default value is 8.

str1="welcome\t to \t prasad \t bylapudi.";
str2=str1.expandtabs(9);
print(str2);
