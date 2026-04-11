from player_classes import *
from turn_logic import *

def main():
    print(f"{BLUE}Игра. Соберите команду героев и сразите монстров!{RESET}")
    print()
    code = input("Введите код: ")
    if code == "+":
        all_hero.extend(secret_heroes)
    hero_team = setup_hero_team(all_hero, hero_team_size)
    enemy_team = setup_enemy_team(all_enemies, enemy_team_size)
    show_stats(hero_team, enemy_team)
    print()
    #Проверка конца игры
    game_over, round_num = game_loop(hero_team, enemy_team)
    if game_over:
        print()
        time.sleep(0.5)
        print(f"{BLUE}" + f"{line_hd}" * 40)
        print(f"{'ИГРА ОКОНЧЕНА':^40}")
        print(f"{line_hd}" * 40 + f"{RESET}")
        print(f"{BLUE}{f'ВСЕГО РАУНДОВ: {round_num}':^40}{RESET}")
        show_stats(hero_team, enemy_team)
if __name__ == "__main__":
    main()