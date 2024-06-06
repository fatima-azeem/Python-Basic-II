r = int(input("Enter the radius of the cylinder: "))
h = int(input("Enter the height of the cylinder: "))
s = int(input("Enter the side of the cube: "))
rd = float(input("Enter the radius of the sphere: "))

cylinder = 3.14 * r * r * h
cube = s * s * s
sphere = 4/3 * 3.14 * rd * rd * rd

print(f"The volume of the cylinder is {cylinder}")
print(f"The volume of the cube is {cube}")
print(f"The volume of the sphere is {sphere}")