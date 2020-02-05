import draw_window
import numpy


width = 256
height = 256
rand = 10
array = numpy.zeros((width, height, 3))
array = draw_window.draw_win(width, height, rand)
print(array)
print('*******')
for i in range(width):
    for j in range(height):
        print(array[int(i)][int(j)][int(0)], array[int(i)][int(j)][int(1)], array[int(i)][int(j)][int(2)])
    print()
