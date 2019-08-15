def fun(name1,message,name2):
    print("printing the message with",name1,message,name2);

fun("john",message="hello",name2="david");

"""
The python allows us to provide the mix of the required arguments and keyword arguments at the time of function call. However, the required argument must not be given after the keyword argument, i.e.,
once the keyword argument is encountered in the function call, the following arguments must also be the keyword arguments.
"""
