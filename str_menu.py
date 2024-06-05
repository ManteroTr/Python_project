import pygame


class Menu:

    def __init__(self, weight, height, screen):
        self.weight = weight
        self.height = height
        self.screen = screen
        self.mouse_pos = pygame.mouse.get_pos()
        self.bg_dark = pygame.transform.scale(pygame.image.load('image/shop_menu.png').convert_alpha(),
                                              (self.weight, self.height))
        self.bg_dark.set_alpha(245)
        self.button_play = pygame.transform.scale(pygame.image.load('image/button.png').convert_alpha(),
                                                  (self.weight // 6, self.height // 10))
        self.button_play_rect = self.button_play.get_rect(center=(self.weight // 2, self.height // 1.379))
        self.button_sett = pygame.transform.scale(pygame.image.load('image/button.png').convert_alpha(),
                                                  (self.weight // 6, self.height // 10))
        self.button_sett_rect = self.button_sett.get_rect(center=(self.weight // 2, self.height // 1.1764))
        self.button_play_up = pygame.transform.scale(pygame.image.load('image/button_up.png').convert_alpha(),
                                                  (self.weight // 6, self.height // 10))
        self.button_play_up_rect = self.button_play_up.get_rect(center=(self.weight // 2, self.height // 1.3793))
        self.button_sett_up = pygame.transform.scale(pygame.image.load('image/button_up.png').convert_alpha(),
                                                (self.weight // 6, self.height // 10))
        self.button_sett_up_rect = self.button_sett_up.get_rect(center=(self.weight // 2, self.height // 1.1764))
        self.button_play_txt = pygame.font.Font('font/font2.ttf', self.weight // 24).render('Играть', True, "#59FFA9")
        self.button_play_txt_rect = self.button_play_txt.get_rect(center=(self.weight // 2, self.height // 1.3793))
        self.button_sett_txt = pygame.font.Font('font/font2.ttf', self.weight // 31).render('Настройки', True, "#59FFA9")
        self.button_sett_txt_rect = self.button_sett_txt.get_rect(center=(self.weight // 2, self.height // 1.1764))
        self.sett_menu = pygame.transform.scale(pygame.image.load('image/sett_menu.png').convert_alpha(),
                                                  (self.weight // 2, self.height // 2.666))
        self.sett_menu_rect = self.sett_menu.get_rect(center=(self.weight // 2, self.height // 2.857))
        self.sett_wh1 = pygame.transform.scale(pygame.image.load('image/button.png').convert_alpha(),
                                               (self.weight // 8, self.height // 10))
        self.sett_wh1_rect = self.sett_wh1.get_rect(center=(self.weight // 2.9268, self.height // 4))
        self.sett_wh2 = pygame.transform.scale(pygame.image.load('image/button.png').convert_alpha(),
                                               (self.weight // 8, self.height // 10))
        self.sett_wh2_rect = self.sett_wh2.get_rect(center=(self.weight // 2, self.height // 4))
        self.sett_wh3 = pygame.transform.scale(pygame.image.load('image/button.png').convert_alpha(),
                                               (self.weight // 8, self.height // 10))
        self.sett_wh3_rect = self.sett_wh3.get_rect(center=(self.weight // 1.5189, self.height // 4))
        self.sett_left = pygame.transform.scale(pygame.image.load('image/button_left_down.png').convert_alpha(),
                                                (self.weight // 15, self.height // 10))
        self.sett_left_rect = self.sett_left.get_rect(center=(self.weight // 2.9268, self.height // 2.2857))
        self.sett_right = pygame.transform.scale(pygame.image.load('image/button_right_down.png').convert_alpha(),
                                                 (self.weight // 15, self.height // 10))
        self.sett_right_rect = self.sett_right.get_rect(center=(self.weight // 1.5189, self.height // 2.2857))
        self.sett_left_up = pygame.transform.scale(pygame.image.load('image/button_left.png').convert_alpha(),
                                                (self.weight // 15, self.height // 10))
        self.sett_left_up_rect = self.sett_left_up.get_rect(center=(self.weight // 2.9268, self.height // 2.2857))
        self.sett_right_up = pygame.transform.scale(pygame.image.load('image/button_right.png').convert_alpha(),
                                                 (self.weight // 15, self.height // 10))
        self.sett_right_up_rect = self.sett_right_up.get_rect(center=(self.weight // 1.5189, self.height // 2.2857))
        self.sett_scroll = pygame.transform.scale(pygame.image.load('image/scroll_vol.png').convert_alpha(),
                                                  (self.weight // 4.6153, self.height // 32))
        self.sett_scroll_rect = self.sett_right.get_rect(center=(self.weight // 2.3529,  self.height // 2.1052))
        self.sett_pol = pygame.transform.scale(pygame.image.load('image/scroll_pol.png').convert_alpha(),
                                               (self.weight // 60, self.height // 20))
        self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 2, self.height // 2.2857))
        self.sett_wh1_1 = pygame.font.Font('font/font2.ttf', self.weight // 48).render('900x600', True, "#59FFA9")
        self.sett_wh1_1_rect = self.sett_wh1_1.get_rect(center=(self.weight // 2.9268, self.height // 4))
        self.sett_wh2_2 = pygame.font.Font('font/font2.ttf', self.weight // 48).render('1200x800', True, "#59FFA9")
        self.sett_wh2_2_rect = self.sett_wh2_2.get_rect(center=(self.weight // 2, self.height // 4))
        self.sett_wh3_3 = pygame.font.Font('font/font2.ttf', self.weight // 48).render('1500x1000', True, "#59FFA9")
        self.sett_wh3_3_rect = self.sett_wh3_3.get_rect(center=(self.weight // 1.5189, self.height // 4))
        self.play_pos = False
        self.sett_pos = False
        self.sett_open = False
        self.sett_open_cor = False
        self.play = False
        self.button1_press = False
        self.button2_press = False
        self.button3_press = False
        self.button_left_press = False
        self.button_right_press = False

    def draw_menu_button(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.button_play, self.button_play_rect)
        self.screen.blit(self.button_sett, self.button_play_rect)
        if self.button_play_rect.collidepoint(self.mouse_pos):
            self.play_pos = True
            self.screen.blit(self.button_play_up, self.button_play_up_rect)
        else:
            self.play_pos = False
            self.screen.blit(self.button_play, self.button_play_rect)
        if self.button_sett_rect.collidepoint(self.mouse_pos):
            self.sett_pos = True
            self.screen.blit(self.button_sett_up, self.button_sett_up_rect)
        else:
            self.sett_pos = False
            self.screen.blit(self.button_sett, self.button_sett_rect)
        self.screen.blit(self.button_play_txt, self.button_play_txt_rect)
        self.screen.blit(self.button_sett_txt, self.button_sett_txt_rect)

    def start_game(self):
        self.mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.play_pos:
            self.play = True

    def sett_game(self, user, coin):
        self.mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.sett_pos and self.sett_open is False:
            if (self.sett_menu_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]
                    and self.sett_open_cor is False):
                self.sett_open_cor = True
            self.sett_open = True
        else:
            if self.sett_open:
                self.screen.blit(self.sett_menu, self.sett_menu_rect)
                self.draw_sett_button()
                self.sett_button(user, coin)
            if (pygame.mouse.get_pressed()[0] and self.sett_pos == False
                    and not self.sett_menu_rect.collidepoint(self.mouse_pos)):
                self.sett_open_cor = False
                self.sett_open = False

    def draw_sett_button(self):
        self.screen.blit(self.sett_wh1, self.sett_wh1_rect)
        self.screen.blit(self.sett_wh1_1, self.sett_wh1_1_rect)
        self.screen.blit(self.sett_wh2, self.sett_wh2_rect)
        self.screen.blit(self.sett_wh2_2, self.sett_wh2_2_rect)
        self.screen.blit(self.sett_wh3, self.sett_wh3_rect)
        self.screen.blit(self.sett_wh3_3, self.sett_wh3_3_rect)
        self.screen.blit(self.sett_left, self.sett_left_rect)
        self.screen.blit(self.sett_right, self.sett_right_rect)
        self.screen.blit(self.sett_scroll, self.sett_scroll_rect)
        self.screen.blit(self.sett_pol, self.sett_pol_rect)

    def sett_button(self, user, coin):
        if (self.sett_wh1_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]
                and self.button1_press == False):
            self.button1_press = True
            self.button2_press = False
            self.button3_press = False
        else:
            if self.button1_press:
                user.weight = 900
                user.height = 600
                self.__init__(user.weight, user.height, self.screen)
                coin.__init__(user.weight, user.height, self.screen)
                self.scroll_cor(user)

        if (self.sett_wh2_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]
                and self.button2_press == False):
            self.button2_press = True
            self.button1_press = False
            self.button3_press = False
        else:
            if self.button2_press:
                user.weight = 1200
                user.height = 800
                self.__init__(user.weight, user.height, self.screen)
                coin.__init__(user.weight, user.height, self.screen)
                self.scroll_cor(user)

        if (self.sett_wh3_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]
                and self.button3_press == False):
            self.button3_press = True
            self.button1_press = False
            self.button2_press = False
        else:
            if self.button3_press:
                user.weight = 1500
                user.height = 1000
                self.__init__(user.weight, user.height, self.screen)
                coin.__init__(user.weight, user.height, self.screen)
                self.scroll_cor(user)

        if self.sett_left_rect.collidepoint(self.mouse_pos):
            self.screen.blit(self.sett_left_up, self.sett_left_up_rect)
        if self.sett_left_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.button_left_press = True
        else:
            if self.button_left_press:
                self.button_left_press = False
                if user.volume == 0.5:
                    self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 2.553, self.height // 2.285))
                    self.screen.blit(self.sett_pol, self.sett_pol_rect)
                    user.volume = 0
                if user.volume == 1:
                    self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 2.2429, self.height // 2.285))
                    self.screen.blit(self.sett_pol, self.sett_pol_rect)
                    user.volume = 0.5
                if user.volume == 1.5:
                    self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 2, self.height // 2.285))
                    self.screen.blit(self.sett_pol, self.sett_pol_rect)
                    user.volume = 1
                if user.volume == 2:
                    self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 1.804, self.height // 2.285))
                    self.screen.blit(self.sett_pol, self.sett_pol_rect)
                    user.volume = 1.5

        if self.sett_right_rect.collidepoint(self.mouse_pos):
            self.screen.blit(self.sett_right_up, self.sett_right_up_rect)
        if self.sett_right_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.button_right_press = True
        else:
            if self.button_right_press:
                self.button_right_press = False
                if user.volume == 1.5:
                    self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 1.6438, self.height // 2.285))
                    self.screen.blit(self.sett_pol, self.sett_pol_rect)
                    user.volume = 2
                if user.volume == 1:
                    self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 1.804, self.height // 2.285))
                    self.screen.blit(self.sett_pol, self.sett_pol_rect)
                    user.volume = 1.5
                if user.volume == 0.5:
                    self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 2, self.height // 2.285))
                    self.screen.blit(self.sett_pol, self.sett_pol_rect)
                    user.volume = 1
                if user.volume == 0:
                    self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 2.2429, self.height // 2.285))
                    self.screen.blit(self.sett_pol, self.sett_pol_rect)
                    user.volume = 0.5

    def scroll_cor(self, user):
        if user.volume == 2:
            self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 1.6438, self.height // 2.285))
            self.screen.blit(self.sett_pol, self.sett_pol_rect)
        if user.volume == 1.5:
            self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 1.804, self.height // 2.285))
            self.screen.blit(self.sett_pol, self.sett_pol_rect)
        if user.volume == 1:
            self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 2, self.height // 2.285))
            self.screen.blit(self.sett_pol, self.sett_pol_rect)
        if user.volume == 0.5:
            self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 2.2429, self.height // 2.285))
            self.screen.blit(self.sett_pol, self.sett_pol_rect)
        if user.volume == 0:
            self.sett_pol_rect = self.sett_pol.get_rect(center=(self.weight // 2.553, self.height // 2.285))
            self.screen.blit(self.sett_pol, self.sett_pol_rect)

    def menu_render(self, user, coin):
        self.screen.blit(self.bg_dark, (0, 0))
        self.draw_menu_button()
        self.start_game()
        self.sett_game(user, coin)
