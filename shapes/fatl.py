import sys
from shapes.Shape import Shape

FATL = Shape("FATL", [[1, 0], [1, 1], [1, 1]])

# write unit tests

if __name__ == "__main__":
    if (FATL.get_name() == "FATL"):
        print("Name is correct")
    else:
        print("Name is incorrect")
        sys.exit(1)
    if (FATL.width == 2):
        print("Width is correct")
    else:
        print("Width is incorrect")
        sys.exit(1)
    if (FATL.height == 3):
        print("Height is correct")
    else:
        print("Height is incorrect")
        sys.exit(1)
    if (FATL.shape == [[1, 0], [1, 1], [1, 1]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        sys.exit(1)
    FATL.rotate(90)
    if (FATL.shape == [[1, 1, 1], [1, 1, 0]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        FATL.print_shape()
        sys.exit(1) 
    FATL.rotate(180)
    if (FATL.shape == [[1, 1], [1, 1], [0, 1]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        FATL.print_shape()
        sys.exit(1)
    FATL.rotate(270)
    if (FATL.shape == [[0, 1, 1], [1, 1, 1]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        FATL.print_shape()
        sys.exit(1)
    

