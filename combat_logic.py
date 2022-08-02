import time
import input_mapper
import main
import heroes
import enemys
import threading

currrent_hero = heroes.Paladin()
current_hero_enemy = False
respawn_cooldown = 1

desc = []


def summon_enemy():
    global respawn_cooldown
    respawn_cooldown -= 1
    if respawn_cooldown == 0:
        desc.insert(-1, enemys.SkeletonWarrior())
        respawn_cooldown = 10
        print((f'подкрепление, против тебя {len(desc)} еними'))



def check_target():
    if len(desc) > 0:
        current_hero_enemy = desc[0]
    if len(desc) == 0:
        current_hero_enemy = False
    return current_hero_enemy


def mainloop():
    global respawn_cooldown
    global currrent_hero
    global current_hero_enemy

    while True:

        time.sleep(1)
        if currrent_hero.dead == True:
            print('ты проиграл')
            break

        summon_enemy()
        current_hero_enemy = check_target()


        if current_hero_enemy:
            if current_hero_enemy.dead:
                desc.remove(desc[0])
                if desc:
                    current_hero_enemy = desc[0]
                else:
                    current_hero_enemy = False
            else:
                currrent_hero.time_tick(current_hero_enemy)
            if current_hero_enemy:
                if current_hero_enemy.dead != True:
                    for enemyes in desc:
                        enemyes.time_tick(currrent_hero)
