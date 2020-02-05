import pygame
import pygame.surfarray as surfarray
import pygame.display as display


def draw_win(width, height, rand):
    pygame.init()
    # радиус рисования
    input_screen = pygame.display.set_mode((width, height))  # создание поверхности для рисования
    clock = pygame.time.Clock()  # создание объекта clock класса Clock для ограничения колличесвта кадров в секундк (
    # FPS)
    fps = 60  # переменная колличесвта кадров в секундк
    WHITE = (255, 255, 255)  # переменная черного цвета (rgb котртеж)
    BLACK = (0, 0, 0)  # переменная белого цвета (rgb котртеж)
    input_screen.fill(WHITE)  # заливаем поверхность для рисования белым
    display.set_caption('Ввод')  # переименование окна
    running = True  # переменная для выхода из цикла
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):  # условие для выхода
                input_screen.lock()  # блоировка поверхности
                result_array = surfarray.array3d(input_screen)  # сохранение поверхности в масив
                input_screen.unlock()  # разблокировка поверхности
                running = False  # выход из цикла

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # условие нажания пкм
                input_screen.fill(WHITE)  # зачистка повехности

            elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:  # условие перемещения зажатой лкм
                pygame.draw.circle(input_screen, BLACK, event.pos, rand)  # рисование круга под мышкой

        pygame.display.flip()  # обновление поверхности
        clock.tick(fps)  # ограничение fps

    pygame.quit()  # выход
    result_screen = pygame.display.set_mode((width, height))  # создание окна
    display.set_caption('Вывод')  # переименование
    surfarray.blit_array(result_screen, result_array)  # отрисовка содержимого массива
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
        pygame.display.flip()
        clock.tick(fps / 5)
    pygame.quit()  # выход
    clock.tick(fps / 5)
    return result_array


if __name__ == '__main__':
    width_ = 10
    height_ = 5
    rand_ = 1
    print(draw_win(width_, height_, rand_))
