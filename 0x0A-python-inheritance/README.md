Task 0 (Lookup):

Write a function lookup(obj) to get attributes and methods of an object.
Return a list of attributes and methods.
No module imports allowed.
Task 1 (My list):

Create a class MyList that inherits from list.
Add a print_sorted method to print the list in ascending order.
Elements are assumed to be integers.
Task 2 (Exact same object):

Write a function is_same_class(obj, a_class) to check if an object is an instance of a specific class.
Return True if the object is an instance; otherwise, return False.
No module imports allowed.
Task 3 (Same class or inherit from):

Create a function is_kind_of_class(obj, a_class) to check if an object is an instance of or inherits from a class.
Return True if the object is an instance or inherits; otherwise, return False.
No module imports allowed.
Task 4 (Only sub class of):

Implement a function inherits_from(obj, a_class) to check if an object is an instance of a class inherited (directly or indirectly) from the specified class.
Return True if it inherits; otherwise, return False.
No module imports allowed.
Task 5 (Geometry module):

Create an empty class BaseGeometry.
No module imports allowed.
Task 6 (Improve Geometry):

Enhance BaseGeometry class with an area method raising an exception.
The exception message is "area() is not implemented."
No module imports allowed.
Task 7 (Integer validator):

Extend BaseGeometry class with an integer_validator method.
Validate if a value is an integer and greater than 0.
Raise appropriate exceptions for invalid values.
No module imports allowed.
Task 8 (Rectangle):

Create a class Rectangle inheriting from BaseGeometry.
Initialize width and height with private attributes.
Validate them with integer_validator.
Task 9 (Full rectangle):

Extend Rectangle class by implementing the area method.
Add a custom __str__ method for the rectangle's description.
Task 10 (Square #1):

Create a class Square that inherits from Rectangle.
Initialize size as a private attribute and validate it.
Task 11 (Square #2):

Extend Square class to provide a custom __str__ method for square description.
The description format is "[Square] <width>/<height>".
