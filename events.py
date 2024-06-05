import pygame
import random
from alchemist import Alchemist
from save import Save


class Events:

    def __init__(self, user):
        self.save = Save()
        self.volume = user.volume
        self.alchemist_app = pygame.USEREVENT + 1
        self.alchemist_del = pygame.USEREVENT + 2
        pygame.time.set_timer(self.alchemist_app, random.randint(150000, 300000))
        self.alchemist_spawn = False
        self.kill_value = False
        self.kill_count = 0

    def event_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def event_game(self, alchemists, user, sound):
        for event in pygame.event.get():
            self.event = event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                for alchemist_count in alchemists:
                    if alchemist_count.rect.collidepoint(x, y):
                        alchemist_count.kill()
                        sound.kill_sound(user)
                        self.kill_count += 1
                if self.kill_count == 5:
                    self.kill_value = True
                    self.kill_count = 0
            if event.type == pygame.QUIT:
                user.volume = self.volume
                self.save.save_game(user)
                exit()

    def make_alchemists(self, weight, height, screen, alchemists, user, sound):
        alchemists.update()
        alchemists.draw(screen)
        if self.event.type == self.alchemist_app and self.alchemist_spawn == False:
            self.alchemist_spawn = True
            for i in range(5):
                alchemist = Alchemist(weight, height)
                alchemists.add(alchemist)
            pygame.time.set_timer(self.alchemist_del, 5000)
            sound.timer_sound(user)
        if self.event.type == self.alchemist_del and self.alchemist_spawn == True:
            alchemists.empty()
            sound.fail_sound(user)
            self.alchemist_spawn = False
            pygame.time.set_timer(self.alchemist_app, random.randint(150000, 300000))
        if not alchemists and self.alchemist_spawn == True and self.kill_value == True:
            self.kill_value = False
            self.alchemist_spawn = False
            pygame.time.set_timer(self.alchemist_app, random.randint(150000, 300000))
            sound.timer.set_volume(0)
            sound.victory_sound(user)
            user.accum_user_event()
