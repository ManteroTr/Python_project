import pygame
from save import Save


class Level:

    def __init__(self,  weight, height, screen, user):
        self.screen = screen
        self.weight = weight
        self.height = height
        self.volume = user.volume
        self.save = Save()
        self.mouse_pos = pygame.mouse.get_pos()
        self.level_view = pygame.transform.scale(pygame.image.load('image/lvl.png').convert_alpha(),
                                                 (self.weight // 8.1632, self.height // 2.4242))
        self.level_view_rect = self.level_view.get_rect(center=(self.weight // 1.0685, self.height // 4.8484))
        self.stat_menu = pygame.transform.scale(pygame.image.load('image/stat_menu.png').convert_alpha(),
                                                (self.weight // 8.1632, self.height // 3.2))
        self.stat_menu_rect = self.stat_menu.get_rect(center=(self.weight // 1.0685, self.height // 1.7582))
        self.stat_menu.set_alpha(228)
        self.button_sett = pygame.transform.scale(pygame.image.load('image/button.png').convert_alpha(),
                                                  (130, 60))
        self.button_sett_rect = self.button_sett.get_rect(center=(self.weight // 1.0685, 470))
        self.button_sett_up = pygame.transform.scale(pygame.image.load('image/button_up.png').convert_alpha(),
                                                     (130, 60))
        self.button_sett_up_rect = self.button_sett_up.get_rect(center=(self.weight // 1.0685, 470))
        self.button_sett_txt = pygame.font.Font(None, self.weight // 48).render('Звук Вкл', True, "#59FFA9")
        self.button_sett_txt_rect = self.button_sett_txt.get_rect(center=(self.weight // 1.0685, 470))
        self.button_sett_txt_off = pygame.font.Font(None, self.weight // 48).render('Звук Выкл', True, "#59FFA9")
        self.button_sett_txt_off_rect = self.button_sett_txt_off.get_rect(center=(self.weight // 1.0685, 470))
        self.button_sett_exit = pygame.transform.scale(pygame.image.load('image/button.png').convert_alpha(),
                                                  (130, 60))
        self.button_sett_exit_rect = self.button_sett.get_rect(center=(self.weight // 1.0685, 540))
        self.button_sett_exit_up = pygame.transform.scale(pygame.image.load('image/button_up.png').convert_alpha(),
                                                     (130, 60))
        self.button_sett_exit_up_rect = self.button_sett_up.get_rect(center=(self.weight // 1.0685, 540))
        self.exit_txt = pygame.font.Font(None, self.weight // 48).render('Выйти', True, "#59FFA9")
        self.exit_txt_rect = self.exit_txt.get_rect(center=(self.weight // 1.0685, 540))
        self.total_click = pygame.font.Font(None, self.weight // 48).render(f'Clicks: {user.click}', True, "#59FFA9")
        self.total_moneys = pygame.font.Font(None, self.weight // 48).render(f'Tot mon: {user.total_money}',
                                                                             True, "#59FFA9")
        self.stat_open = False
        self.stat_open_cor = False
        self.volume_off = False
        self.volume_on = True
        self.sett_open = False
        self.sett_exit = False
        self.close_sound = False


    def draw_lvl(self, user):
        self.screen.blit(self.level_view, self.level_view_rect)
        self.level = pygame.font.Font(None, self.weight // 24).render(f'{user.lvl}', True, "#59FFA9")
        self.level_rect = self.level.get_rect(center=(self.weight // 1.0695, self.height // 8))
        self.screen.blit(self.level, self.level_rect)
        self.exp = pygame.font.Font(None, self.weight // 48).render(f'{user.exp - user.click} exp', True, "#59FFA9")
        self.exp_rect = self.exp.get_rect(center=(self.weight // 1.0695, self.height // 4.324))
        self.screen.blit(self.exp, self.exp_rect)

    def lvl_up(self, user, sound):
        if user.exp == user.click:
            sound.lvlup_sound(user)
            user.lvl_user()
        for i in range(1, 99):
            if user.lvl == i:
                user.exp_user(i)

    def draw_stat_menu(self, user, sound):
        self.mouse_pos = pygame.mouse.get_pos()
        if (self.level_view_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]
                and self.stat_open == False):
            sound.level_sound(user)
            if (self.stat_menu_rect.collidepoint(self.mouse_pos) and pygame.mouse.get_pressed()[0]
                    and self.stat_open_cor == False):
                self.stat_open_cor = True
            self.stat_open = True
            self.close_sound = True
        else:
            if self.stat_open:
                self.screen.blit(self.stat_menu, self.stat_menu_rect)
                self.total_click = pygame.font.Font(None, self.weight // 48).render(f'Clicks: {user.click}', True,
                                                                                    "#59FFA9")
                self.screen.blit(self.total_click, (1060, 340))
                self.total_moneys = pygame.font.Font(None, self.weight // 48).render(f'Tot mon: {user.total_money}',
                                                                                     True, "#59FFA9")
                self.screen.blit(self.total_moneys, (1060, 370))
                self.screen.blit(self.button_sett_exit, self.button_sett_exit_rect)
                self.screen.blit(self.exit_txt, self.exit_txt_rect)
                self.screen.blit(self.button_sett, self.button_sett_rect)
                self.save_exit_game(user)
                if self.volume_on:
                    self.screen.blit(self.button_sett_txt, self.button_sett_txt_rect)
                else:
                    self.screen.blit(self.button_sett_txt_off, self.button_sett_txt_off_rect)
                self.sett_game_lev(user)
                if (pygame.mouse.get_pressed()[0] and not self.level_view_rect.collidepoint(self.mouse_pos)
                        and not self.stat_menu_rect.collidepoint(self.mouse_pos)):
                    if self.close_sound:
                        self.close_sound = False
                        sound.level_sound(user)
                    self.stat_open = False

    def save_exit_game(self, user):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.button_sett_exit_rect.collidepoint(self.mouse_pos):
            self.screen.blit(self.button_sett_exit_up, self.button_sett_exit_up_rect)
            self.screen.blit(self.exit_txt, self.exit_txt_rect)
            if pygame.mouse.get_pressed()[0]:
                self.sett_exit = True
            else:
                if self.sett_exit:
                    self.sett_exit = False
                    user.volume = self.volume
                    self.save.save_game(user)
                    exit()

    def sett_game_lev(self, user):
        self.mouse_pos = pygame.mouse.get_pos()
        if self.button_sett_rect.collidepoint(self.mouse_pos) and self.volume_on == True:
            self.screen.blit(self.button_sett_up, self.button_sett_up_rect)
            self.screen.blit(self.button_sett_txt, self.button_sett_txt_rect)
            if pygame.mouse.get_pressed()[0]:
                self.sett_open = True
            else:
                if self.sett_open:
                    self.volume_on = False
                    self.volume_off = True
                    user.volume = 0
                    self.sett_open = False
        if self.button_sett_rect.collidepoint(self.mouse_pos) and self.volume_off == True:
            self.screen.blit(self.button_sett_up, self.button_sett_up_rect)
            self.screen.blit(self.button_sett_txt_off, self.button_sett_txt_off_rect)
            if pygame.mouse.get_pressed()[0]:
                self.sett_open = True
            else:
                if self.sett_open:
                    self.volume_off = False
                    self.volume_on = True
                    user.volume = self.volume
                    self.sett_open = False
