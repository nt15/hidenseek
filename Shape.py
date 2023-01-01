class Shape:
    def __init__(self, name, l):
        self.shape = l
        self.width = len(self.shape[0])
        self.height = len(self.shape)
        self.name = name
    
    def rotate(self, degrees):
        if degrees == 90:
            self.shape = list(zip(*self.shape[::-1]))
        elif degrees == 180:
            self.shape = list(zip(*self.shape[::-1]))
            self.shape = list(zip(*self.shape[::-1]))
        elif degrees == 270:
            self.shape = list(zip(*self.shape[::-1]))
            self.shape = list(zip(*self.shape[::-1]))
            self.shape = list(zip(*self.shape[::-1]))
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