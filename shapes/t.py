import sys
from shapes.Shape import Shape

T = Shape("T", [[1, 1, 1], [0, 1, 0], [0, 1, 0]])

# write unit tests

if __name__ == "__main__":
    if(T.get_name() == "T"):
        print("Name is correct")
    else:
        print("Name is incorrect")        
        sys.exit(1)
    if(T.width == 3):
        print("Width is correct")
    else:
        print("Width is incorrect")
        sys.exit(1)
    if(T.height == 3):
        print("Height is correct")
    else:
        print("Height is incorrect")
        sys.exit(1)
    if (T.shape == [[1, 1, 1], [0, 1, 0], [0, 1, 0]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        sys.exit(1)
    T.rotate(90)
    if (T.shape == [[0, 0, 1], [1, 1, 1], [0, 0, 1]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        T.print_shape()
        sys.exit(1)
    T.rotate(180)
    if (T.shape == [[0, 1, 0], [0, 1, 0], [1, 1, 1]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        T.print_shape()
        sys.exit(1)
    T.rotate(270)
    if (T.shape == [[1, 0, 0], [1, 1, 1], [1, 0, 0]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        T.print_shape()
        sys.exit(1)
    T.flip()
    if (T.shape == [[1, 1, 1], [0, 1, 0], [0, 1, 0]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        T.print_shape()
        sys.exit(1)

