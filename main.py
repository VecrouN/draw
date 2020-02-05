import draw_window
import numpy

print(1)
width = 10
height = 5
rand = 2
array = numpy.zeros((width, height, 3))
array = draw_window.draw_win(width, height, rand)
print(2)
print(array)
print('*******')
for i in range(width):
    for j in range(height):
        print(array[int(i)][int(j)][int(0)], array[int(i)][int(j)][int(1)], array[int(i)][int(j)][int(2)])
    print()
