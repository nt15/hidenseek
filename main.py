from GameBoard import GameBoard
from shapes.t import T
from shapes.u import U
from shapes.fatl import FATL
from shapes.funnyf import FUNNYF
import copy
import time
from uihandler import uihandler

def get_all_possible_placements():
    game = GameBoard()
    shapes = [T, U, FATL, FUNNYF]
    print("Starting board")
    game.print_board()
    # First find all possible placements for each shape including rotation
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
                        shape_placement[shape.get_name()].append((shape1x, shape1y, rotation, shape))
                        pass
    
    placed_gameboards = []
    print ("Finding all possible solutions")
    
    # time the process
    start_time = time.time()

    # Now try to place all shapes in all possible combinations
    # This is a brute force approach and will take a while
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
    print (f"Time to find solutions: {time.time() - start_time}")
    return placed_gameboards

if __name__ == "__main__":
    placed_gameboards = get_all_possible_placements()
    uihandler1 = uihandler(placed_gameboards)
    uihandler1.main()
