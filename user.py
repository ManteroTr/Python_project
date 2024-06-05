import pygame
from sound import Sound


class User:
    def __init__(self):
        self.money = 0
        self.total_money = 0
        self.count = 1
        self.lvl = 0
        self.exp = 1
        self.click = 0
        self.multi_count = 1
        self.accum = 0
        self.multi_accum = 1
        self.skill1_cost = 20
        self.skill2_cost = 1500
        self.skill3_cost = 300
        self.skill4_cost = 1000
        self.weight = 1200
        self.height = 800
        self.volume = 1

    def settings(self, weight, height, volume):
        self.weight = weight
        self.height = height
        self.volume = volume

    def money_user(self, money):
        self.money += money
        self.total_money += money

    def count_user(self):
        if self.count >= 4:
            self.count += 2
        else:
            self.count += 1

    def multi_count_user(self):
        self.multi_count += 1

    def multi_accum_user(self):
        self.multi_accum += 1

    def accum_user(self):
        if self.accum >= 4:
            self.accum += 2
        else:
            self.accum += 1

    def accum_user_event(self):
        self.accum += 5

    def lvl_user(self):
        self.lvl += 1

    def exp_user(self, i):
        self.exp = i**2 * 10

    def click_user(self):
        self.click += 1

    def skill1_cost_user(self, skill1_cost):
        self.skill1_cost = skill1_cost

    def skill2_cost_user(self, skill2_cost):
        self.skill2_cost = skill2_cost

    def skill3_cost_user(self, skill3_cost):
        self.skill3_cost = skill3_cost

    def skill4_cost_user(self, skill4_cost):
        self.skill4_cost = skill4_cost
