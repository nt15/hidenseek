from GameBoard import GameBoard
from shapes.Shape import Shape
from shapes.t import T
from shapes.u import U
from shapes.fatl import FATL
from shapes.funnyf import FUNNYF
import copy
import itertools

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
                    game.reset_board()
                    shape.rotate(rotation)
                    if game.place_shape(shape, shape1x, shape1y):
                        shape_placement[shape.get_name()].append((shape1x, shape1y, rotation))
                        pass
    
    for shape in shape_placement:
        print(f"Found {len(shape_placement[shape])} possible for shape {shape}" )
        for placement in shape_placement[shape]:
            print(f"Shape {shape} at {placement[0]}, {placement[1]} rotated {placement[2]}")
    
    placed_gameboards = []
                
    for T_placement in shape_placement["T"]:
        game.reset_board()
        T.rotate(T_placement[2])
        if not game.place_shape(T, T_placement[0], T_placement[1]):
            throw("T placement failed")
        for U_placement in shape_placement["U"]:
            U.rotate(U_placement[2])
            if game.place_shape(U, U_placement[0], U_placement[1]):
                for FATL_placement in shape_placement["FATL"]:
                    FATL.rotate(FATL_placement[2])
                    if game.place_shape(FATL, FATL_placement[0], FATL_placement[1]):
                        for FUNNYF_placement in shape_placement["FUNNYF"]:
                            FUNNYF.rotate(FUNNYF_placement[2])
                            if game.place_shape(FUNNYF, FUNNYF_placement[0], FUNNYF_placement[1]):
                                placed_game = copy.deepcopy(game)
                                placed_gameboards.append(placed_game)
                                print("Found a solution")
                                game.print_board()
                                print()                       
    
    print (f"Found {len(placed_gameboards)} solutions")

    # combinations = itertools.combinations(shapes, 3)
    # for combination in combinations:
    #     for shape in combination:
    #         print(shape.get_name(), end=" ")
    #     print()
    
    # combinations = itertools.combinations(shapes, 3)
    # for combination in combinations:
    #     shape1 = combination[0]
    #     shape2 = combination[1]
    #     shape3 = combination[2]
    #     for shape1_placement in shape_placement[shape1.get_name()]:
    #         game.reset_board()
    #         shape1.rotate(shape1_placement[2])
    #         if game.place_shape(shape1, shape1_placement[0], shape1_placement[1]):
    #             for shape2_placement in shape_placement[shape2.get_name()]:
    #                 shape2.rotate(shape2_placement[2])
    #                 if game.place_shape(shape2, shape2_placement[0], shape2_placement[1]):
    #                     for shape3_placement in shape_placement[shape3.get_name()]:
    #                         shape3.rotate(shape3_placement[2])
    #                         if game.place_shape(shape3, shape3_placement[0], shape3_placement[1]):
    #                             placed_game = copy.deepcopy(game)
    #                             placed_gameboards.append(placed_game)
    #                             print("Found a solution")
    #                             game.print_board()
    #                             print()                                
    # print (f"Found {len(placed_gameboards)} solutions")    
    # get string from user end with blank line
    animals_desired = []
    while True:
        user_input = input("Enter a string: ")
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
    
                                
