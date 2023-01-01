import Shape

class GameBoard:        
    def reset_board(self):
        self.width = 9
        self.height = 9
        self.center_width = 5
        self.center_height = 5
        # Create a 2D array of width x height
        self.board = [[0 for x in range(self.width)] for y in range(self.height)]
        # set all values to outside
        for y in range(self.height):
            for x in range(self.width):
                self.board[y][x] = "outside"
        # set the center cells to empty to indicate they are available
        self.startx = (int)((self.width - self.center_width)/2)
        self.starty = (int)((self.height - self.center_height)/2)
        for x in range(self.startx, self.startx + self.center_width):
            for y in range(self.starty, self.starty + self.center_height):
                self.board[y][x] = "empty"

    def __init__(self):
        self.reset_board()
    
    def print_board(self):
        print('*********************************')
        for y in range(self.height):
            for x in range(self.width):
                print(self.board[y][x].center(10), end=" ")
            print()
        print('*********************************')
    def place_shape(self, shape, x, y):
        working_board = [[0 for x1 in range(self.width)] for y1 in range(self.height)]
        for tx in range(self.width):
            for ty in range(self.height):
                working_board[tx][ty] = self.board[tx][ty]
        try:
            for shape_y in range(shape.height):
                for shape_x in range(shape.width):
                    if shape.shape[shape_y][shape_x] == 1:
                        if working_board[y + shape_y][x + shape_x] == "empty":
                            working_board[y + shape_y][x + shape_x] = shape.get_name()
                        else:
                            return False
        except IndexError:
            return False
        self.board = working_board
        return True
