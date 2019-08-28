
def show(frame):

    import pygame

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (800, 800)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Sudoku")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    font = pygame.font.SysFont('Calibri', 40, True, False)

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Game logic should go here

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(WHITE)

        # --- Drawing code should go here

        x_offset = 0

        m = 9.5
        l = 15

        pygame.draw.line(screen, BLACK, [0,0], [800, 0], 5)
        pygame.draw.line(screen, BLACK, [0,size[1]], [800, size[1]], 5)
        pygame.draw.line(screen, BLACK, [0, 0], [0, 800], 5)
        pygame.draw.line(screen, BLACK, [800, 0], [800, 800], 5)

        pygame.draw.line(screen, BLACK, [0, 800 * 1/3], [800, 800 * 1/3], 5)
        pygame.draw.line(screen, BLACK, [0, 800 * 2/3], [800, 800 * 2/3], 5)

        pygame.draw.line(screen, BLACK, [800 * 1/3, 0], [800 * 1/3, 800], 5)
        pygame.draw.line(screen, BLACK, [800 * 2/3, 0], [800 * 2/3, 800], 5)

        for i in range(9):
            pygame.draw.line(screen, BLACK, [0, 800/9 * i], [800, 800/9 * i], 1)

        for i in range(9):
            pygame.draw.line(screen, BLACK, [800/9 * i, 0], [800/9 * i, 800], 1)

        for i in range(9):
            for n in range(9):
                text = font.render(str(frame[i][n]), True, BLACK)
                screen.blit(text, [800/18 - m + (800/9 * n), 800/18 - l + (800/9 * i)])


        # --- Go ahead and u.................pdate the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()