#! /usr/env/python3

#pythagoras
A = int(input("Value of edge A: "))
B = int(input("Value of edge B: "))
C = int(input("Value of edge C: "))
print(62 * "+")

tri = [A, B, C]
tri = sorted(tri)
print("Edges of your triangle are: ", tri)


if tri[2] < tri[0] + tri[1]:
  print("Yes, it is a triangle.")
else:
  print("This is impossible to construct, please choose other values.")


if (tri[0]) ** 2 + (tri[1]) ** 2 == (tri[2]) ** 2:
  print("This is a pythagorean triangle.")
if (tri[0])/3 == (tri[1])/4 == (tri[2])/5:
  print("This is also an Egyptian triangle.")
