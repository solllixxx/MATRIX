import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Получаем размеры экрана
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h

# Создаём экран в полноэкранном режиме
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME | pygame.FULLSCREEN)

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Устанавливаем параметры шрифта
font = pygame.font.SysFont('Courier', 20)

# Количество колонок и строк
columns = screen_width // 20  # Количество колонок
rows = screen_height // 20  # Количество строк

# Генерация случайных символов
def generate_matrix_effect():
    drops = [0] * columns  # Начальные позиции для капель

    while True:
        screen.fill(BLACK)  # Заполняем экран чёрным цветом

        # Рисуем каждую каплю
        for i in range(columns):
            # Рисуем несколько символов в каждой колонке
            for j in range(3):  # Здесь 3 - это количество символов в каждой колонке
                symbol = chr(random.randint(33, 126))  # Случайный символ
                x = i * 20  # Позиция по оси X
                y = (drops[i] + j * 5) * 20  # Позиция по оси Y, смещаем каждый символ в колонке

                text = font.render(symbol, True, GREEN)
                screen.blit(text, (x, y))

            # Обновляем позицию капли
            if drops[i] * 20 > screen_height and random.random() > 0.975:
                drops[i] = 0
            drops[i] += 1

        pygame.display.update()  # Обновляем экран
        time.sleep(0.05)  # Устанавливаем скорость

        # Обработка выхода из программы (клавиша Esc)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Закрытие при нажатии Esc
                    pygame.quit()
                    quit()

# Запуск эффекта
generate_matrix_effect()
