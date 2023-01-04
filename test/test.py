import itertools
import copy
import time

class shape:
    def __init__(self, name):
        self.operations = 0
        self.degrees = 0
    
    def rotate(self, degrees):
        self.operations += 1
        self.degrees = degrees

class gameboard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shapes = []
        
    def add_shape(self, shape, x, y):
        time.sleep(0.01) # Simulate a long operation
        self.shapes.append(shape)

    
list_of_list = []
shape1 = shape("a")
shape2 = shape("b")
shape3 = shape("c")
list_of_shapes = [shape1, shape2, shape3]

# just some randome cordinates
list_of_list.append([(2, 3), (4, 5), (6, 7), (8, 9)])
list_of_list.append([(1, 3), (5, 5), (8, 7), (3, 9)])
list_of_list.append([(1, 3), (2, 5), (3, 7), (5, 3)])

start_time = time.time()

for coordinates in list_of_list[0]:
    gameboard1 = gameboard(10, 10)
    gameboard1.add_shape(shape1, coordinates[0], coordinates[1])
    for coordinates in list_of_list[1]:            
        gameboard2 = copy.deepcopy(gameboard1)
        gameboard2.add_shape(shape2, coordinates[0], coordinates[1])
        for coordinates in list_of_list[2]:
            gameboard3 = copy.deepcopy(gameboard2)
            gameboard3.add_shape(shape3, coordinates[0], coordinates[1])
print(f"Time taken: {time.time() - start_time}")

start_time = time.time()
coordinates = itertools.product(*list_of_list)
for experiment in coordinates:
    gameboard1 = gameboard(10, 10)
    fail = False
    for i in range(3):
        gameboard1.add_shape(list_of_shapes[i], experiment[i][0], experiment[i][1])

print(f"Time taken: {time.time() - start_time}")