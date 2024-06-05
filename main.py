import pygame
from coin import Coin
from shop import Shop
from events import Events
from user import User
from level import Level
from sound import Sound
from str_menu import Menu
from save import Save
save = Save()
save.load_game()
user = save.load_game()
if user == None:
    user = User()


def run_menu():
    pygame.init()
    weight = user.weight
    height = user.height
    pygame.display.set_caption("Alchemist`s clicker")
    screen = pygame.display.set_mode((weight, height))
    pygame.display.set_icon(pygame.image.load('image/ability5.jpg'))
    clock = pygame.time.Clock()

    sound = Sound()
    coin = Coin(weight, height, screen)
    menu = Menu(weight, height, screen)
    events = Events(user)
    sound.bg_sound(user)

    while True:
        screen.blit(pygame.transform.scale(pygame.image.load('image/fon.jpg').convert(), (weight, height)),
                    (0, 0))
        events.event_menu()
        coin.rotating()
        menu.menu_render(user, coin)
        pygame.mixer.music.set_volume(user.volume / 20.0)
        if user.weight != weight:
            weight = user.weight
            height = user.height
            screen = pygame.display.set_mode((weight, height))
        if menu.play:
            run_game()
        pygame.display.update()
        clock.tick(60)


def run_game():
    pygame.init()
    weight = user.weight
    height = user.height
    pygame.display.set_caption("Alchemist`s clicker")
    screen = pygame.display.set_mode((weight, height))
    clock = pygame.time.Clock()
    pygame.display.set_icon(pygame.image.load('image/ability5.jpg'))

    sound = Sound()
    sound.bg_sound(user)
    coin = Coin(weight, height, screen)
    shop = Shop(weight, height, screen)
    level = Level(weight, height, screen, user)
    events = Events(user)
    alchemists = pygame.sprite.Group()

    while True:
        screen.blit(pygame.transform.scale(pygame.image.load('image/fon.jpg').convert(), (weight, height)),
                    (0, 0))
        events.event_game(alchemists, user, sound)
        coin.coin_render(user, sound, level)
        shop.draw_shop(user, sound)
        level.draw_lvl(user)
        level.draw_stat_menu(user, sound)
        pygame.mixer.music.set_volume(user.volume / 20.0)
        events.make_alchemists(weight, height, screen, alchemists, user, sound)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    run_menu()
