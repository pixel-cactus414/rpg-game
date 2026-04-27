from config import *
import random
import copy
import time

def get_number(prompt, min_val, max_val):
    """
    Запрашивает у пользователя число в заданном диапозоне.

    :param prompt: (str) Текст, который будет показан пользователю
    :param min_val: (int) Минимальное допустимое число
    :param max_val: (int) Максимальное допустимое число
    :return: (int) Введённое пользователем число в заданном диапозоне
    """
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            if min_val <= value <= max_val:
                return value
def get_alive_units(team):
    """
    Возвращает список живых юнитов из команды

    :param team: (list) Список словарей юнитов. У каждого юнита должен быть ключ hp
    :return: (list) Список юнитов с hp > 0. Если таких нет возвращает пустой список
    """
    alive_team = []
    for unit in team:
        if unit['hp'] > 0:
            alive_team.append(unit)
    return alive_team
def show_alive_enemies(enemy_team):
    """
    Выводит список живых врагов с нумерацией в консоль.

    :param enemy_team: (list) Список словарей врагов с ключами 'name', 'hp', 'max_hp'
    :return: (list) Список живых врагов для выбора цулью атаки. Если живых нет - возвращает пустой список
    """
    alive = get_alive_units(enemy_team)
    for i, enemy in enumerate(alive):
        print(f"{i+1}) {YELLOW}{enemy['name']}{RESET}: {RED}{enemy['hp']}/{enemy['max_hp']} HP{RESET}")
    return alive
def calculate_threat(unit):
    """
    Расчитывает уровень угрозы юнита для выбора цели атаки.

    Угроза зависит от:
        max_hp - чем бодьше, тем выше угроза
        threat - базовый уровень угрозы юнита
        модификатора текущего hp - чем ниже уровень, тем ниже угроза
    :param unit: (dict) Словарь юнита с ключами 'hp', 'max_hp', 'threat'
    :return: (float) Уровень угрозы (шанс стать целью атаки)

    :note: Снижение здоровья = снижение угрозы
        100-80% = 1.0
        80-30% = 1-0.5
        30% = 0.5
    """
    max_hp = unit['max_hp']
    hp = unit['hp']
    base_threat = unit['threat']
    percent_hp = hp / max_hp
    if percent_hp > 0.8:
        hp_modifier = 1.0
    elif percent_hp < 0.3:
        hp_modifier = 0.5
    else:
        hp_modifier = 1 - (0.8 - percent_hp)
    threat = max_hp * base_threat * hp_modifier
    return threat
def setup_hero_team(all_hero, team_size):
    """
    Собирает команду героев через выбор пользователя.

    :param all_hero: (list) Список доступных словарей героев
    :param team_size: (int) Количество возможных героев в команде
    :return: (list) Список выбранных словарей героев (без повторений)
    """
    team = []
    available_heroes = all_hero.copy()
    for j in range(team_size):
        print(f"{YELLOW}Выберите {j+1}/{team_size} героя {RESET}")
        for i in range(len(available_heroes)):
            hero = available_heroes[i]
            print(f"{YELLOW}{i+1}){RESET} {hero['icon']}  {GREEN}{hero['name']}{RESET}: {RED}{hero['max_hp']} HP{RESET}, {BLUE}{hero['damage']} DAMAGE{RESET}")
            skills = get_current_skills(hero)
            for skill in skills:
                print(f"{BLUE}{t_left}{line_h} {RED}{skill['name']}{RESET} = {skill['description']}")
        choice = get_number(f"{BLUE}Введите номер героя: {RESET}", 1, len(available_heroes))
        team.append(available_heroes.pop(choice - 1))
        print()
    return team
def setup_enemy_team(all_enemies, team_size):
    """
    Собирает команду врагов случайным образом.

    :param all_enemies: (list) Список доступных врагов.
    :param team_size: (int) Количество возможных врагов в команде.
    :return: (list) Список словарей случайных врагов.
    """
    team = []
    for _ in range(team_size):
        chosen = random.choice(all_enemies)
        team.append(copy.deepcopy(chosen))
    return team
def show_stats(hero_team, enemy_team):
    """
    Выводит в консоль текущую статистику боя
    Отображает:
        иконку; имя; полоски hp, mp, sh (если есть) для каждого героя
        имя; полоску hp для каждого врага

    :param hero_team: (list) Список словарей героев с ключами 'icon', 'name', 'hp', 'max_hp', 'mp', 'max_mp'
    :param enemy_team: (list) Список словарей врагов с ключами 'name', 'hp', 'max_hp'
    :return: None
    """
    print(f"{BLUE}{corner_tld}{line_hd * 38}{corner_trd}")
    print(f"{line_vd}{f'ТЕКУЩЕЕ СОСТОЯНИЕ:':^38}{line_vd}")
    print(f"{BLUE}{t_left}{line_hd * 38}{t_right}")
    for hero in hero_team:
        name_line = f"{hero['icon']}  {hero['name']} ({hero['crit_chance']}% crit):"
        print(f"{BLUE}{line_vd}{GREEN}{name_line:^20}{RESET}", end='')
        for effect in hero['effects']:
            print(f"{effect['icon']}", end=' ')
        print()
        print(f"{BLUE}{line_vd}{RESET}", end=" ")
        shows_hp_bar(hero)
        for effect in hero['effects']:
            if effect['type'] == "physical_shield":
                print(f"{BLUE}{line_vd}{RESET}", end=" ")
                shows_sh_bar(hero, effect)
        print(f"{BLUE}{line_vd}{RESET}", end=" ")
        shows_mp_bar(hero)
    print(f"{BLUE}{line_vd}{RESET}")
    for enemy in enemy_team:
        print(f"{BLUE}{line_vd}{RESET}", end=" ")
        print(f"{f'{YELLOW}{enemy['name']}{RESET}:':^30}", end=' ')
        for effect in enemy['effects']:
            print(f"{effect['icon']}", end=' ')
        print()
        print(f"{BLUE}{line_vd}{RESET}", end=" ")
        shows_hp_bar(enemy)
    print(f"{BLUE}{corner_dld}" + f"{line_hd}" * 38 + f"{corner_drd}{RESET}")
def shows_hp_bar(unit):
    """
    Выводит цветную полоску hp юнита в консоль

    :param unit: Словарь юнита с ключами 'hp', 'max_hp'
    :return: None

    :note: Цвет полоски зависит от процента hp:
        Зеленый: hp > 80%
        Жёлтый: 30-80% hp
        Красный: hp < 30%
    """
    length = int(unit['max_hp'] / 10)
    percent_hp = unit['hp'] / unit['max_hp']
    full_bar = int(percent_hp * max(length, 1))
    empty_bar = length - full_bar
    bar = full_bar_icon * full_bar + empty_bar_icon * empty_bar
    if percent_hp >= 0.8:
        color = GREEN
    elif 0.3 < percent_hp < 0.8:
        color = YELLOW
    else:
        color = RED
    print(f"{RED}HP: {color}{bar}{RESET} | {RED}{unit['hp']}/{unit['max_hp']}{RESET}")
def shows_mp_bar(unit):
    """
    Выводит цветную полоску mp юнита в консоль

    :param unit: (dict) Словарь юнита с ключами 'mp', 'max_mp'
    :return: None
    """
    length = int(unit['max_mp'] / 10)
    percent_mp = unit['mp'] / unit['max_mp']
    full_bar = int(percent_mp * max(length, 1))
    empty_bar = length - full_bar
    bar = full_bar_icon * full_bar + empty_bar_icon * empty_bar
    color = BLUE
    print(f"{BLUE}MP: {color}{bar}{RESET} | {BLUE}{unit['mp']}/{unit['max_mp']}{RESET}")
def shows_sh_bar(unit, effect):
    """
    Выводит полоску брони юнита.

    :param unit: (dict) Словарь юнита с ключом 'effects'
    :param effect: (dict) Словарь эффекта "броня" с ключом 'value'
    :return: None
    """
    lenght = int(effect['value'] / 10)
    bar = full_bar_icon * max(lenght, 1)
    print(f"{CYAN}SH: {bar}{RESET} | {CYAN}{effect['value']}{RESET}")
def is_game_over(enemy_team, hero_team):
    """
    Проверяет окончена ли игра (победа или поражение).
    Конец игры, если:
        все враги мертвы - победа
        все герои мертвы - поражение

    :param enemy_team: (list) Список словарей врагов
    :param hero_team: (list) Список словарей героев
    :return: (bool) True, если игра окончена (победа или поражение)
                    False, если игра продолжается
    """
    if not get_alive_units(enemy_team):
        print(f"{YELLOW}Победа! Противники повержены!{RESET}")
        return True
    if not get_alive_units(hero_team):
        print(f"{YELLOW}Поражение! Все герои пали{RESET}")
        return True
def revert_transform(hero):
    """
    Меняет форму героя Оборотень на 'human'.
    Сохраняет процент здоровья, меняет характеристики

    :param hero: (dict) Словарь героя использующего навык
    :return: None
    """
    form_data = hero['forms']["human"]
    hp_percent = hero['hp']/hero['max_hp']
    hero['max_hp'] = int(hero['base_max_hp'] * form_data['max_hp_mod'])
    hero['hp'] = int(max(hero['max_hp'] * hp_percent, 1))
    hero['damage'] = int(hero['base_damage'] * form_data['damage_mod'])
    hero['threat'] = hero['base_threat'] * form_data['threat_mod']
    hero['accuracy'] = hero['base_accuracy'] * form_data['accuracy_mod']
    hero['icon'] = form_data['icon']
    hero['skills'] = form_data['skills']
    hero['form'] = "human"
    hero['transform_timer'] = 0
    print(f"{GREEN}{hero['name']} {YELLOW}превращается в {BLUE}{"human"}!{RESET}")
    print(f"{RED}HP: {hero['hp']} / {hero['max_hp']}{RESET}")
def decrease_effects(team):
    """
    Уменьшает длительность активных эффектов юнитов и удаляет истёкшие.
    Эффекты с 'duration' > 0 уменьшаются на 1
    Эффекты с 'duration' = 0 удаляются
    Эффекты без 'duration' не обрабатываются (например щит)

    :param team: (list) Список словарей юнитов
    :return: None
    """
    for unit in team:
        expired_effects = []
        for i, effect in enumerate(unit['effects']):
            if 'duration' in effect and effect['duration'] > 0:
                effect['duration'] -= 1
                if effect['duration'] <= 0:
                    expired_effects.append(i)
                    print(f"Эффект {BLUE}{effect['name']}{RESET} у {YELLOW}{unit['name']}{RESET} закончился!")
                    time.sleep(0.3)
        for i in reversed(expired_effects):
            unit['effects'].pop(i)
        #Обратная трансформация оборотня
        if unit.get("transform_timer", 0) > 0:
            if unit['hp'] > 0:
                unit['transform_timer'] -= 1
                if unit['transform_timer'] == 0:
                    print(f"{YELLOW}Трансформация {GREEN}{unit['name']}{YELLOW} закончиоась!{RESET}")
                    revert_transform(unit)
def is_stunned(unit):
    """
    Проверяет оглушён ли юнит.

    :param unit: (dict) Словарь юнита с ключом 'effects'.
    :return: (bool) True если юнит оглушён.
                    False в противном случае.
    """
    for effect in unit['effects']:
        if effect['type'] == "stun" and effect['duration'] > 0:
            print(f"{YELLOW}{unit['name']} пропускает ход!{RESET}")
            print()
            return True
def get_current_skills(hero):
    """
    Возвращает список навыков текущей формы героя.
    У героев с 2 формами (werewolf) навыки зависят от текущей формы.
    У обычных героев навыки хранятся в 'skills'.

    :param hero: (dict) Словарь героя с ключом 'skills'
    :return: (list) Список словарей навыков
    """
    if "forms" in hero and hero['form'] in hero['forms']:
        return hero['forms'][hero['form']]['skills']
    return hero.get("skills", [])
def get_target(team):
    """
    Запрвшивает у пользователя выбор цели из списка живых врагов.
    Если живых врагов нет - возвращает None.
    Если жив один - возвращает его без запроса.
    Если несколько - выводит список и запрвшивает номер.

    :param team: (list) Список словарей врагов
    :return: (dict or None) Словарь выбранного героя, или None если целей нет
    """
    alive_enemies = show_alive_enemies(team)
    if not alive_enemies:
        return None
    elif len(alive_enemies) == 1:
        return alive_enemies[0]
    else:
        choice = get_number(f"{BLUE}Выберите цель: {RESET}", 1, len(alive_enemies))
        return alive_enemies[choice - 1]
def removing_invisibility(unit):
    # Проверка невидимости
    for i, effect in enumerate(unit['effects']):
        if effect['type'] == "shadow_mantle":
            unit['effects'].pop(i)
            print(f"{YELLOW}Невидимость {unit['name']} пропадает!")
            break