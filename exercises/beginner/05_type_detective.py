"""
Exercise 5: Type Detective (Difficulty: 5/5)
Topic: Variables & Data Types
Level: Beginner
=====================================================

Description:
  You are given a list of mystery values below. Without changing them, write code to:

    1. Print the type of each value
    2. Print whether each value is truthy or falsy using bool()
    3. Try to convert each value to an integer using int()
       - If conversion succeeds, print the integer
       - If it fails (ValueError), print: "Cannot convert '<value>' to int"

  Mystery values:
    a = "100"
    b = 3.7
    c = ""
    d = 0
    e = "hello"

Expected output:
    100 is type <class 'str'> | truthy: True  | int: 100
    3.7 is type <class 'float'> | truthy: True  | int: 3
    '' is type <class 'str'> | truthy: False | int: Cannot convert '' to int
    0 is type <class 'int'> | truthy: False | int: 0
    hello is type <class 'str'> | truthy: True  | int: Cannot convert 'hello' to int

Hint:
  - Use a try/except block to handle conversion errors:
      try:
          result = int(value)
      except ValueError:
          result = f"Cannot convert '{value}' to int"
"""

a = "100"
b = 3.7
c = ""
d = 0
e = "hello"

values = [a, b, c, d, e]

# ✏️ Write your code below this line
# Tip: loop over `values` and handle each one


# 💡 When done, run this file:  python exercises/beginner/05_type_detective.py


# ✅ SOLUTION
# for v in values:
#     try:
#         as_int = int(v)
#     except (ValueError, TypeError):
#         as_int = f"Cannot convert '{v}' to int"
#
#     print(f"{repr(v)} is type {type(v)} | truthy: {bool(v)!s:<5} | int: {as_int}")
