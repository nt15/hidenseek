import copy

class Shape:
    def __init__(self, name, l):
        self.shape = l
        self.original_shape = copy.deepcopy(l)
        self.width = len(self.shape[0])
        self.height = len(self.shape)
        self.name = name
    
    def reset(self):
        self.shape = copy.deepcopy(self.original_shape)
        self.width = len(self.shape[0])
        self.height = len(self.shape)

    def rotateby90(self):
        tuple = zip(*self.shape[::-1])
        self.shape = [list(row) for row in tuple]
    
    def rotate(self, degrees):
        if degrees == 0:
            pass
        elif degrees == 90:
            self.rotateby90()
        elif degrees == 180:
            self.rotateby90()
            self.rotateby90()
        elif degrees == 270:
            self.rotateby90()
            self.rotateby90()
            self.rotateby90()
        else:
            print("Invalid degrees")
        self.width = len(self.shape[0])
        self.height = len(self.shape)
    
    def print_shape(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.shape[y][x], end=" ")
            print()
    
    def get_name(self):
        return self.name