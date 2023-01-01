from GameBoard import GameBoard
from Shape import Shape


if __name__ == "__main__":
    game = GameBoard()
    T = Shape("T", [[1, 1, 1], [0, 1, 0], [0, 1, 0]])
    print("T shape")
    T.print_shape()
    print("T shape rotated 90 degrees")
    T.rotate(90)
    T.print_shape()
    print("T shape rotated 180 degrees")
    T.rotate(90)
    T.print_shape()
    U = Shape("U", [[1, 0, 1], [1, 1, 1]])
    U.print_shape()
    U.rotate(90)
    print("U rotated by 90")
    U.print_shape()
    print("Starting board")
    game.print_board()
    for shape1x in range(game.width):
        for shape1y in range(game.height):
            for rotation in range(4):
                game.reset_board()
                if game.place_shape(T, shape1x, shape1y):
                    #print("Placed T at", shape1x, shape1y)
                    #game.print_board()
                    pass
                T.rotate(90)
    
    

