def simple_interest(p,t,r):
    return (p*t*r)/100
p=float(input("enter the principle amount:"));
r=float(input("enter rate of interest"));
t=float(input("enter time in years"));
print(simple_interest(p,t,r));
"""
#the function simple_interest accepts three arguments and returns the simple interest accordingly  
def simple_interest(p,t,r):  
    return (p*t*r)/100  
p = float(input("Enter the principle amount? "))  
r = float(input("Enter the rate of interest? "))  
t = float(input("Enter the time in years? "))  
print("Simple Interest: ",simple_interest(p,t,r))

"""
#take care small letters and capital letters
