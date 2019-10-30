# ==============================================================================
## Assignment 2
# ==============================================================================

__author__ = "Ioannis Zornatzis"
__email__ = "johnz@student.ethz.ch"
__date__ = "30.10.2019"

# ==============================================================================
##  Geometry
# ==============================================================================

#Task 1: Given two vectors, use the cross product 
#        to create a set of three ortho**normal** vectors.

from compas.geometry import Vector

#define two random vectors
a = Vector(10, 0, 0)
b = Vector(0, 20, 0)

def orthonormal_vectors(u, v):
    x = u.unitized()
    z = u.cross(v).unitized()
    y = z.cross(x)
    return (x, y, z)

vectors = orthonormal_vectors(a, b)
print(vectors)

#Task 2: Use the cross product to compute the area of a convex, 2D polygon.

from compas.geometry import Polygon
from compas_plotters import Plotter
from compas.utilities import pairwise

#define a random convex polygon

points = [[0., 0., 0.], [1.5, -1., 0.], [1., -2., 0.], [-1., -2., 0.], [-1.5, -1., 0.]]
#print (points)
polygon = Polygon(points)

def triangle_area(a, b, c):
   
    return 0.5 * (b - a).cross(c - a).length

def convex_area(polygon):

    # check if the polygon is convex (!) -dummy check
    if not polygon.is_convex():
        raise ValueError("Define a convex polygon")

    pts = polygon.points[:] + [polygon.points[0]]

    # list of triangle areas using the centroid
    centroid = polygon.centroid
    areas = [triangle_area(a, b, centroid) for a, b in pairwise(pts)]

    return sum(areas)

area = convex_area(polygon)
print (area)

#plotter = Plotter(figsize=(8, 5))
#plotter.draw_polygons(polygon)
#plotter.show()
"""this plotter not working atm, check it later"""

#Task 3: Define a function for computing the cross products of two arrays of vectors.
#        The input arrays have the same length (same number of vectors).
""" would be interesting to check for different lengths..."""

from numpy import array
from numpy import cross
from compas.geometry import cross_vectors

# define custom arrays of vectors 

u1 = [1, 0, 0]
u2 = [0, 1, 0]

v1 = [2, 0, 0]
v2 = [0, 2, 0]

a1 = array([u1, u2])
a2 = array([v1, v2])

#print(a1)
#print(a2)

# a. Prototype in pure Python (loop over the arrays).

def cross_python(array1, array2):

    if len(array1) == len(array2):
        return array([cross_vectors(u, v) for u, v in zip(array1, array2)])

    else:
        return None

c_python = cross_python(a1, a2)
#print(c_python)

# b. Make Numpy equivalent without loops.

def cross_numpy(array1, array2):

    if len(array1) == len(array2):
        return cross(array1, array2)
    else:
        return None

c_numpy = cross_numpy(a1, a2)
#print(c_numpy)

## test results (just in case...)

print(c_python == c_numpy) # verify results

# ==============================================================================
## Data structures
# ==============================================================================

#   Create a mesh using `faces.obj`:

import compas
import random
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

#plot mesh
"""
plotter = MeshPlotter(mesh, figsize=(4, 4))
plotter.draw_vertices()
plotter.draw_edges()
plotter.draw_faces()
plotter.show()

"""

#   a. Define a function for traversing the mesh from boundary to boundary in a "straight" line.
"""https://github.com/compas-ITA19/ITA19/blob/master/modules/module0/solutions/Data%20Structures.ipynb"""

def traverse(mesh):

    boundary_vertices = mesh.vertices_on_boundaries()[0]
    start = random.choice(boundary_vertices)
    nbrs = mesh.vertex_neighbors(start)
    path = []
    current = start

    """ 
    plotter = MeshPlotter(mesh, figsize=(4, 4))
    plotter.draw_vertices(
    radius=0.4, text='key', keys=list(mesh.vertices_on_boundary()), facecolor={start: (255, 0, 0)})
    plotter.draw_edges()
    plotter.draw_faces()
    plotter.show()

    """
    #Find the neighbour NOT on the boudnary
    for nbr in nbrs:
        if not mesh.is_vertex_on_boundary(nbr):
            previous, current = current, nbr
            break
    while True:
        path.append(current)
        if mesh.is_vertex_on_boundary(current):
            break
        # Find the neighbours of this vertex in cycling order
        nbrs = mesh.vertex_neighbors(current, ordered=True)
        # Find the opposite neighbour of the previous vertex
        "path: topologically straight line"
        i = nbrs.index(previous)
        previous, current = current, nbrs[i - 2]
    path.append(start)
    print (nbrs)
    return path

#   b. Visualise the result.

path = traverse(mesh)

plotter = MeshPlotter(mesh, figsize=(4, 4))
plotter.draw_vertices(
    radius=0.4, text='key', keys=path, facecolor=(255, 0, 0))
plotter.draw_edges()
plotter.draw_faces()
plotter.show()