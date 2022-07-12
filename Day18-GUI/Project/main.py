# Extract colors using colorgram
# import colorgram
import turtle as t
import random
#
# colors = colorgram.extract('image.jpg', 21)
#
# print(colors)
#
# color_rgb = []
# print(len(colors))
# for c in range(len(colors)):
#     color_curr = colors[c]
#     r = color_curr.rgb.r
#     g = color_curr.rgb.g
#     b = color_curr.rgb.b
#
#     color_rgb.append((r, g, b))
#
# print(color_rgb)

color_list = [(236, 35, 108), (145, 28, 64), (239, 75, 35), (6, 148, 93), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191)]

turt = t.Turtle()
screen = t.Screen()
screen.colormode(255)
x, y = -350, -350
turt.penup()

for _ in range(10):
    turt.goto(x, y)
    for _ in range(10):
        col = random.choice(color_list)
        r = col[0]
        g = col[1]
        b = col[2]
        turt.color((r, g, b))
        turt.dot(20)
        turt.forward(70)
    y += 70

screen.exitonclick()

