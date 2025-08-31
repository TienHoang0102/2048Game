# 2024 game ver 0.1
# '''
import pygame
import random
import math

pygame.init()

FPS = 60
WIDTH, HEIGHT = 600, 600
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTlINE_COLOR = (187, 173, 160)
OUTlINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)
MOVE_VEL = 20
FONT = pygame.font.SysFont('comicsans', 60, bold=True)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')

class Tile:
    COLOR = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def  __init__(self, value: int, row: int, col: int):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        color = self.COLOR[color_index]
        return  color

    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(
            window,
            color,
            (self.x, self.y, RECT_WIDTH, RECT_HEIGHT)
        )
        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(
            text,
            (
                self.x + (RECT_WIDTH / 2 - text.get_width() / 2),
                self.y + (RECT_HEIGHT / 2 - text.get_height() / 2)
             )
        )

    def set_pos(self): pass

    def move(self): pass

def draw_grid(window):
    pygame.draw.rect(window, OUTlINE_COLOR, (0,0, WIDTH, HEIGHT), OUTlINE_THICKNESS)
    for row in range(ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTlINE_COLOR, (0, y), (WIDTH, y), OUTlINE_THICKNESS)
    for col in range(COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTlINE_COLOR, (x, 0), (x, HEIGHT), OUTlINE_THICKNESS)

def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)

    pygame.display.update()

def get_random_pos(tiles):
    row = None
    col = None
    while True:
        row = random.randrange(0,ROWS)
        col = random.randrange(0, COLS)

        if f'{row}{col}' not in tiles:
            break
    return row,col

def move_tiles(window, tiles, clock, direction):
    update = True
    blocks = set()

    if direction == 'left':
        sortFunc = lambda x: x.col
        reverse = False
        delta = (-MOVE_VEL, 0)
        boundaryCheck = lambda tile: tile.col == 0  # Return True of False
        getNextTile = lambda  tile: tiles.get(f'{tile.row}{tile.col-1}')
        mergeCheck = lambda tile, nextTile: tile.x > nextTile.X + MOVE_VEL
        moveCheck = lambda tile, nextTile: tile.x > nextTile.X + RECT_WIDTH + MOVE_VEL

    elif direction == 'right':
        pass
    elif direction == 'up':
        pass
    elif direction == 'down':
        pass
def generate_tiles():
    tiles = {}
    for _ in range(2):
        row, col = get_random_pos(tiles)
        tiles[f'{row}{col}'] = Tile(2, row, col)
    return tiles

def main(window):
    clock = pygame.time.Clock()
    run = True

    tiles = generate_tiles()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window, tiles)

    pygame.quit()

if __name__ == '__main__':
    main(WINDOW)

#'''

# Teky: TKinter lib
'''
import tkinter
from tkinter import messagebox, StringVar, Button
import turtle

def showText(text):
    text_2 = text.get()
    messagebox.showinfo('Text', text_2)
    print(text_2)

def thongbao():
    # messagebox.askokcancel('Noti', 'HelloWorld')
    window2 = tkinter.Tk()
    window2.title('Check TKinter')
    window2.config(width=700, height=700, background='#fc8011')
    window2.geometry('300x300+300+300')

    global text
    text = StringVar()
    entry = tkinter.Entry(window2, bd = 10, textvariable=text)
    entry.pack()
    bt_2 = Button(window2, text = 'show Text', command=lambda:showText(text))
    bt_2.pack()
    window2.mainloop()

# turtle = turtle.Turtle()
window = tkinter.Tk()
window.title('Check TKinter')
window.config(width=700, height=700, background='#fc8011')
window.geometry('300x300+100+100')


label1 = tkinter.Label( text='Hello World',anchor='sw')
label1.pack()
label2 = tkinter.Label( text='Hello World_2')
label2.pack()
bt_1 = tkinter.Button( text='PressMe', height=10, width=10, command=thongbao)
bt_1.pack()

# colors = ["red", "yellow"] * 5
# def change_color(i=0):
#     if i < len(colors):
#         window.config(background=colors[i])
#         window.after(2000, change_color, i+1)
# change_color()


window.mainloop()
'''

# Algo: TakeOver -  M5L5. OOP. Inheritance
'''
from typing import Any

class CarARGS:
    def __init__(self, **kwargs):
        self.brand = kwargs.get('brand', 'BrandSample')
        self.color = kwargs.get('color', 'ColorSample')
        self.lights = kwargs.get('lights', 0)
        self.wheels = kwargs.get('wheels', 4)

    def showInfomation(self):
        print(f'the {self.brand} car, color: {self.color}, number of lights: {self.lights}, wheels: {self.wheels}')

    def configure(self,
                  show: bool = False,
                  *,
                  brand: str = ...,
                  color: str = ...,
                  lights: int | str = ...,
                  wheels: int | str = ...
                  ) -> dict[str, tuple[str, Any]] | None:
        if brand is not ...:
            self.brand = brand
        if color is not ...:
            self.color = color
        if lights is not ...:
            self.lights = lights
        if wheels is not ...:
            self.wheels = wheels

        if show:
            return {
                'brand': ('option', self.brand),
                'color': ('option', self.color),
                'lights': ('option', self.lights),
                'wheels': ('option', self.wheels),
            }
        else:
            return None

class Car:
    def __init__(self,
                 brand='BrandSample',
                 color='ColorSample',
                 lights=0,
                 wheels=4):
        self.brand = brand
        self.color = color
        self.lights = lights
        self.wheels = wheels

    def showInfomation(self):
        print(f'the {self.brand} car, color: {self.color}, number of lights: {self.lights}, wheels: {self.wheels}')

    def inCar(self, amountPeople):
        print(f'There\'s/re {amountPeople} inside the car')

class MiniCar(Car, CarARGS):
    def __init__(self, brand, color, lights=2, wheels=3):
        super().__init__(brand, color, lights, wheels)
        self.capacity = 2
        self.size = 'small'

    def showInformation(self):
        print(
            f'[MiniCar] Brand: {self.brand}, Color: {self.color}, Lights: {self.lights}, Wheels: {self.wheels}, Capacity: {self.capacity}')

    def checkCapacity(self, amountPeople):
        if 0 < amountPeople and amountPeople <= self.capacity:
            print(f'OK: {amountPeople} people can sit inside this MiniCar.')
        elif amountPeople > self.capacity:
            print(f'Over capacity! Max {self.capacity} people only.')
        else:
            print('ERROR!!')

# Main Program
my_car = Car('red', 'red', 0,0)
# my_car.showInfomation()
# my_car.inCar(2)

mini_car = MiniCar(brand='Bentley', color='black')
mini_car.configure(brand='Bentley_2')
mini_car.showInformation()
# mini_car.checkCapacity(2)

car_ARGS = CarARGS(brand='BMW', color= 'red', )
# car_ARGS.showInfomation()
car_ARGS.configure(brand='BMW_2', color='red_2')
config = car_ARGS.configure(show=True, brand='bmw_3')
# car_ARGS.showInfomation()
# print(config)
'''

# Teky: Cover - Collision game
'''
import turtle
import random
import math

score = 0

screen = turtle.Screen()

screen.setup(800,800)
screen.bgpic('')

turtle.shape('turtle')
turtle.color('red')
turtle.shapesize(2)

move_speed = 10
turn_speed = 15

def forward():
    global move_speed
    move_speed += 1
    if move_speed >= 5:
        move_speed = 5
def backward():
    global move_speed
    move_speed -= 1
    if move_speed <= -5:
        move_speed = -5
def right():
    turtle.right(turn_speed)
def left():
    turtle.left(turn_speed)

def isCollision(t1, t2):
    global score
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        score += 1
        return True
    else:
        return False

def boundarychecking(t):
    if (t.xcor() < -290) or (t.xcor() > 290):
        t.right(random.randint(135, 225))
        t.forward(20)
    if (t.ycor() < -290) or (t.ycor() > 290):
        t.right(random.randint(135, 225))
        t.forward(20)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = turtle.xcor()
        y = turtle.ycor()
        bullet.setposition(x, y)
        bullet.showturtle()

screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(right, 'd')
screen.onkey(left, 'a')

screen.listen()

barrier = turtle.Turtle()
barrier.penup()
barrier.setposition(-300, -300)
barrier.pendown()
barrier.pensize(5)
barrier.speed(0)

for i in range(4):
    barrier.forward(600)
    barrier.left(90)
barrier.hideturtle()

circle1 = turtle.Turtle()
circle1.shape('circle')
circle1.penup()
circle1.setposition(random.randint(-300, 300), random.randint(-300, 300))
circle2 = turtle.Turtle()
circle2.shape('circle')
circle2.penup()
circle2.setposition(random.randint(-300, 300), random.randint(-300, 300))
circle3 = turtle.Turtle()
circle3.shape('circle')
circle3.penup()
circle3.setposition(random.randint(-300, 300), random.randint(-300, 300))

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("arrow")
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5)
bulletspeed = 20
bulletstate = "ready"

gun = turtle.Turtle()
gun.hideturtle()

while True:
    turtle.forward(move_speed)
    boundarychecking(turtle)
    if isCollision(turtle, circle1):
        print(score)
        circle1.hideturtle()
    if isCollision(turtle, circle2):
        print(score)
        circle2.hideturtle()
    if isCollision(turtle, circle3):
        print(score)
        circle3.hideturtle()
    if score == 3:
        break

    circle1.forward(move_speed)
    boundarychecking(circle1)
    circle2.forward(move_speed)
    boundarychecking(circle2)
    circle3.forward(move_speed)
    boundarychecking(circle3)
    bullet.setposition(turtle.xcor(), turtle.ycor())
'''

# Algo: Cover - the Maze game
'''
import pygame
# from pygame.examples.sprite_texture import sprite

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

window = pygame.display.set_mode((700, 700))
window.fill((0, 80,80))
pygame.display.set_caption('My Game')
run = True

wall1 = GameSprite('picture/pic1.jpg', 80, 180, 200, 250)
wall2 = GameSprite('picture/pic1.jpg', 180, 80, 280, 250)

# player = GameSprite('picture/pic2.gif', 80, 80, 5, 400)
player = Player('picture/pic2.gif', 80, 80, 5, 400,0, 0)

while run:
    pygame.time.delay(50)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                player.y_speed = -5
            if e.key == pygame.K_DOWN:
                player.y_speed = 5
            if e.key == pygame.K_RIGHT:
                player.x_speed = 5
            if e.key == pygame.K_LEFT:
                player.x_speed = -5
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                player.y_speed = 0
            if e.key == pygame.K_DOWN:
                player.y_speed = 0
            if e.key == pygame.K_RIGHT:
                player.x_speed = 0
            if e.key == pygame.K_LEFT:
                player.x_speed = 0

    window.fill((0, 80, 80))
    player.update()
    wall1.reset()
    wall2.reset()
    player.reset()
    pygame.display.update()
'''

# 2024 game ver 0.0.1
'''
def create_array():
    grid = []
    for _ in range(4):
        row = []
        for _ in range(4):
            row.append(0)
        grid.append(row)
    return grid

def display_grid(grid):
    for row in grid:
        print(' '.join(str(num) for num in row))

def add_random_tile(grid):
    while True:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if grid[row][col] == 0:
            grid[row][col] = random.choice([2, 4])
            break
    return grid

grid = create_array()
for _ in range(2):
    add_random_tile(grid)
display_grid(grid)
'''
