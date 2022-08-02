import heroes
import combat_logic


def input_logic():
    input_string = 0
    while True:
        try:
            input_string = input().lower()
        except EOFError:
            pass

        if input_string == 'flask':
            combat_logic.currrent_hero.flask()

# def attack():
#     main.char.time_tick(main.char)
#     for enemyes in combat_logic.desc:
#         enemyes.time_tick(combat_logic.currrent_hero)
#     if combat_logic.current_hero_enemy:
#         if not combat_logic.current_hero_enemy.dead:
#             combat_logic.currrent_hero.attack(combat_logic.currrent_hero, combat_logic.current_hero_enemy)
#
# input_map ={'attack': attack()}
#
# def input_wait(input):
#     input_map[input]()
