from GameBoard import GameBoard
from shapes.Shape import Shape
from shapes.t import T
from shapes.u import U
from shapes.fatl import FATL
from shapes.funnyf import FUNNYF
import copy

if __name__ == "__main__":
    game = GameBoard()
    shapes = [T, U, FATL, FUNNYF]
    print("Starting board")
    game.print_board()
    # create an empty dictionary to store the shape placements
    shape_placement = {}
    for shape in shapes:
        shape_placement[shape.get_name()] = []
        for shape1x in range(game.width):
            for shape1y in range(game.height):
                for rotation in range(0, 271, 90):
                    shape.reset()
                    game.reset_board()
                    shape.rotate(rotation)
                    if game.place_shape(shape, shape1x, shape1y):
                        shape_placement[shape.get_name()].append((shape1x, shape1y, rotation))
                        pass
    
    placed_gameboards = []
    print ("Finding all possible solutions")
                
    for T_placement in shape_placement["T"]:
        game = GameBoard()
        T.reset()
        T.rotate(T_placement[2])
        print(".", end="")
        if not game.place_shape(T, T_placement[0], T_placement[1]):
            SystemError("T placement failed")
        for U_placement in shape_placement["U"]:
            gameT = copy.deepcopy(game)
            U.reset()
            U.rotate(U_placement[2])
            if gameT.place_shape(U, U_placement[0], U_placement[1]):
                for FATL_placement in shape_placement["FATL"]:
                    gameTU = copy.deepcopy(gameT)
                    FATL.reset()
                    FATL.rotate(FATL_placement[2])
                    if gameTU.place_shape(FATL, FATL_placement[0], FATL_placement[1]):
                        for FUNNYF_placement in shape_placement["FUNNYF"]:
                            gameTUFATL = copy.deepcopy(gameTU)
                            FUNNYF.reset()
                            FUNNYF.rotate(FUNNYF_placement[2])
                            if gameTUFATL.place_shape(FUNNYF, FUNNYF_placement[0], FUNNYF_placement[1]):
                                placed_game = copy.deepcopy(gameTUFATL)
                                placed_gameboards.append(placed_game)
                    
    
    print (f"Found {len(placed_gameboards)} solutions")

    animals_desired = []
    while True:
        user_input = input("Enter animal name (bat, fox, tapir, jaguar, monkey, bear) blank to end: ")
        if user_input == "":
            break
        else:
            animals_desired.append(user_input)

    # sort the animals_desired list
    animals_desired.sort()
    print(animals_desired)
    found = False
    for placed_gameboard in placed_gameboards:
        if placed_gameboard.get_animals_left() == animals_desired:
            placed_gameboard.print_board()
            print()
            found = True
            break
    if not found:
        print("No solution found")
    

    
                                
