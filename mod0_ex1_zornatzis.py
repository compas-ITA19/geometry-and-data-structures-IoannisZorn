# ==============================================================================
## Assignment 1
# ==============================================================================

__author__ = "Ioannis Zornatzis"
__email__ = "johnz@student.ethz.ch"
__date__ = "15.10.2019"

#Task 1 ----------------------------------------------------------------------------------------------------
#Write a function that returns True if the rotation from AB onto AC is counter-clockwise (ccw).
#A, B, C are points in the xy-plane...
#define funvtion name
#def is_ccw(a,b,c):

#define vectors from points in 2D

def vector_from_two_points_xy(pt_a, pt_b):
    return (pt_b[0] - pt_a[0], pt_b[1] - pt_a[1])

#define cross product of vectors in 3D
#def is_ccw(a, b):
 # c = [a[1]*b[2] - a[2]*b[1],
  #       a[2]*b[0] - a[0]*b[2],
   #      a[0]*b[1] - a[1]*b[0]]
  #return c

#define cross product of vectors in "2D" as a list
#def is_ccw(a, b):
  #c = [a[1]*0 - 0*b[1],
   #      0*b[0] - a[0]*0,
    #     a[0]*b[1] - a[1]*b[0]]
  #return c

#define cross product of vectors in "2D" as a single value
def is_ccw(a, b):
  c = a[0]*b[1] - a[1]*b[0]
  if c>0:
    return True
  else:
    return False
  #return c

#Task 2 ----------------------------------------------------------------------------------------------------
#Read points from the points.txt text file in this folder. Each line contains a tuple with three 2D points. Each point is a tuple of 2 floats (x,y), e.g. ((1895.0943, 2291.517), (589.296, 207.324), (1360.998, 1611.965)).
#Calculate and print out is_ccw for each tuple of points.
#data containers - open file
#with open('filepath', 'points') as f:
#f.readlines()

with open(r"C:\Users\Inspiron\Desktop\064-0025-19L\ITA19-master-new\modules\module0\points.txt",'r') as f:
    for lines in f:
        lines_ev = eval(lines)
        #print(type(lines))

        point_A, point_B, point_C = lines_ev
        #print(point_A)
        #print(lines_ev)

        AB = vector_from_two_points_xy(point_A, point_B)
        #print(AB)

        BC = vector_from_two_points_xy(point_B, point_C)
        #print(BC)

        print(is_ccw(AB,BC))
  
# Extra brownie points cookie
#Given a point P and a normal that span a plane in 3D space, return an arbitrary 
# vector that rests within that plane.
"check it later"