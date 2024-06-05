import pygame


class Coin:
    def __init__(self, weight, height, screen):
        self.screen = screen
        self.weight = weight
        self.height = height
        self.mouse_pos = pygame.mouse.get_pos()
        self.index = 0
        self.image = [pygame.transform.scale(pygame.image.load(f'image/coins/coin{i}.png').convert_alpha(),
                                             (self.weight // 4.8, self.height // 3.2)) for i in range(1, 8)]
        self.image_big = [pygame.transform.scale(pygame.image.load(f'image/coins/coin{i}.png').convert_alpha(),
                                                 (self.weight // 4.3, self.height // 2.86)) for i in range(1, 8)]
        self.rotate = self.image[self.index]
        self.rotate_big = self.image_big[self.index]
        self.rect = self.image[self.index].get_rect(center=(self.weight // 2, self.height // 2))
        self.rect_big = self.image_big[self.index].get_rect(center=(self.weight // 2, self.height // 2))
        self.click = False

    def rotating_click(self, user, sound, level):
        self.mouse_pos = pygame.mouse.get_pos()
        self.rotate = self.image[self.index // 7]
        self.rotate_big = self.image_big[self.index // 7]
        self.rect = self.image[self.index // 7].get_rect(center=(self.weight // 2, self.height // 2))
        self.rect_big = self.image_big[self.index // 7].get_rect(center=(self.weight // 2, self.height // 2))
        if self.index < 42:
            if self.index == 0:
                if user.accum >= 1:
                    user.money_user(user.accum * user.multi_accum)
                    self.screen.blit(self.rotate_big, self.rect_big)
                    sound.money_sound(user)

            self.index += 1

        else:
            self.index = 0
        self.screen.blit(self.rotate, self.rect)
        if self.rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.click = True
        else:
            if self.click:
                self.screen.blit(self.rotate_big, self.rect_big)
                sound.money_sound(user)
                user.money_user(user.count * user.multi_count)
                user.click_user()
                level.lvl_up(user, sound)
                self.click = False

    def rotating(self):
        self.rotate = self.image[self.index // 7]
        self.rect = self.image[self.index // 7].get_rect(center=(self.weight // 2, self.height // 2))
        if self.index < 42:
            self.index += 1
        else:
            self.index = 0
        self.screen.blit(self.rotate, self.rect)

    def draw_money(self, user):
        self.money_count = pygame.font.Font(None, self.weight // 24).render(f'Money: {user.money}', True, "#ffffff")
        self.screen.blit(self.money_count, (self.weight // 2.285, 0 // self.height))

    def coin_render(self, user, sound, level):
        self.draw_money(user)
        self.rotating_click(user, sound, level)
