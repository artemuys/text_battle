class SkeletonWarrior:



    def __init__(self):
        self.is_alive = True
        self.name = 'name'
        self.dead = False
        self.dmg = 15
        self.max_hp = 50
        self.current_hp = 50
        self.attack_is_ready = 0

    def attack(self, enemy):
        enemy.current_hp = enemy.current_hp - self.dmg
        print(f'тебя пизданули у тебя {enemy.current_hp}')
        if enemy.current_hp <= 0:
            enemy.dead = True

    def time_tick(self, target = False):
        if self.attack_is_ready > 0:
            self.attack_is_ready -= 1

        if target and self.attack_is_ready == 0:
            self.attack_is_ready = 5
            if not target.dead:
                self.attack(target)


