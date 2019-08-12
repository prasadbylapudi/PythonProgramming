#usint the else statement with the for loop
"""
Using else statement with for loop
Unlike other languages like C, C++, or Java, python allows us to
use the else statement with the for loop which can be executed only when all the iterations are exhausted.
Here, we must notice that if the loop contains any of the break statement then the else statement will not be executed.
"""
for i in range(0,5):
    print(i);
    if(i==3):
        break;
    
else:
    print("for loop is completelry executed,since there is no  break");
