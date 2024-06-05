import pygame


class Shop:

    def __init__(self, weight, height, screen):
        self.screen = screen
        self.weight = weight
        self.height = height
        self.mouse_pos = pygame.mouse.get_pos()
        self.shop_icon = pygame.transform.scale(pygame.image.load('image/shop2.png').convert_alpha(),
                                                (self.weight // 12, self.height // 8))
        self.rect = self.shop_icon.get_rect(center=(self.weight // 24, self.height // 16))
        self.shop_menu = pygame.transform.scale(pygame.image.load('image/shop_menu.png').convert_alpha(),
                                                (self.weight // 3, self.height // 1.333))
        self.shop_menu.set_alpha(228)
        self.shop_menu_rect = self.shop_menu.get_rect(center=(self.weight // 6, self.height // 2))
        self.skill1 = pygame.transform.scale(pygame.image.load('image/skill1.png').convert_alpha(),
                                             (self.weight // 3.076, self.height // 5.95))
        self.skill1_rect = self.skill1.get_rect(center=(self.weight // 6, self.height // 4.44))
        self.skill1.set_alpha(228)
        self.skill2 = pygame.transform.scale(pygame.image.load('image/skill2.png').convert_alpha(),
                                             (self.weight // 3.076, self.height // 5.95))
        self.skill2_rect = self.skill2.get_rect(center=(self.weight // 6, self.height // 2.44))
        self.skill2.set_alpha(228)
        self.skill3 = pygame.transform.scale(pygame.image.load('image/skill3.png').convert_alpha(),
                                             (self.weight // 3.076, self.height // 5.95))
        self.skill3_rect = self.skill3.get_rect(center=(self.weight // 6, self.height // 1.687))
        self.skill3.set_alpha(228)
        self.skill4 = pygame.transform.scale(pygame.image.load('image/skill4.png').convert_alpha(),
                                             (self.weight // 3.076, self.height // 5.95))
        self.skill4_rect = self.skill4.get_rect(center=(self.weight // 6, self.height // 1.292))
        self.skill4.set_alpha(228)
        self.shop_open = False
        self.shop_open_cor = False
        self.skill1_buy = False
        self.skill2_buy = False
        self.skill3_buy = False
        self.skill4_buy = False
        self.close_sound = False

    def draw_shop(self, user, sound):
        self.mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.shop_icon, self.rect)

        if self.rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0] and self.shop_open == False:
            sound.open_sound(user)
            if (self.shop_menu_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]
                    and self.shop_open_cor == False):
                self.shop_open_cor = True
            self.shop_open = True
            self.close_sound = True
        else:
            if self.shop_open:
                self.screen.blit(self.shop_menu, self.shop_menu_rect)
                self.skills_buy(user, sound)
                self.draw_skill1(user)
                self.draw_skill2(user)
                self.draw_skill3(user)
                self.draw_skill4(user)
            if (pygame.mouse.get_pressed()[0] and not self.rect.collidepoint(self.mouse_pos)
                    and not self.shop_menu_rect.collidepoint(self.mouse_pos)):
                if self.close_sound:
                    self.close_sound = False
                    sound.close_sound(user)
                self.shop_open = False
                self.shop_open_cor = False

    def draw_skill1(self, user):
        self.screen.blit(self.skill1, self.skill1_rect)
        self.skill1_name = pygame.font.Font('font/font2.ttf', self.weight // 30).render('Многопалый', True, "#59FFA9")
        self.screen.blit(self.skill1_name, (self.weight // 7.47, self.height // 6.5))
        self.skill1_count = pygame.font.Font('font/font2.ttf', self.weight // 40).render(f'У вас: {user.count}', True,
                                                                                         "#59FFA9")
        self.screen.blit(self.skill1_count, (self.weight // 7.47, self.height // 4.77))
        self.skill1_cost_text = (pygame.font.Font('font/font2.ttf', self.weight // 40).render
                                 (f'Цена: {user.skill1_cost}', True, "#59FFA9"))
        self.screen.blit(self.skill1_cost_text, (self.weight // 7.47, self.height // 3.9))
        if self.skill1_rect.collidepoint(self.mouse_pos):
            self.skill1.set_alpha(255)
        else:
            self.skill1.set_alpha(228)

    def draw_skill2(self, user):
        self.screen.blit(self.skill2, self.skill2_rect)
        self.skill2_name = pygame.font.Font('font/font2.ttf', self.weight // 30).render('Многорукий', True, "#59FFA9")
        self.screen.blit(self.skill2_name, (self.weight // 7.47, self.height // 2.97))
        self.skill2_count = pygame.font.Font('font/font2.ttf', self.weight // 40).render(f'У вас: {user.multi_count}', True, "#59FFA9")
        self.screen.blit(self.skill2_count, (self.weight // 7.47, self.height // 2.56))
        self.skill2_cost_text = pygame.font.Font('font/font2.ttf', self.weight // 40).render(f'Цена: {user.skill2_cost}', True,
                                                                              "#59FFA9")
        self.screen.blit(self.skill2_cost_text, (self.weight // 7.47, self.height // 2.285))
        if self.skill2_rect.collidepoint(self.mouse_pos):
            self.skill2.set_alpha(255)
        else:
            self.skill2.set_alpha(228)

    def draw_skill3(self, user):
        self.screen.blit(self.skill3, self.skill3_rect)
        self.skill3_name = pygame.font.Font('font/font2.ttf', self.weight // 30).render('Ленивый', True, "#59FFA9")
        self.screen.blit(self.skill3_name, (self.weight // 7.47, self.height // 1.921))
        self.skill3_count = pygame.font.Font('font/font2.ttf', self.weight // 40).render(f'У вас: {user.accum}', True, "#59FFA9")
        self.screen.blit(self.skill3_count, (self.weight // 7.47, self.height // 1.73))
        self.skill3_cost_text = pygame.font.Font('font/font2.ttf', self.weight // 40).render(f'Цена: {user.skill3_cost}', True,
                                                                              "#59FFA9")
        self.screen.blit(self.skill3_cost_text, (self.weight // 7.47, self.height // 1.598))
        if self.skill3_rect.collidepoint(self.mouse_pos):
            self.skill3.set_alpha(255)
        else:
            self.skill3.set_alpha(228)

    def draw_skill4(self, user):
        self.screen.blit(self.skill4, self.skill4_rect)
        self.skill4_name = pygame.font.Font('font/font2.ttf', self.weight // 30).render('Бережливый', True, "#59FFA9")
        self.screen.blit(self.skill4_name, (self.weight // 7.47, self.height // 1.42))
        self.skill4_count = pygame.font.Font('font/font2.ttf', self.weight // 40).render(f'У вас: {user.multi_accum}', True, "#59FFA9")
        self.screen.blit(self.skill4_count, (self.weight // 7.47, self.height // 1.315))
        self.skill4_cost_text = pygame.font.Font('font/font2.ttf', self.weight // 40).render(f'Цена: {user.skill4_cost}', True,
                                                                              "#59FFA9")
        self.screen.blit(self.skill4_cost_text, (self.weight // 7.47, self.height // 1.241))
        if self.skill4_rect.collidepoint(self.mouse_pos):
            self.skill4.set_alpha(255)
        else:
            self.skill4.set_alpha(228)

    def skills_buy(self, user, sound):
        if self.skill1_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]:
            if user.money < user.skill1_cost:
                sound.no_money_sound(user)
            if user.money >= user.skill1_cost:
                self.skill1_buy = True
        else:
            if self.skill1_buy:
                if user.money >= user.skill1_cost:
                    user.money -= user.skill1_cost
                    sound.buy_sound(user)
                    user.count_user()
                    user.skill1_cost_user(user.skill1_cost * 2)
                    self.skill1_buy = False

        if self.skill2_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]:
            if user.money < user.skill2_cost:
                sound.no_money_sound(user)
            if user.money >= user.skill2_cost:
                self.skill2_buy = True
        else:
            if self.skill2_buy:
                if user.money >= user.skill2_cost:
                    user.money -= user.skill2_cost
                    sound.buy_sound(user)
                    user.multi_count_user()
                    user.skill2_cost_user(user.skill2_cost * 10)
                    self.skill2_buy = False

        if self.skill3_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]:
            if user.money < user.skill3_cost:
                sound.no_money_sound(user)
            if user.money >= user.skill3_cost:
                self.skill3_buy = True
        else:
            if self.skill3_buy:
                if user.money >= user.skill3_cost:
                    user.money -= user.skill3_cost
                    sound.buy_sound(user)
                    user.accum_user()
                    user.skill3_cost_user(user.skill3_cost * 3)
                    self.skill3_buy = False

        if self.skill4_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]:
            if user.money < user.skill4_cost:
                sound.no_money_sound(user)
            if user.money >= user.skill4_cost:
                self.skill4_buy = True
        else:
            if self.skill4_buy:
                if user.money >= user.skill4_cost:
                    user.money -= user.skill4_cost
                    sound.buy_sound(user)
                    user.multi_accum_user()
                    user.skill4_cost_user(user.skill4_cost * 5)
                    self.skill4_buy = False
