import time

from player_classes import *
from turn_logic import *

def main():
    print(f"{BLUE}Зачарованный {GREEN}Лес{RESET}")
    print()
    writes_the_introduction()
    print()
    time.sleep(0.5)
    shows_all_heroes()
    print()
    hero_team = setup_hero_team(all_hero, hero_team_size)
    enemy_team = setup_enemy_team(all_enemies, enemy_team_size)
    print()
    show_stats(hero_team, enemy_team)
    print()
    #Проверка конца игры
    game_over, round_num = game_loop(hero_team, enemy_team)
    if game_over:
        print()
        time.sleep(0.5)
        shows_ending_stats(hero_team, enemy_team, round_num)
if __name__ == "__main__":
    main()