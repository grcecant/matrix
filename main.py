
from display import *
from draw import *
from matrix import *

#testing add_edge
print('Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 = ')
m2 = new_matrix(rows=4, cols=0)
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)
print('\n')

#testing identity matrix
print('Testing ident. m1 = ')
m1 = new_matrix()
ident(m1)
print_matrix(m1)
print('\n')

#testing matrix multiplication
print('Testing matrix mult. m1 * m2 = ')
matrix_mult(m1, m2)
print_matrix(m2)
print('\n')

#testing matrix multiplication, pt.2
print('Testing matrix mult. m3 = ')
m3 = new_matrix(rows=4, cols=0)
add_point(m3, 0, 500, 250)
add_point(m3, 250, 0, 500)
add_edge(m3, 100, 100, 100, 250, 500, 0)
print_matrix(m3)
print('\n')

#testing matrix multiplication, pt.3
print('Testing matrix mult. m4 = ')
m4 = new_matrix(rows=4, cols=0)
add_point(m4, 0, 500, 250)
add_point(m4, 250, 0, 500)
print_matrix(m4)
print('\n')

#testing matrix multiplication, pt.4
print('Testing matrix mult. m3 * m4 = ')
matrix_mult(m3, m4)
print_matrix(m4)
print('\n')

#rainbow image
screen = new_screen()
x1, y1, x2, y2 = 250, 0, 500, 500

#purple
purple = new_matrix()
color = [76, 0, 153]
while x2 > 437.5:
    add_edge(purple, x1, y1, 0, x2, y2, 0)
    x2 -= 1
draw_lines(purple, screen, color)

#indigo
indigo = new_matrix()
color = [0, 0, 102]
while x2 > 375:
    add_edge(indigo, x1, y1, 0, x2, y2, 0)
    x2 -= 1
draw_lines(indigo, screen, color)

#blue
blue = new_matrix()
color = [102, 178, 255]
while x2 > 312.5:
    add_edge(blue, x1, y1, 0, x2, y2, 0)
    x2 -= 1
draw_lines(blue, screen, color)

#green
green = new_matrix()
color = [102, 204, 0]
while x2 > 250:
    add_edge(green, x1, y1, 0, x2, y2, 0)
    x2 -= 1
draw_lines(green, screen, color)

#yellow
yellow = new_matrix()
color = [255, 255, 0]
while x2 > 187.5:
    add_edge(yellow, x1, y1, 0, x2, y2, 0)
    x2 -= 1
draw_lines(yellow, screen, color)

#orange
orange = new_matrix()
color = [255, 128, 0]
while x2 > 125:
    add_edge(orange, x1, y1, 0, x2, y2, 0)
    x2 -= 1
draw_lines(orange, screen, color)

#red
red = new_matrix()
color = [255, 0, 0]
while x2 > 62.5:
    add_edge(red, x1, y1, 0, x2, y2, 0)
    x2 -= 1
draw_lines(red, screen, color)

#pink
pink = new_matrix()
color = [255, 153, 204]
while x2 > 0:
    add_edge(pink, x1, y1, 0, x2, y2, 0)
    x2 -= 1
draw_lines(pink, screen, color)

save_ppm_ascii(screen, 'pic.ppm')
save_extension(screen, 'rainbow.png')
display(screen)


'''
# test mr.dw face image
screen = new_screen()
color = [255,0,255]
edges = new_matrix(cols=0)

add_edge(edges, 50, 450, 0, 100, 450, 0)
add_edge(edges, 50, 450, 0, 50, 400, 0)
add_edge(edges, 100, 450, 0, 100, 400, 0)
add_edge(edges, 100, 400, 0, 50, 400, 0)

add_edge(edges, 200, 450, 0, 250, 450, 0)
add_edge(edges, 200, 450, 0, 200, 400, 0)
add_edge(edges, 250, 450, 0, 250, 400, 0)
add_edge(edges, 250, 400, 0, 200, 400, 0)

add_edge(edges, 150, 400, 0, 130, 360, 0)
add_edge(edges, 150, 400, 0, 170, 360, 0)
add_edge(edges, 130, 360, 0, 170, 360, 0)

add_edge(edges, 100, 340, 0, 200, 340, 0)
add_edge(edges, 100, 320, 0, 200, 320, 0)
add_edge(edges, 100, 340, 0, 100, 320, 0)
add_edge(edges, 200, 340, 0, 200, 320, 0)

draw_lines(edges, screen, color)
'''
