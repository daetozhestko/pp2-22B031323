class Shape:
    def __init__(self):
        self.area=0
    def get_area(self):
        return self.area
class Square(Shape):
    def __init__(self,length):
        self.length=length
        self.area=self.length**2
a=Square(int(input()))
print(Shape.get_area(a))