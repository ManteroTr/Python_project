import pygame


class Button:
    def __init__(self, x, y, width, height, screen, color, text=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_hovered = False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect,  0)

        if self.text != None:
            font = pygame.font.Font(None, 36)
            text_screen = font.render(self.text, True, (0, 0, 0))
            text_rect = text_screen.get_rect(center=self.rect.center)
            self.screen.blit(text_screen, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        if self.is_hovered:
            self.color = (128, 128, 128)
        else:
            self.color = (255, 255, 255)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
