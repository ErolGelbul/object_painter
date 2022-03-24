class Rectangle:

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:

    def __init__(self, x, y, edge, color):
        self.color = color
        self.x = x
        self.y = y
        self.edge = edge

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.edge, self.y: self.y + self.edge] = self.color
