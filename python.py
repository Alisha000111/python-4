def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hiii, Alisha")
greet("Alishay")
try:
    num = int(input("Enter number"))
    print(f"Your entered: {num}")
except ValueError:
    print("Not a number")
    import math
from datetime import datetime
print(math.sqrt(3))  
print(datetime.now().strftime("%d-%m-%Y")) 