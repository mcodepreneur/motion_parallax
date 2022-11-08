'''
Author: Michael Denenberg
Description: This program displays a landscape with three random color
             mountains, a sun, a field with grass, a tree, and birds
             flying in a 'v' formation. All objects move in
             correspondence to a change in perspective actuated by
             mouse movements.

'''

import random
from graphics import graphics


def rand_color():
    return graphics.get_color_string(graphics, random.randint(0, 255),
                                               random.randint(0, 255),
                                               random.randint(0, 255))


def main():
    gui = graphics(600, 600, 'canvas')
    color1, color2, color3 = rand_color(), rand_color(), rand_color()
    i = 0
    ti = 0

    while True:
        gui.clear()

        x_off = (gui.mouse_x - 300) / 300
        y_off = (gui.mouse_y - 300) / 300
        phr = 1
        #print(round(x_off, 2), round(y_off, 2))
        gui.rectangle(0, 0, 600, 600, 'lightskyblue')

        sun_off = 10 * phr
        gui.ellipse(400 + (sun_off * x_off), 100 + (sun_off * y_off), 90, 90, 'gold')

        tri_off1 = 18 * phr
        tri_off2 = 21 * phr
        tri_off3 = 26 * phr

        gui.triangle(-400 + (tri_off1 * x_off), 600 + (tri_off1 * y_off),
                     140 + (tri_off1 * x_off), 200 + (tri_off1 * y_off),
                     700 + (tri_off1 * x_off), 600 + (tri_off1 * y_off), color1)
        gui.triangle(-100 + (tri_off2 * x_off), 600 + (tri_off2 * y_off),
                     400 + (tri_off2 * x_off), 220 + (tri_off2 * y_off),
                     1100 + (tri_off2 * x_off), 600 + (tri_off2 * y_off), color2)

        if i % 50 == 0:
            ti += 1

        brrt_off = 24 * phr
        for x in range(-4, 5):  #birds
            apex = (i - (abs(x) * 20) + (brrt_off * x_off), 250 + (x * 10) + (brrt_off * y_off))
            osc = ti % 3
            gui.line(apex[0] - 8, apex[1] - 3 - (osc - 1), apex[0], apex[1], 'black', 2)
            gui.line(apex[0] + 8, apex[1] - 3 - (osc - 1), apex[0], apex[1], 'black', 2)

        gui.triangle(0 + (tri_off3 * x_off), 600 + (tri_off3 * y_off),
                     290 + (tri_off3 * x_off), 230 + (tri_off3 * y_off),
                     600 + (tri_off3 * x_off), 600 + (tri_off3 * y_off), color3)

        plain_off = 40 * phr
        gui.rectangle(-100 + (plain_off * x_off), 400 + (plain_off * y_off), 800, 300, 'forestgreen')

        for x in range(-100, 700, 4):
            gui.rectangle(x + (plain_off * x_off), 392 + (plain_off * y_off), 3, 10, 'seagreen')

        tree_off = 46 * phr
        gui.rectangle(400 + (tree_off * x_off), 350 + (tree_off * y_off), 25, 110, 'sienna')
        gui.ellipse(413 + (tree_off * x_off), 320 + (tree_off * y_off), 70, 150, 'green')



        gui.update_frame(60)
        i += 2
        if i > 736:
            i = -26
            ti = 0


main()

