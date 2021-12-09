from abc import get_cache_token
from num2 import *

def main():
    bob = Cylinder(3, "purple",10)
    print(f"There is a {bob.getColor()} cylinder named Bob.")
    print(f"Bob's radius is {bob.getRadius()}, and his base's area is {bob.getArea():.2f}")
    print(f"Bob's height is {bob.getHeight()}, and his voulme is {bob.getVolume():.2f}\n")

    answer = str(input("Do you want to change bob? (Y/N): "))

    if answer == "Y":
        col = str(input("Enter bob's new color: "))
        rad = float(input("Enter bob's new radius: "))
        heigh = float(input("Enter bob's new height: "))
        bob.setColor(col)
        bob.setRadius(rad)
        bob.setHeight(heigh)
        print(f"Now bob is {bob.getColor()}, {bob.getRadius()} radius, and {bob.getHeight()} height")
        print(f"His new area is {bob.getArea():.2f}, and his new volume is {bob.getVolume():.2f}")
    elif answer == "N":
        print("Ok, good bye!")
    else: 
        print("It's your fault for not answering with the right letter.")
        print("Run the code again.")
        print("I'm too lazy to loop this code.")

main()