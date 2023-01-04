import tkinter
from GameBoard import GameBoard
from shapes.t import T
from shapes.u import U
from shapes.fatl import FATL
from shapes.funnyf import FUNNYF

def solve(labels, images):
    gameboard = GameBoard()
    gameboard.place_shape(T, 2, 2)
    display_gameboard(gameboard, labels, images)

def display_gameboard(gameboard, labels, images):
    content = gameboard.get_contents()
    for y in range(len(content)):
        for x in range(len(content[y])):
            labels[y * gameboard.center_width + x].config(image=images[content[y][x]])

def on_click(event, animal, text_label, number_of_animals):
    if number_of_animals[animal] >= 3:
        number_of_animals[animal] = 0
    else:
        number_of_animals[animal] += 1
    text_label.config(text=str(number_of_animals[animal]))


gameboard = GameBoard()
root = tkinter.Tk()
root.title("Tkinter try")
root.geometry("650x800")
# create a grid of images in a frame
frame = tkinter.Frame(root, borderwidth=10)
frame.grid()
# create a list of images
empty = tkinter.PhotoImage(file="images/empty.png")
bear = tkinter.PhotoImage(file="images/bear.png")
tapir = tkinter.PhotoImage(file="images/tapir.png")
fox = tkinter.PhotoImage(file="images/fox.png")
jaguar = tkinter.PhotoImage(file="images/jaguar.png")
monkey = tkinter.PhotoImage(file="images/monkey.png")
bat = tkinter.PhotoImage(file="images/bat.png")

t = tkinter.PhotoImage(file="images/t.png")
u = tkinter.PhotoImage(file="images/u.png")
fatl = tkinter.PhotoImage(file="images/fatl.png")
funnyf = tkinter.PhotoImage(file="images/funnyf.png")

animals = {}
animals["empty"] = empty
animals["bear"] = bear
animals["tapir"] = tapir
animals["fox"] = fox
animals["jaguar"] = jaguar
animals["monkey"] = monkey
animals["bat"] = bat

shapes = {}
shapes["T"] = t
shapes["U"] = u
shapes["FATL"] = fatl
shapes["FUNNYF"] = funnyf

# merge the two dictionaries
images = {}
images.update(animals)
images.update(shapes)

# create a list of labels
labels = []
for y in range (gameboard.center_height):
    for x in range (gameboard.center_width):
        labels.append(tkinter.Label(frame, image=images["empty"]))

display_gameboard(gameboard, labels, images)


# add the labels to the grid
for i in range(5):
    for j in range(5):
        labels[i * 5 + j].grid(row=i, column=j)

# create second grid
frame2 = tkinter.Frame(root, borderwidth=10)
frame2.grid()
# add bear image
column = 0
number_of_animals = {}
number_of_animals["bear"] = 0
number_of_animals["tapir"] = 0
number_of_animals["fox"] = 0
number_of_animals["jaguar"] = 0
number_of_animals["monkey"] = 0
number_of_animals["bat"] = 0

for animal in animals:
    if animal != "empty":
        text_label = tkinter.Label(frame2, text=str(number_of_animals[animal]))
        text_label.grid(row=1, column=column)
        image_label = tkinter.Label(frame2, image=animals[animal])
        image_label.bind("<Button-1>", lambda event, animal=animal, text_label=text_label, number_of_animals=number_of_animals: on_click(event, animal, text_label, number_of_animals))
        image_label.grid(row=0, column=column)
        column = column + 1
# add button
button = tkinter.Button(frame2, text="Solve", command=lambda: solve(labels, images))
button.grid(row=2, column=0, columnspan=6)
root.mainloop()

