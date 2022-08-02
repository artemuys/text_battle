import random


class Paladin:
    def __init__(self):
        self.is_alive = True
        self.name = 'Васян ярость света'
        self.dead = False
        self.dmg = 30
        self.max_hp = 200
        self.current_hp = 200
        self.attack_cd = 0
        self.flask_cooldown = 0
        self.target = False
        self.killing_spree = 0
        self.amount_of_flasks = 2


    def attack(self, enemy):
        if self.attack_cd == 0:
            self.attack_cd = 3
            crit_chance = random.randint(0, 10)
            if crit_chance > 5:
                enemy.current_hp = enemy.current_hp - self.dmg
                print('ты попал, у врага ' + str(enemy.current_hp) + 'хп')

                return
            if crit_chance > 3:
                enemy.current_hp = enemy.current_hp - self.dmg * 2
                print(f'ты кританул, у врага {enemy.current_hp}')
            else:
                print('ты промахнулся')
                pass
        if enemy.current_hp <= 0:
            enemy.dead = True
            enemy.dmg = 0
            self.killing_spree += 1
            print(f'killing spree {self.killing_spree}')

    def flask(self):
        if self.amount_of_flasks <= 0:
            print('фласок нет')
        if self.flask_cooldown > 0:
            print('фласка на кд')
        if self.amount_of_flasks > 0 and self.flask_cooldown == 0:

            self.amount_of_flasks -= 1
            self.flask_cooldown = 3
            if self.current_hp + 50 < 200:
                self.current_hp = self.current_hp + 50
            if self.current_hp + 50 >= 200:
                self.current_hp = 200
            print(f'полечился теперь у тебя {self.current_hp}')


    def time_tick(self, target = False):
        if self.attack_cd > 0:
            self.attack_cd -= 1
        if self.flask_cooldown > 0:
            self.flask_cooldown -= 1
        if target:
            self.attack(target)




