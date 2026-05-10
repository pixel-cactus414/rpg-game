import random
from idlelib.configdialog import changes

from utils import *
import time

def deal_damage(unit, target, damage):
    """
    Наносит урон от атакующего к цели атаки
    Учитывает:
        баффы увеличения урона (damage_boost)
        баффы защиты (physical_shield)
        восстанавливает ману атакующего при атаке

    :param unit: (dict) Словарь атакующего с ключами 'damage', 'effects', 'mp', 'max_mp'
    :param target: (dict) Словарь цели атаки с ключами 'hp', 'effects'
    :return: (bool) True если цель умерла после атаки
                    False если цуль осталась жива
    """
    expired = []
    for i, effect in enumerate(unit['effects']):
        #Проверка эффекта "Увеличение урона" у атакующего
        if effect['type'] == "damage_boost":
            damage *= effect['value']
            damage = int(damage)
            effect['charges'] -= 1
            #Удаление эффекта, если заряжы закончились
            if effect['charges'] == 0:
                expired.append(i)
        #Проверка невидимости у атакующего
        if effect['type'] == "shadow_mantle":
            expired.append(i)
            print(f"{YELLOW}Невидимость {unit['name']} пропадает!")
    for i in reversed(expired):
        unit['effects'].pop(i)
    #Проверка эффектов у цели атаки
    for i, effect in enumerate(target['effects']):
        #Проверка щита
        if effect['type'] == "physical_shield":
            damage = break_shield(unit, damage, target, i)
            if damage == 0:
                return False
        #Проверка невидимости
        if effect['type'] == "shadow_mantle":
            target['effects'].pop(i)
            print(f"{YELLOW}Невидимость {target['name']} пропадает!")
    #Нанесение урона
    target['hp'] -= damage
    print(f"{GREEN}{unit['name']}{RESET} наносит {RED}{damage}{RESET} урона!")
    died = target['hp'] <= 0
    if died:
        print(f"{BLUE}{target['name']} повержен!{RESET}")
        time.sleep(1)
    return died
def break_shield(unit, damage, target, effect_index):
    """
    Обрабатывает поглощение урона щитом:
        если щит мощнее урона - снижает прочность
        если урон мощнее щита - разрушает щит и возвращает остаток урона

    :param unit: (dict) Словарь атакующего с ключами 'damage', 'name'
    :param damage: (int) Урон атакующего
    :param target: (dict) Словарь цели атаки с ключами 'effects', 'name'
    :param effect_index: (int) Индекс эффекта щита в списке target['effects']
    :return: (int) Остаток урона после щита
    """
    effect = target['effects'][effect_index]
    shield = effect['value']
    if shield > damage:
        effect['value'] -= damage
        print(f"{YELLOW}Урон заблокирован!{RESET}")
        return 0
    else:
        excess_damage = damage - shield
        print(f"{YELLOW}Щит разрушен!{RESET}")
        target['effects'].pop(effect_index)
        return excess_damage
def process_hero_attack(hero, enemy_team):
    """
    Обрабатывает атаку героя.

    :param hero: (dict) Словарь героя
    :param enemy_team: (list) Список словарей врагов
    :return: (bool) True если все враги враги мертвы
                    False если остались живые враги
    """
    target = get_target(enemy_team)
    if target is None:
        return False
    print(f"{GREEN}{hero['name']}{RESET} атакует {YELLOW}{target['name']}{RESET}:")
    #Проверка шанса попасть по цели
    hit_chance = int(hero['accuracy'])
    if random.randint(1, 100) > hit_chance:
        print(f"{YELLOW}Промах!{RESET}")
        print()
        return False
    #Настройка разброса урона
    damage_variance = random.uniform(-0.1, 0.1)
    damage = round(hero['damage'] * (1 + damage_variance))
    damage = max(1, int(damage))
    #Проверка критического удара
    if random.randint(1, 100) <= hero['crit_chance']:
        print(f"{YELLOW}Крит! {RESET}", end=' ')
        damage = int(damage * 1.5)
        if hero['crit_chance'] != hero['basic_crit_chance']:
            hero['crit_chance'] = hero['basic_crit_chance']
    #Нанесение урона
    deal_damage(hero, target, damage)
    removing_invisibility(hero)
    if hero['mp'] < hero['max_mp']:
        hero['mp'] = min(hero['mp'] + 15, hero['max_mp'])
    if not get_alive_units(enemy_team):
        print(f"Все враги мертвы!")
        return True
    print()
    return False
def process_enemy_attack(enemy, hero_team):
    """
    Обрабатывает атаку врага.

    :param enemy: (dict) Словарь врага
    :param hero_team: (list) Список словарей героев
    :return: (bool) True если все враги враги мертвы
                    False если остались живые враги
    """
    target = choose_target(hero_team)
    if not target:
        return False
    print(f"{YELLOW}{enemy['name']}{RESET} атакует {GREEN}{target['name']}{RESET}:")
    deal_damage(enemy, target, enemy['damage'])
    if not get_alive_units(hero_team):
        print(f"{YELLOW}Все герои мертвы!{RESET}")
        return True
    print()
    return False
def choose_target(hero_team):
    """
    Выбирает цель для атаки врага.
    Приоритеты:
        герои с эффектом провокации - 'taunt'
        герои по системе угроз

    :param hero_team: (list) Список словарей героев
    :return: (dict) Словарь выбранного героя (цель для атаки)
    """
    taunt_heroes = []
    for unit in get_alive_units(hero_team):
        for effect in unit['effects']:
            if effect['type'] == "taunt" and effect['duration'] > 0 and unit['hp'] > 0:
                taunt_heroes.append(unit)
                break
    if taunt_heroes:
        target = random.choice(taunt_heroes)
        return target

    alive_heroes = get_alive_units(hero_team)
    visible_heroes = []
    for hero in alive_heroes:
        is_visible = True
        for effect in hero['effects']:
            if effect['type'] == "shadow_mantle":
                is_visible = False
                break
        if is_visible:
            visible_heroes.append(hero)

    if visible_heroes:
        threats = []
        for hero in visible_heroes:
            threats.append(calculate_threat(hero))
        total = sum(threats)
        chances = []
        for t in threats:
            chances.append(t / total)
        return random.choices(visible_heroes, weights=chances)[0]
    if alive_heroes:
        return random.choice(alive_heroes)
    return None
