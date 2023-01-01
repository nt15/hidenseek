import sys
from shapes.Shape import Shape

U = Shape("U", [[1, 0, 1], [1, 1, 1]])

# write unit tests
if __name__ == "__main__":
    if(U.get_name() == "U"):
        print("Name is correct")
    else:
        print("Name is incorrect")        
        sys.exit(1)
    if(U.width == 3):
        print("Width is correct")
    else:
        print("Width is incorrect")
        sys.exit(1)
    if(U.height == 2):
        print("Height is correct")
    else:
        print("Height is incorrect")
        sys.exit(1)
    if (U.shape == [[1, 0, 1], [1, 1, 1]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        sys.exit(1)
    U.rotate(90)
    if (U.shape == [[1, 1], [1, 0], [1, 1]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        U.print_shape()
        sys.exit(1)
    U.rotate(180)
    if (U.shape == [[1, 1, 1], [1, 0, 1]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        U.print_shape()
        sys.exit(1)
    U.rotate(270)
    if (U.shape == [[1, 1], [0, 1], [1, 1]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        U.print_shape()
        sys.exit(1)