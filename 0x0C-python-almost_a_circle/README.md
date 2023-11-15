Task 0: If it's not tested it doesn't work

Ensure that all your files, classes, and methods are unit tested.
Validate your code using PEP 8 standards.
Run your tests using python3 -m unittest discover tests.
Task 1: Base class

Create a class named Base.
Implement a constructor with an optional id argument. If id is provided, assign it to the instance's id attribute; otherwise, increment the class's private attribute __nb_objects and assign it to the instance's id attribute.
Task 2: First Rectangle

Create a class Rectangle that inherits from Base.
Implement private instance attributes: __width, __height, __x, __y.
Implement a constructor for Rectangle that initializes its attributes.
Add validation for attributes, such as checking for negative values.
Why use private attributes with getters/setters? To protect attributes and validate values.
Task 3: Validate attributes

Update the Rectangle class to add validation for all setter methods and instantiation.
Raise appropriate exceptions if the input is not an integer or if width or height is less than or equal to 0, or if x or y is less than 0.
Task 4: Area first

Add a public method area to the Rectangle class that calculates and returns the area of the rectangle.
Task 5: Display #0

Add a public method display to the Rectangle class that prints the rectangle using # characters.
Task 6: __str__

Override the __str__ method in the Rectangle class to return a string representation of the object as [Rectangle] (<id>) <x>/<y> - <width>/<height>.
Task 7: Display #1

Update the display method to include x and y offsets.
Task 8: Update #0

Add a public method update to the Rectangle class that assigns attributes in the order: id, width, height, x, y.
Task 9: Update #1

Update the update method to accept keyword arguments and use **kwargs. The order of arguments doesn't matter.
Task 10: Square size

Add a getter and setter for the size attribute in the Square class.
Task 11: Square update

Add a update method to the Square class that accepts arguments in the order: id, size, x, and y.
Task 12: Dictionary to JSON string

Add a static method to_json_string to the Base class that returns the JSON string representation of a list of dictionaries.
Task 13: JSON string to file

Add a class method save_to_file to the Base class that writes the JSON string representation of a list of instances to a file.
Task 14: JSON string to dictionary

Add a static method from_json_string to the Base class that returns a list of dictionaries from a JSON string.
Task 15: Dictionary to Instance

Add a class method create to the Base class that creates an instance from a dictionary.
Task 16: File to instances

Add a class method load_from_file to the Base class that loads a list of instances from a JSON file.
These tasks are part of an assignment where you're building a framework for managing shapes. Each task adds functionality and improvements to the base classes and their subclasses, Rectangle and Square. The goal is to create well-structured and tested code that can be used as a foundation for more complex shape management.
