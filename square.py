class Square:
    def __init__(self, square_side:float):
        self.square_side = square_side
    
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        Args:
            No
        Returns:
            bool: This method checks if the square is valid.
        """
        return self.square_side > 0
    
    def area(self) -> float:
        """
        This method finds the area of the square.
        Args:
            No
        Returns:
            float or int: return area of the square if the square is valid, 0 otherwise
        """
        if self.is_valid():
            return self.square_side ** 2
        else:
            return 0
    
    def perimeter(self) -> float:
        """
        This method finds the perimeter of the square.
        Args:
            No
        Returns:
            float: return perimeter of the square if the square is valid, 0 otherwise
        """
        if self.is_valid():
            return self.square_side * 4
        else:
            return 0


s = Square(5)
print(s.area())
print(s.perimeter())
print(s.is_valid())
