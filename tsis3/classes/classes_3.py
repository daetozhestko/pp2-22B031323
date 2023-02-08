class Shape:
    def __init__(self):
        self.area=0
    def get_area(self):
        return self.area
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.area=self.length*self.width
a=int(input())
b=int(input())
x = Rectangle(a, b)
print(Shape.get_area(x))