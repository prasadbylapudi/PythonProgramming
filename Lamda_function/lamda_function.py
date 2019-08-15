"""
Python allows us to not declare the function in the standard manner, i.e.,
by using the def keyword. Rather, the anonymous functions are declared by using lambda keyword. However, Lambda functions can accept any number of arguments, but they can return only one value in the form of expression.

The anonymous function contains a small piece of code.
It simulates inline functions of C and C++, but it is not exactly an inline function.


"""
#syntax is -> lambda arguments a:a+10;
x=lambda a:a+10;
#a is an argument
#a+10 is an expresssion
print(x(90));
