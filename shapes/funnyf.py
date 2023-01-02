import sys
from shapes.Shape import Shape

FUNNYF = Shape("FUNNYF", [[0, 1, 1], [1, 1, 0], [0, 1, 0]])

# Test code
if __name__ == "__main__":
    if(FUNNYF.get_name() == "FUNNYF"):
        print("Name is correct")
    else:
        print("Name is incorrect")        
        sys.exit(1)
    if(FUNNYF.width == 3):
        print("Width is correct")
    else:
        print("Width is incorrect")
        sys.exit(1)
    if(FUNNYF.height == 3):
        print("Height is correct")
    else:
        print("Height is incorrect")
        sys.exit(1)
    if (FUNNYF.shape == [[0, 1, 1], [1, 1, 0], [0, 1, 0]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        sys.exit(1)
    FUNNYF.rotate(90)
    if (FUNNYF.shape == [[0, 1, 0], [1, 1, 1], [0, 0, 1]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        FUNNYF.print_shape()
        sys.exit(1)
    FUNNYF.rotate(180)
    if (FUNNYF.shape == [[0, 1, 0], [0, 1, 1], [1, 1, 0]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        FUNNYF.print_shape()
        sys.exit(1)
    FUNNYF.rotate(270)
    if (FUNNYF.shape == [[1, 0, 0], [1, 1, 1], [0, 1, 0]]):
        print("Shape is correct")
    else:
        print("Shape is incorrect")
        FUNNYF.print_shape()
        sys.exit(1)
