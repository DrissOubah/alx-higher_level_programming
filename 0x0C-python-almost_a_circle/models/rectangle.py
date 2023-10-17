#!/usr/bin/python3
from .base import Base


class Rectangle(Base):
    """
    Rectangle class representing a rectangle
    with width, height, x, and y attributes.

    Attributes:
        id (int): The unique ID of the rectangle.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.

    Args:
        id (int, optional): The ID of the rectangle.
                            If not provided, a unique ID is generated.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int, optional): The x-coordinate of the rectangle. Default is 0.
        y (int, optional): The y-coordinate of the rectangle. Default is 0.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            id (int, optional): The ID of the rectangle.
                                If not provided, a unique ID is generated.
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle. Default is 0.
            y (int, optional): The y-coordinate of the rectangle. Default is 0.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Getter for width
    @property
    def width(self):
        return self.__width

    # Setter for width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter for height
    @property
    def height(self):
        return self.__height

    # Setter for height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # Getter for x
    @property
    def x(self):
        return self.__x

    # Setter for x
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Getter for y
    @property
    def y(self):
        return self.__y

    # Setter for y
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print()
            return

        for _ in range(self.y):
            print()

        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        Update the Rectangle attributes.

        Args:
            *args (int): New attribute values in the following order:
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.

        """
        attribute_names = ["id", "width", "height", "x", "y"]

        for i, arg in enumerate(args):
            if i < len(attribute_names) and arg is not None:
                setattr(self, attribute_names[i], arg)

        for key, value in kwargs.items():
            if key in attribute_names and value is not None:
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )
