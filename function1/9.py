import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

radius = int(input("Enter your number: "))
sphere_volume = calculate_sphere_volume(radius)
print("The volume of the sphere is:", sphere_volume)

#the value of the radius to power of 3 ( the '**' is like calling pow(...) function in C++ language.