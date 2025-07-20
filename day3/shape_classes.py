import math

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

def action(shape):
    while True:
      choice = int(input("\nWhat action do you want to perform\n1)Area\n2)Perimeter\n"))
      if choice == 1:
          return shape.area()
      elif choice == 2:
          return shape.perimeter()
      enchoice = int(input("\n1) Want to continue\n2) End\n\nEnter your choice\n"))
      if enchoice == 1:
          continue
      elif enchoice == 2:
          break

def main():
  while True:
    choice = int(input("\nWhat shape do you want to perform actions on\n1)Circle\n2)Rectangle\n3)square\n\n"))
    if choice == 1:
      radius = float(input("please enter the radius : "))
      print(action(Circle(radius)))
    elif choice == 2:
      length = float(input("Enter the length : "))
      breadth = float(input("Enter the breadth : "))
      print(action(Rectangle(length,breadth)))
    elif choice == 3:
      side = float(input("Enter the length of a side : "))
      print(action(Square(side)))
    else:
        return "Enter a valid choice"
    enchoice = int(input("\n1) Want to continue\n2) End\n\nEnter your choice"))
    if enchoice == 1:
        continue
    elif enchoice == 2:
        break
if __name__ == "__main__":
  main()
        