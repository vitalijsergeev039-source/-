import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Лес с ёлками, солнцем и облаками")
screen.setup(800, 600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_ground():
    t.penup()
    t.goto(-400, -200)
    t.pendown()
    t.color("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(800)
        t.right(90)
        t.forward(400)
        t.right(90)
    t.end_fill()

def draw_sun(x, y, radius=40):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    for _ in range(12):
        t.penup()
        t.goto(x, y + radius)
        t.pendown()
        t.forward(radius + 15)
        t.backward(radius + 15)
        t.right(30)

def draw_cloud(x, y, size=1):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    circles = [
        (0, 0, 25 * size),
        (20 * size, 5 * size, 20 * size),
        (40 * size, 0, 25 * size),
        (15 * size, -15 * size, 18 * size),
        (30 * size, -10 * size, 15 * size)
    ]
    
    for dx, dy, radius in circles:
        t.penup()
        t.goto(x + dx, y + dy - radius)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

def draw_tree(x, y, height=100):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(15)
        t.left(90)
        t.forward(40)  
        t.left(90)
    t.end_fill()
    t.color("darkgreen")
    crown_width = height * 0.6
    levels = 3
    
    for i in range(levels):
        level_y = y + 40 + (i * height/levels)
        level_width = crown_width * (levels - i) / levels
        
        t.penup()
        t.goto(x + 7.5 - level_width/2, level_y)
        t.pendown()
        
        t.begin_fill()
        t.goto(x + 7.5 + level_width/2, level_y)
        t.goto(x + 7.5, level_y + height/levels)
        t.goto(x + 7.5 - level_width/2, level_y)
        t.end_fill()

def draw_forest():
    tree_positions = [
        (-350, -200), (-250, -200), (-150, -200),
        (-50, -200), (50, -200), (150, -200), (250, -200), (350, -200)
    ]
    for x, y in tree_positions:
        tree_height = random.randint(80, 120)
        draw_tree(x, y, tree_height)

def draw_sky_elements():
    draw_sun(-300, 200)
    draw_cloud(-150, 220, 1.0)
    draw_cloud(50, 250, 1.2)
    draw_cloud(200, 230, 0.9)
    draw_cloud(-280, 260, 0.8)
    draw_cloud(300, 200, 1.1)

draw_ground()  
draw_sky_elements()
draw_forest()
turtle.done()
