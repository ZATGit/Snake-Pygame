import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

snake_box_width = 15
snake_box_height = 15
snake_box_margin = 3


class Box(pygame.sprite.Sprite):
    """ Class properties for each box of snake body. """
    def __init__(self,x,y):
        super().__init__()
        #Snake Height, Width, Pass-in
        self.image = pygame.Surface([snake_box_width, snake_box_height])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = -1
        self.change_y = -1

def main():

    pygame.init()

    #[Width,Height] of Screen
    size = [700, 500]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake Snake Revolution")

    all_sprites_list = pygame.sprite.Group()

    #Snake Start Speed
    x_change = snake_box_width + snake_box_margin
    y_change = 0

    #Create Snake
    #Append Each Box to Both Lists
    snake_body = []
    for i in range(15):
        x = 250 - (snake_box_width + snake_box_margin) * i
        y = 30
        snake_box = Box(x, y)
        snake_body.append(snake_box)
        all_sprites_list.add(snake_box)

    # Manage Screen Update Speed
    clock = pygame.time.Clock()

    done = False

    while not done:
        #Event Processing
        #Quit Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        #Snake Movement (Up,Down,Left,Right)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    x_change = 0
                    y_change = (snake_box_height + snake_box_margin) * -1
                if event.key == pygame.K_s:
                    x_change = 0
                    y_change = (snake_box_height + snake_box_margin)
                if event.key == pygame.K_a:
                    x_change = (snake_box_width + snake_box_margin) * -1
                    y_change = 0
                if event.key == pygame.K_d:
                    x_change = (snake_box_width + snake_box_margin)
                    y_change = 0

        score = 0

        #Shorten Snake: Remove/Return Last Item Both Lists
        removed_box = snake_body.pop()
        all_sprites_list.remove(removed_box)

        #New Box Location
        x = snake_body[0].rect.x + x_change
        y = snake_body[0].rect.y + y_change
        snake_box = Box(x,y)

        #Insert New Box Item to List
        snake_body.insert(0,snake_box)
        all_sprites_list.add(snake_box)


        # Screen Fill Background
        screen.fill(BLACK)

        #Draw
        all_sprites_list.draw(screen)

        font = pygame.font.SysFont('Courier', 25)
        scoretext = font.render("Score:" + str(score), True, WHITE)
        screen.blit(scoretext, [10, 10])

        #Flip Screen
        pygame.display.flip()

        #Clock FPS
        clock.tick(5)

    pygame.quit()


if __name__ == "__main__":
    main()