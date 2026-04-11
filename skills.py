from combat import deal_damage
from config import *
from effects import *
from utils import *
#Воин
def skill_execution(hero, enemy_team, skill):
    """
    Навык Воина "Яростный взмах": наносит мощный удар врагу, при убийстве мана не расходуется

    :param hero: (dict) Словарь героя, использующего навык
    :param enemy_team: (list) Спиоок словарей врагов
    :param skill: (dict) Словарь навыка с ключами 'value' (урон), 'mana_cost'
    :return: None
    """
    target = get_target(enemy_team)
    if target is None:
        return False
    damage = skill['value']
    target['hp'] = target['hp'] - damage
    print(f"{GREEN}{hero['name']}{RESET} наносит {RED}{damage}{RESET} урона {YELLOW}{target['name']}{RESET}")
    if target['hp'] <= 0:
        print(f"{YELLOW}{target['name']} повержен!{RESET}")
        return
    hero['mp'] -= skill['mana_cost']
def skill_boost_damage(hero, hero_team, skill):
    """
    Навык воина "Боевой клич": временно увеличивает урон базовой атаки всех союзников (добавляет эффект 'damage_boost')

    :param hero: (dict) Словарь героя, использующего навык
    :param hero_team: (list) Список словарей врагов
    :param skill: (dict) Словарь навыка героя
    :return: None
    """
    alive_heroes = get_alive_units(hero_team)
    if not alive_heroes:
        return
    effect = effects_list['damage_boost'].copy()
    effect['charges'] = skill['charges']
    effect['value'] = skill['value']
    for unit in alive_heroes:
        if unit != hero:
            unit['effects'].append(effect.copy())
    hero['mp'] -= skill['mana_cost']
    print(f"{GREEN}{hero['name']}{RESET} использует {YELLOW}{skill['name']}{RESET}")
#Лучница
def skill_arrow_rain(hero, enemy_team, skill):
    """
    Навык лучницы "Град стрел": наносит урон всем врагам.
    Количество стрел зависит от:
        количества маны - каждая стрела стоит ману
        количества целей- по одной стреле на цель

    :param hero: (dict) Словарь героя использующего навык
    :param enemy_team: (list) Список словарей врагов
    :param skill: (dict) Словарь навыка героя
    :return: None
    """
    alive_enemies = get_alive_units(enemy_team)
    if not alive_enemies:
        return
    shots_by_mp = hero['mp'] // skill['mana_cost']
    skill_shots = min(shots_by_mp, len(alive_enemies))
    if skill_shots == 0:
        return
    hero['mp'] -= skill_shots * skill['mana_cost']
    for enemy in alive_enemies[0:skill_shots]:
        enemy['hp'] -= skill['value']
        print(f"{GREEN}{hero['name']}{RESET} наносит {RED}{skill['value']}{RESET} урона {YELLOW}{enemy['name']}{RESET}")
        if enemy['hp'] <= 0:
            print(f"{YELLOW}{enemy['name']} повержен!{RESET}")
def hunter_hunters_mark():
    pass
#Паладин
def skill_taunt(skill, hero):
    """
    Навык паладина "Провокация": заставляет всех врагов атаковать только этого героя.

    :param skill: (dict) Словарь навыка
    :param hero: (dict) Словарь героя использующего навык
    :return: None
    """
    effect = effects_list['taunt'].copy()
    effect['duration'] = skill['duration']
    hero['effects'].append(effect)
    hero['mp'] -= skill['mana_cost']
    print(f"{GREEN}{hero['name']}{RESET} использует {YELLOW}{skill['name']}{RESET}")
def skill_shield(skill, hero, hero_team):
    """
    Навык паладина "Щит веры": добавляет эффект 'physical_shield' в ключ 'effects' выбранного героя.

    :param skill: (dict) Словарь навыка
    :param hero: (dict) Словарь героя
    :param hero_team: (list) Список словарей союзных героев
    :return:
    """
    target = get_target(hero_team)
    if target is None:
        return False
    for effect in target['effects']:
        if effect['type'] == "physical_shield":
            effect['value'] += skill['value']
            print(f"{YELLOW}Щит {GREEN}{target['name']} {YELLOW}усилен!")
            hero['mp'] -= skill['mana_cost']
            return True
    new_shield = effects_list['physical_shield'].copy()
    new_shield['value'] = skill['value']
    target['effects'].append(new_shield)
    hero['mp'] -= skill['mana_cost']
    print(f"{GREEN}{target['name']}{YELLOW} получает щит!{RESET}")
#Берри
def skill_instant_heal(hero, hero_team, skill):
    """
    Навык "Аптечка": мгновенно восстанавливает 'hp' героя на фиксированное значение.

    :param hero: (dict) Словарь героя использующего навык
    :param hero_team: (list) Список словарей союзных героев
    :param skill: (dict) Словарь навыка с ключами 'mana_cost', 'value'
    :return: None
    """
    available_targets = []
    for member in hero_team:
        if 0 < member['hp'] < member['max_hp']:
            available_targets.append(member)
    if not available_targets:
        print(f"{YELLOW}Все союзники целые!{RESET}")
        return
    for i, target in enumerate(available_targets, 1):
        print(f"{i}) {target['name']}")
        shows_hp_bar(target)
    choice = get_number(f"{YELLOW}Введите номер цели для исцеления: {RESET}", 1, len(available_targets))
    heal_target = available_targets[choice - 1]
    heal_power = skill['value']
    hero['mp'] -= skill['mana_cost']
    heal_target['hp'] = min(heal_target['max_hp'], heal_target['hp'] + heal_power)
    print(f"{GREEN}{hero['name']}{RESET} исцеляет {GREEN}{heal_target['name']}{RESET} на {RED}{heal_power} HP!{RESET}")
def skill_stun(hero, enemy_team, skill):
    """
    Навык "Оглушение": оглушает выбранного врага.

    :param hero: (dict) Словарь героя использующего навык
    :param enemy_team: (list) Список словарей врагов
    :param skill: (dict) Словарь навыка
    :return: None
    """
    effect = effects_list['stun'].copy()
    effect['duration"'] = skill['duration']
    target = get_target(enemy_team)
    if target is None:
        return False
    target['effects'].append(effect)
    hero['mp'] -= skill['mana_cost']
    print(f"{YELLOW}{target['name']} оглушен на {effect['duration']} ход!{RESET}")
#Оборотень
def skill_transform(hero, target_form, duration=0):
    """
    Навык оборотня "Подавленная ярость": меняет форму героя Оборотень на 'wolf'.
    Сохраняет процент здоровья, меняет характеристики

    :param hero: (dict) Словарь героя использующего навык
    :param target_form: (str) Название формы героя для перевоплощения
    :param duration: (int) Число ходов сколько длится перевоплощение
    :return: None
    """
    if hero['form'] == target_form:
        return
    form_data = hero['forms'][target_form]
    hp_percent = hero['hp']/hero['max_hp']
    hero['max_hp'] = int(hero['base_max_hp'] * form_data['max_hp_mod'])
    hero['hp'] = int(max(hero['max_hp'] * hp_percent, 1))
    hero['damage'] = int(hero['base_damage'] * form_data['damage_mod'])
    hero['threat'] = hero['base_threat'] * form_data['threat_mod']
    hero['accuracy'] = hero['base_accuracy'] * form_data['accuracy_mod']
    hero['icon'] = form_data['icon']
    hero['skills'] = form_data['skills']
    hero['form'] = target_form
    hero['transform_timer'] = duration
    print(f"{GREEN}{hero['name']} {YELLOW}превращается в {BLUE}{target_form}!{RESET}")
    print(f"{RED}HP: {hero['hp']} / {hero['max_hp']}{RESET}")
def skill_berserk (hero, enemy_team, skill):
    """
    Навык "Жажда крови": герой атакует противника, урон увеличивается с потерей hp.

    :param hero: (dict) Словарь героя использующего навык
    :param enemy_team: (list) Список словарей противников
    :param skill: (dict) Словарь навыка
    :return: None
    """
    target = get_target(enemy_team)
    if not target:
        return
    damage_percent = (hero['max_hp'] - hero['hp']) / hero['max_hp']
    bonus = damage_percent * 1.5
    damage = int(skill['value'] * (1 + bonus))
    deal_damage(hero, target, damage)
    hero['mp'] -= skill['mana_cost']
def skill_vampire_byte(hero, enemy_team, skill):
    """
    Навык "Жажда крови": наносит урон врагу и исцеляет героя.

    :param hero: (dict) Словварь героя использующего навык
    :param enemy_team: (list) Список словарей врагов
    :param skill: (dict) Словарь навыка
    :return: None
    """
    target = get_target(enemy_team)
    if not target:
        return
    damage = skill['value']
    deal_damage(hero, target, damage)
    heal = int(skill['value'] * 0.85)
    hero['hp'] = min(hero['max_hp'], hero['hp'] + heal)
    print(f"{GREEN}{hero['name']}{RESET} восстанавливает {RED}{heal}{RESET} здоровья!")
    hero['mp'] -= skill['mana_cost']
def skill_triple_strike (hero, enemy_team, skill):
    """
    Навык "Подавленная ярость": наносит 3 мощных удара по одному врагу.
    Активация навыка стоит 60% маны, каждый удар расходует 20%.
    Если враг умер после 1-2 ударов, оставшаяся мана не расходуется

    :param hero: (dict) Словарь героя использующего навык
    :param enemy_team: (list)  Список словарей противников
    :param skill: (dict) Словарь навыка
    :return: None
    """
    target = get_target(enemy_team)
    if not target:
        return
    hits = 3
    for i in range(hits):
        if target['hp'] > 0:
            deal_damage(hero, target, skill['value'])
            hero['mp'] -= int(skill['mana_cost'] / 3)
#
def skill_shadow_ambush(hero, skill):
    """
    Навык Засада: даёт невидимость герою, который использует навык, а аткже повышает шанс критического удара
        Невидимость - герой с таким эффектом не может быть выбран целью атаки, если есть другие союзники
    :param hero: (dict) Словарь героя использующего навык
    :param skill: (dict) Словарь навыка
    :return: None
    """
    effect_exists = False
    for eff in hero['effects']:
        if eff['type'] == "shadow_mantle":
            eff['duration'] = skill['duration']
            effect_exists = True
            break
    if not effect_exists:
        effect = effects_list['shadow_mantle'].copy()
        effect['duration'] = skill['duration']
        hero['effects'].append(effect.copy())
    hero['crit_chance'] = min(hero['crit_chance'] + skill['value'], 100)
    print(f"{GREEN}{hero['name']} {BLUE}становится невидимым{RESET}")
    hero['mp'] -= skill['mana_cost']
#
def asd():
    pass
def activate_skill(hero, hero_team, enemy_team, skill_index):
    """
    Активирует выбранный навык героя в зависимости от его типа.

    :param hero: (dict) Словарь героя использующего навык
    :param hero_team: (list) Список словарей героев
    :param enemy_team: (list) Список словарей врагов
    :param skill_index: (int) Индекс используемого навыка
    :return: None
    """
    skills = get_current_skills(hero)
    skill = skills[skill_index]
    if skill['type'] == "taunt":
        skill_taunt(skill, hero)
    elif skill['type'] == "physical_shield":
        skill_shield(skill, hero, hero_team)
    elif skill['type'] == "instant_heal":
        skill_instant_heal(hero, hero_team, skill)
    elif skill['type'] == "damage_boost":
        skill_boost_damage(hero, hero_team, skill)
    elif skill['type'] == "execution":
        skill_execution(hero, enemy_team, skill)
    elif skill['type'] == "massive_damage":
        skill_arrow_rain(hero, enemy_team, skill)
    elif skill['type'] == "stun":
        skill_stun(hero, enemy_team, skill)
    elif skill['type'] == "transform":
        hero['mp'] -= skill['mana_cost']
        skill_transform(hero, "wolf", skill['duration'])
    elif skill['type'] == "berserk":
        skill_berserk(hero, enemy_team, skill)
    elif skill['type'] == "vampire":
        skill_vampire_byte(hero, enemy_team, skill)
    elif skill['type'] == "multiple_damage":
        skill_triple_strike(hero, enemy_team, skill)
    elif skill['type'] == "shadow_ambush":
        skill_shadow_ambush(hero, skill)