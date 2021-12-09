class Circle:
    def __init__(self, radius = 1.0, color = "red") -> None:
        self.__radius = radius
        self.__color = color
    
    def getRadius(self) -> float:
        return self.__radius

    def setRadius(self, radius) -> None:
        self.__radius = radius
    
    def getColor(self) -> str:
        return self.__color

    def setColor(self, color) -> None:
        self.__color = color
    
    def toString(self) -> str:
        return f"Radius: {self.getRadius()}" + "\n" + f"Color: {self.getColor()}"

    def getArea(self) -> float:
        return ((22/7)*(self.getRadius()**2))
    
    
    
class Cylinder(Circle):
    def __init__(self, radius=1, color="red", height : float = 1) -> None:
        super().__init__(radius=radius, color=color)
        self.__height = height
    
    def getHeight(self) -> float:
        return self.__height

    def setHeight(self, height) -> None:
        self.__height = height

    def toString(self) -> str:
        return f"Height: {self.getHeight()}"
    
    def getVolume(self):
        return (22/7)*((self.getRadius())**2)* self.getHeight()

