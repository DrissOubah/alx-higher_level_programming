ead file: You need to write a function called read_file that reads the content of a text file and prints it to the console. You should use the with statement to manage the file. You don't need to handle exceptions related to file permissions or non-existent files.

Write to a file: Create a function called write_file that writes a string to a text file and returns the number of characters written. Use the with statement, and if the file doesn't exist, your function should create it.

Append to a file: Implement a function called append_write that appends a string to the end of a text file and returns the number of characters added. If the file doesn't exist, it should be created. Use the with statement.

To JSON string: Create a function called to_json_string that takes an object as input and returns its JSON representation as a string. You should not manage exceptions for objects that can't be serialized.

From JSON string to Object: Write a function called from_json_string that converts a JSON string into a Python data structure (e.g., a dictionary or a list). You don't need to manage exceptions for invalid JSON strings.

Save Object to a file: Implement a function called save_to_json_file that writes an object to a text file using its JSON representation. Use the with statement and don't handle exceptions for unserializable objects.

Create object from a JSON file: Create a function called load_from_json_file that reads a JSON file and converts it back into a Python object. Use the with statement, and don't manage file exceptions.

Class to JSON: Write a function called class_to_json that returns a dictionary representation of an object for JSON serialization. This function should work for objects with attributes like lists, dictionaries, strings, integers, and booleans.

Student to JSON: Define a Student class with attributes first_name, last_name, and age. Implement a to_json method that returns a dictionary representation of a Student instance.

Student to JSON with filter: Extend the Student class by adding a to_json method that can accept a list of attributes to filter the output.

Student to disk and reload: Implement a method in the Student class to save and reload the object to/from a JSON file. This demonstrates serialization and deserialization.

Pascal's Triangle: Create a function called pascal_triangle that generates Pascal's triangle up to the given row n and returns it as a list of lists of integers.
