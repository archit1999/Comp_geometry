Problem:- 
  Given n points in a plane, find the smallest circle that encloses all the points in the plane(either inside or on the circle).
Approach:-
  -The main algorithm is taken from the book Computational Geometry by Mark de berg and 3 others.
  -It's a randomized incremental algorithm, where we basically just shuffle the input points, so as to get all the any of the permuted order with equal probability.
  -Point is a class with x and y co-ordinates as the attributes and the following functions
    - dist between two points
    - squared distance between two points(for comparison porposes)
  -Circle is a class with point object as centre and radius as the attributes, and the functions are as follows
    - Constructor based on two points as input and three points as input.
    - check function to check whether a given point lies inside or outside the circle.
  -RIC algo
    - its an incremental algorithm based on the procedure mentioned in the book.
