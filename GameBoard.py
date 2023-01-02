import shapes.Shape as Shape
import copy
from shapes.t import T
from shapes.u import U
from shapes.fatl import FATL
from shapes.funnyf import FUNNYF
import sys


class GameBoard:        
    def reset_board(self):
        self.width = 9
        self.height = 9
        self.center_width = 5
        self.center_height = 5
        # Create a 2D array of width x height
        self.board = [["outside" for x in range(self.width)] for y in range(self.height)]
        # set all values to outside

        # set the center cells to empty to indicate they are available
        self.startx = (int)((self.width - self.center_width)/2)
        self.starty = (int)((self.height - self.center_height)/2)
        for x in range(self.startx, self.startx + self.center_width):
            for y in range(self.starty, self.starty + self.center_height):
                self.board[y][x] = "empty"
        self.animal_placement = [[0 for x in range(self.width)] for y in range(self.height)]
        self.animal_placement[2][2] = "bat"
        self.animal_placement[2][3] = "fox"
        self.animal_placement[2][4] = "fox"
        self.animal_placement[2][5] = "empty"
        self.animal_placement[2][6] = "bat"
        self.animal_placement[3][2] = "monkey"
        self.animal_placement[3][3] = "jaguar"
        self.animal_placement[3][4] = "tapir"
        self.animal_placement[3][5] = "bat"
        self.animal_placement[3][6] = "fox"
        self.animal_placement[4][2] = "jaguar"
        self.animal_placement[4][3] = "empty"
        self.animal_placement[4][4] = "bear"
        self.animal_placement[4][5] = "jaguar"
        self.animal_placement[4][6] = "empty"
        self.animal_placement[5][2] = "empty"
        self.animal_placement[5][3] = "tapir"
        self.animal_placement[5][4] = "fox"
        self.animal_placement[5][5] = "monkey"
        self.animal_placement[5][6] = "tapir"
        self.animal_placement[6][2] = "fox"
        self.animal_placement[6][3] = "bat"
        self.animal_placement[6][4] = "empty"
        self.animal_placement[6][5] = "empty"
        self.animal_placement[6][6] = "jaguar"


    def __init__(self):
        self.reset_board()
    
    def place_shape(self, shape, x, y):
        working_board = [[0 for x1 in range(self.width)] for y1 in range(self.height)]
        working_board = copy.deepcopy(self.board)
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
        self.board = copy.deepcopy(working_board)
        return True

    def get_animals_left(self):
        animals_left = []
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == "outside":
                    pass
                elif self.board[y][x] == "empty":
                    if self.animal_placement[y][x] != "empty":
                        animals_left.append(self.animal_placement[y][x])
                else:
                    pass
        animals_left.sort()
        return animals_left
    
    def print_board(self):
        print('*********************************')
        animals_left = []
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == "outside":
                    pass
                elif self.board[y][x] == "empty":
                    print(self.animal_placement[y][x].center(10), end=" ")
                    if self.animal_placement[y][x] != "empty":
                        animals_left.append(self.animal_placement[y][x])
                else:
                    print(self.board[y][x].center(10), end=" ")
            print()
        print('*********************************')
        print('Animals left: ', animals_left)



# Test code
if __name__ == '__main__':
    game_board = GameBoard()
    game_board.print_board()
    T.rotate(180)
    if not game_board.place_shape(T, 4, 4):
        print("Could not place shape")
        game_board.print_board()
        sys.exit(1)
    U.rotate(90)
    if not game_board.place_shape(U, 2, 4):
        print("Could not place shape")
        game_board.print_board()
        sys.exit(1)
    FATL.rotate(180)
    if not game_board.place_shape(FATL, 5, 2):
        print("Could not place shape")
        game_board.print_board()
        sys.exit(1)
    FUNNYF.rotate(90)
    if not game_board.place_shape(FUNNYF, 2, 2):
        print("Could not place shape")
        game_board.print_board()
        sys.exit(1)
    print("Success")
    game_board.print_board()