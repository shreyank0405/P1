1️⃣ Variable in Python

A variable is a name used to store a value.

x = 10
name = "Python"


x stores 10

name stores "Python"


--------------------------------------------------------------------------



2️⃣ Scope in Python
Scope means where a variable can be used or accessed in a program.

Python mainly has 4 types of scope (LEGB Rule):
🔹 L – Local Scope
Variables created inside a function
def my_func():
    a = 5   # local variable
    print(a)

my_func()
# print(a) ❌ Error (a is not accessible outside)


🔹 E – Enclosing Scope
Variables in a function inside another function
def outer():
    x = 10   # enclosing variable

    def inner():
        print(x)

    inner()

outer()


🔹 G – Global Scope
Variables created outside all functions
x = 20   # global variable

def show():
    print(x)

show()


🔹 B – Built-in Scope
Predefined names in Python
print(len("Python"))  # len is built-in


----------------------------------------------------------------------



🔹 Types of Control Statements
1️⃣ Conditional (Decision) Statements

Used to make decisions.

✅ if
x = 10
if x > 5:
    print("x is greater than 5")

✅ if-else
x = 3
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
---------------------------

✅ if-elif-else
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
--------------------------------------------------------------------

2️⃣ Looping (Iteration) Statements

Used to repeat a block of code.

🔁 for Loop
for i in range(1, 6):
    print(i)
---------------------------


Example – print list elements:

numbers = [1, 2, 3]
for n in numbers:
    print(n)

🔁 while Loop
i = 1
while i <= 5:
    print(i)
    i += 1
-------------------------------------

3️⃣ Loop Control Statements

Used to change loop execution.

🔸 break (stop loop)
for i in range(1, 6):
    if i == 3:
        break
    print(i)

🔸 continue (skip iteration)
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

🔸 pass (do nothing)
for i in range(5):
    pass

-------------------------------------


🔹 1️⃣ Functions in Python

A function is a block of reusable code that performs a specific task.

✔ Why use functions?

Avoid code repetition

Easy to read and maintain

Saves time

🔸 Defining a Function
def add(a, b):
    return a + b

🔸 Calling a Function
result = add(5, 3)
print(result)
---------------------

🔹 Types of Functions
1️⃣ Built-in Functions
print("Hello")
len([1, 2, 3])

2️⃣ User-defined Functions
def greet():
    print("Hello Python")

greet()

🔹 Function with Parameters
def square(x):
    return x * x

print(square(4))

🔹 Function with Default Argument
def greet(name="User"):
    print("Hello", name)

greet()
greet("Shreyank")

🔹 Function with Multiple Return Values
def calc(a, b):
    return a+b, a-b

x, y = calc(10, 5)
print(x, y)

----------------------------------------------------

🔹 2️⃣ Modules in Python

A module is a file that contains functions, variables, and classes.

🔸 Using Built-in Modules
math module
import math
print(math.sqrt(16))

Import specific function
from math import sqrt
print(sqrt(25))

🔸 Creating Your Own Module
Step 1: Create a file mymodule.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

Step 2: Use it in another file
import mymodule

print(mymodule.add(5, 2))
print(mymodule.sub(5, 2))


📘 Difference Between Function and Module
Function	        Module
Single task	        Collection of code
Defined using def	Python file
Reusable block	        Reusable program
