import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []

    mouse_pressed = False

    pick_form = 0
    screen.fill((255, 255, 255))
    while True:

        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_q:
                    pick_form = 0
                    points = []
                elif event.key == pygame.K_a:
                    pick_form = 1
                    points = []
                elif event.key == pygame.K_z:
                    pick_form = 2
                    points = []
                elif event.key == pygame.K_UP:
                    radius = min(200, radius + 1)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # нажатие кнопки мыши
                    mouse_pressed = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # отпускание кнопки мыши
                    mouse_pressed = False

            if event.type == pygame.MOUSEMOTION:  # перемещение курсора мыши

                position = event.pos
                if mouse_pressed:
                    points = points + [position]
                    points = points[-256:]
                else:
                    points = []

        # draw all points
        i = 0
        while i < len(points) - 1:
            if pick_form == 0:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, pick_form, mouse_pressed)
            if pick_form == 1:
                drawLineRect(screen, i, points[i], points[i + 1], radius, mode, pick_form, mouse_pressed)
            if pick_form == 2:
                drawLineEraser(screen, i, points[i], points[i + 1], radius, mode, pick_form, mouse_pressed)
            i += 1

        pygame.display.flip()

        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode, pick_form, mouse_pressed):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if mouse_pressed:
            pygame.draw.circle(screen, color_mode, (x, y), width)


def drawLineRect(screen, index, start, end, width, color_mode, pick_form, mouse_pressed):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if mouse_pressed:
            pygame.draw.rect(screen, color_mode, [x, y, width, width])


def drawLineEraser(screen, index, start, end, width, color_mode, pick_form, mouse_pressed):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if mouse_pressed:
            pygame.draw.circle(screen, 'white', (x, y), width)


main()