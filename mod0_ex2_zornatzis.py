# # Assignment 1

## Geometry

#1. Given two vectors, use the cross product to create a set of three ortho**normal** vectors.

#calc cross product

from compas.geometry import cross_vectors

u = [1.0, 0.0, 0.0]
v = [0.0, 1.0, 0.0]

uxv = cross_vectors(u, v)

#print(uxv)


#2. Use the cross product to compute the area of a convex, 2D polygon.
from compas.geometry import subtract_vectors
from compas.geometry import cross_vectors
from compas.geometry import length_vector
from compas.geometry import area_triangle

a = [0.0, 0.0, 0.0]
b = [1.0, 0.0, 0.0]
c = [0.0, 1.0, 0.0]

ab = subtract_vectors(b, a)
ac = subtract_vectors(c, a)

L = length_vector(cross_vectors(ab, ac))
A = area_triangle([a, b, c])

print(0.5 * L == A)

#3. Define a function for computing the cross products of two arrays of vectors.

#   The input arrays have the same length (same number of vectors).

#   a. Prototype in pure Python (loop over the arrays).

#   b. Make Numpy equivalent without loops.

## Data structures

#4. Using `faces.obj` :

#   a. Define a function for traversing the mesh from boundary to boundary in a "straight" line.
#   b. Visualise the result.

