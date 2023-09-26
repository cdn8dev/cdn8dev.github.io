import pygame

# Rechteck erstellen, welches die Bälle auffängt
class Fangrechteck(pygame.sprite.Sprite):
    def __init__(self, x_fang, y_fang, y_fanggeschw):
        super().__init__()
        self.x_fang = x_fang
        self.y_fang = y_fang
        self.fang_position = (self.x_fang, self.y_fang)
        self.fang_geschw = y_fanggeschw

    def update(self):
        global moving_right_bool, moving_left_bool
        if moving_right_bool:
            self.y_fang += self.fang_geschw
        if moving_left_bool:
            self.y_fang -= self.fang_geschw

    def draw(self, surface):
        pygame.draw.rect(surface, red, pygame.Rect(self.fang_position, (100, 10)))

    def moving_right(self):
        if moving_right_bool:
            self.fang_position = (self.fang_position[0], self.fang_position[1] + self.fang_geschw)

    def moving_left(self):
        if moving_left_bool:
            self.fang_position = (self.fang_position[0], self.fang_position[1] - self.fang_geschw)

def fangspiel():
    global moving_right_bool, moving_left_bool, red, weiss

    pygame.init()
    clock = pygame.time.Clock()

    # Farben
    weiss = (255, 255, 255)
    red = (255, 0, 0)

    # Display und alle Einstellungen
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption('Fangspiel')

    running = True
    moving_right_bool = False
    moving_left_bool = False

    fangrect = Fangrechteck(350, 650, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_RIGHT:
                    moving_right_bool = True
                elif event.key == pygame.K_LEFT:
                    moving_left_bool = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right_bool = False
                elif event.key == pygame.K_LEFT:
                    moving_left_bool = False

        fangrect.update()

        screen.fill(weiss)

        fangrect.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    fangspiel()
