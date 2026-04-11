from combat import *
from skills import *
from utils import *
from config import *
import time

def shows_hero_status(hero):
    """
    Выводит статистику героя и действия в консоль во время его хода.
    Показывает:
        иконку и имя героя
        полоски здоровья, маны
        урон базовой атаки
        навыки и их описание

    :param hero: (dict) Словарь героя с ключами 'icon', 'name', 'damage', 'effects'
    :return: None
    """
    print(f"{BLUE}Ход героя {hero['icon']} {GREEN}{hero['name']}{BLUE}:{RESET}", end=' ')
    for effect in hero['effects']:
        print(f"{effect['icon']}", end=' ')
    print()
    shows_hp_bar(hero)
    shows_mp_bar(hero)
    damage_val = hero['damage']
    color = RED
    for effect in hero['effects']:
        if effect['type'] == "damage_boost":
            damage_val = int(hero['damage'] * effect['value'])
            color = YELLOW
    print(f"{YELLOW}1){RESET} Атака == {color}{damage_val} {RED}damage{RESET}")
    skills = get_current_skills(hero)
    for i, skill in enumerate(skills, start=2):
        mana_color = GREEN if hero['mp'] >= skill['mana_cost'] else RED
        print(f"{YELLOW}{i}){RESET} {skill['name']} [{mana_color}{skill['mana_cost']} MP{RESET}] == {skill['description']}")
def get_hero_action(hero, hero_team, enemy_team):
    """
    Запрашивает у пользователя действие героя (атака или навык)
    Пользователь вводит номер действия:
        1 - атака
        2, 3 - навык
    Проверяет наличие маны для навыка. Если не хватает - повторяет запрос

    :param hero: (dict) Словарь текущего героя
    :param hero_team: (list) Список героев
    :param enemy_team: (list) Список врагов
    :return: (bool) True если игра окончена (убийство последнего врага)
                    False если ход завершён нормально
    """
    skills = get_current_skills(hero)
    while True:
        action = get_number(f"{BLUE}Введите номер действия: {RESET}", 1, len(get_current_skills(hero)) + 1)
        #АТАКА
        if action == 1:
            return process_hero_attack(hero, enemy_team)
        #НАВЫК
        elif action in range(2, len(skills) + 2):
            skill_index = action - 2
            skill = skills[skill_index]
            if hero['mp'] < skill['mana_cost']:
                print(f"{RED}Недостаточно маны!{RESET}")
                continue
            activate_skill(hero, hero_team, enemy_team, skill_index)
            print()
            if not get_alive_units(enemy_team):
                return True
            return False
def process_heroes_turn(hero_team, enemy_team):
    """
    Обрабатывает ход всех живых героев.
    Каждый героей:
        проверяется на оглушение
        выводится его статистика (hp, mp, навыки)
        запрашивается действие (атака, навык)

    :param hero_team: (list) Список словарей героев
    :param enemy_team: (list) Список словарей врагов
    :return: (bool) True если игра окончена (убийство последнего врага)
                    False если ход завершён нормально
    """
    for hero in hero_team:
        if hero['hp'] <= 0:
            continue
        if is_stunned(hero):
            continue
        shows_hero_status(hero)
        action = get_hero_action(hero, hero_team, enemy_team)
        #Если действие завершило игру
        if action:
            return True
    return False
def process_enemies_turn(enemy_team, hero_team):
    """
    Обрабатывает ход всех живых врагов.
    Каждый враг:
        проверяется на оглушение
        атакует случайного героя

    :param enemy_team: (list) Список словарей врагов
    :param hero_team: (list) Список словарей героев
    :return: (bool) True если игра окончена (умер последний герой)
                    False если ход завершился нормально
    """
    for enemy in get_alive_units(enemy_team):
        if enemy['hp'] > 0:
            print(f"{BLUE}Ход противника {YELLOW}{enemy['name']}{BLUE}:{RESET}")
            if is_stunned(enemy):
                continue
            if process_enemy_attack(enemy, hero_team):
                return True
            time.sleep(0.5)
    return False
def process_round_end(hero_team, enemy_team, round_num):
    """
    Обрабатывает завершение раунда:
        снимает эффекты
        выводит статистику в консоль
        увеличивает счётчик раундов

    :param hero_team: (list) Список словарей героев
    :param enemy_team: (list) Список словарец врагов
    :param round_num: (int) Номер текущего раунда
    :return: (int) Номер следующего раунда
    """
    decrease_effects(hero_team)
    decrease_effects(enemy_team)
    print()
    time.sleep(0.5)
    show_stats(hero_team, enemy_team)
    round_num += 1
    print()
    return round_num
def game_loop(hero_team, enemy_team):
    """
    Главный игровой цикл.
    Каждый раунд:
        проверяет условия победы / поражения
        обрабатывает ход героев
        обрабатывает ход врагов
        завершает раунд (снимает эффекты, обновляет статистику)

    :param hero_team: (list) Список словарей героев
    :param enemy_team: (list) Список словарей врагов
    :return:
            game_over (bool) - True если игра окончена
            round_num (int) -Номер последнего раунда
    """
    round_num = 1
    while True:
        if is_game_over(enemy_team, hero_team):
            return True, round_num
        time.sleep(0.5)
        print(f"{BLUE}{f'РАУНД {round_num}!':^38}{RESET}")
        if process_heroes_turn(hero_team, enemy_team):
            return True, round_num
        time.sleep(0.3)
        print(f"{YELLOW}{f'ХОД ВРАГОВ':^38}{RESET}")
        time.sleep(0.7)
        if process_enemies_turn(enemy_team, hero_team):
            return True, round_num
        round_num = process_round_end(hero_team, enemy_team, round_num)