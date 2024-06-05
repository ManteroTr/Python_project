import pygame


class Sound:

    def __init__(self):
        self.click_sound = pygame.mixer.Sound('sound/money_click.mp3')
        self.lvl_sound = pygame.mixer.Sound('sound/lvlup.mp3')
        self.open_shop_sound = pygame.mixer.Sound('sound/shop_open.mp3')
        self.close_shop_sound = pygame.mixer.Sound('sound/shop_close.mp3')
        self.buy_shop_sound = pygame.mixer.Sound('sound/buy.mp3')
        self.no_money = pygame.mixer.Sound('sound/no_money.mp3')
        self.open_level_sound = pygame.mixer.Sound('sound/open_level.mp3')
        self.victory = pygame.mixer.Sound('sound/victory.mp3')
        self.fail = pygame.mixer.Sound('sound/fail.mp3')
        self.timer = pygame.mixer.Sound('sound/timer_alchem.mp3')
        self.kill = pygame.mixer.Sound('sound/alchem_kill.mp3')

    def bg_sound(self, user):
        pygame.mixer.music.load('sound/forest_bg.mp3')
        pygame.mixer.music.set_volume(user.volume / 20.0)
        pygame.mixer.music.play(-1)

    def money_sound(self, user):
        self.click_sound.set_volume(user.volume / 3.33)
        self.click_sound.play()

    def lvlup_sound(self, user):
        self.lvl_sound.set_volume(user.volume / 2.0)
        self.lvl_sound.play()

    def open_sound(self, user):
        self.open_shop_sound.set_volume(user.volume / 5.0)
        self.open_shop_sound.play()

    def close_sound(self, user):
        self.close_shop_sound.set_volume(user.volume / 5.0)
        self.close_shop_sound.play()

    def buy_sound(self, user):
        self.buy_shop_sound.set_volume(user.volume / 5.0)
        self.buy_shop_sound.play()

    def no_money_sound(self, user):
        self.no_money.set_volume(user.volume / 10.0)
        self.no_money.play()

    def level_sound(self, user):
        self.open_level_sound.set_volume(user.volume / 6.0)
        self.open_level_sound.play()

    def victory_sound(self, user):
        self.victory.set_volume(user.volume / 5.0)
        self.victory.play()

    def fail_sound(self, user):
        self.fail.set_volume(user.volume / 5.0)
        self.fail.play()

    def timer_sound(self, user):
        self.timer.set_volume(user.volume / 5.0)
        self.timer.play()

    def kill_sound(self, user):
        self.kill.set_volume(user.volume / 5.0)
        self.kill.play()
