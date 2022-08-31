class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def __repr__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.width})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def ger_perimeter(self):
        return  (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return  ((self.width**2 + self.height**2) ** .5)

    def get_picture(self):
        if (self.width >= 50) or (self.height >=50):
            return 'Too big for picture'
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, another_shape):
        max_width = self.width // another_shape.width
        max_height = self.height // another_shape.height
        return (max_width * max_height)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def __repr__(self):
        return f'Square(side={self.width})'

    def set_side(self, new_side):
        self.height = self.width = new_side

    def set_height(self, height):
        super().set_height(height)
        self.width = height
    
    def set_width(self, width):
        super().set_width(width)
        self.height = width