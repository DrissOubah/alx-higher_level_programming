Add Integer Function:

The function add_integer takes two arguments, a and b, which must be integers or floats. If they are not, a TypeError exception is raised.
If a and b are floats, they are first cast to integers.
The function returns the sum of a and b as an integer.
Matrix Division Function:

The function matrix_divided divides all elements of a matrix by a given divisor div.
The matrix matrix must be a list of lists of integers or floats, and each row of the matrix must have the same size.
The divisor div must be a number (integer or float) and cannot be zero.
The function raises various exceptions for invalid inputs.
The result is a new matrix with elements rounded to 2 decimal places.
Say My Name Function:

The function say_my_name takes two arguments, first_name and last_name, which must be strings.
If either first_name or last_name is not a string, a TypeError exception is raised.
The function prints "My name is <first name> <last name>".
Print Square Function:

The function print_square prints a square made of '#' characters.
The size argument specifies the size of the square, and it must be a non-negative integer.
The function raises exceptions for invalid inputs, including negative size values.
Text Indentation Function:

The function text_indentation takes a string text and prints it with two new lines after '.', '?', and ':' characters.
The function raises a TypeError exception if text is not a string.
It removes spaces at the beginning and end of each printed line.
Max Integer Function with Unittests:

The function max_integer finds the maximum integer in a list of integers.
The provided test cases demonstrate the function's behavior, and it returns the maximum integer.
Matrix Multiplication Functions:

There are two matrix multiplication functions, matrix_mul and lazy_matrix_mul.
They both multiply two matrices and handle various exceptions for invalid inputs.
matrix_mul uses regular Python code, while lazy_matrix_mul uses the NumPy library.
CPython Function for Printing Python Strings:

The function print_python_string is written in C and prints information about Python strings.
It validates the input and prints the type, length, and value of the string object.
If the input is not a valid string, it prints an error message.
These functions cover a range of tasks, from basic integer addition to matrix operations and string handling, and they include input validation and error handling.
