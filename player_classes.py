from config import *

#Классы
    #damage
    #support
    #tank

#Все герои
medic_dog = {
    "name": "Берри",
    "class": "support",
    "icon": healer_icon,
    "max_hp": 60,
    "hp": 60,
    "max_mp": 100,
    "mp": 30,
    "damage": 10,
    "threat": 0.8,
    "accuracy": 85,
    "crit_chance": 20,
    "basic_crit_chance": 20,
    "effects": [],
    "skills": [
        {
            "name": "Аптечка",
            "description": "Исцеление выбранного союзника на 20 здоровья",
            "type": "instant_heal",
            "mana_cost": 10,
            "value": 20,
            "duration": None
        },
        {
            "name": "Оглушающий лай",
            "description": "Громкий лай оглушает выбранного противника на 1 ход",
            "type": "stun",
            "mana_cost": 30,
            "duration": None
        }
    ]
}
tank_human = {
    "name": "Паладин",
    "class": "tank",
    "icon": tank_icon,
    "max_hp": 150,
    "hp": 150,
    "max_mp": 100,
    "mp": 30,
    "damage": 15,
    "threat": 1.0,
    "accuracy": 85,
    "crit_chance": 20,
    "basic_crit_chance": 20,
    "effects": [],
    "skills": [
        {
            "name": "Провокация",
            "description": "Заставляет всех врагов атаковать себя на 1 ход",
            "type": "taunt",
            "mana_cost": 50,
            "value": None,
            "duration": 1
        },
        {
            "name": "Щит веры",
            "description": "Накладывает щит на союзника, блокирующий 30 урона",
            "type": "physical_shield",
            "mana_cost": 30,
            "value": 30,
            "duration": 0
        }
    ]
}
warrior = {
    "name": "Рыцарь",
    "class": "damage",
    "icon": damage_icon,
    "max_hp": 80,
    "hp": 80,
    "max_mp": 100,
    "mp": 30,
    "damage": 20,
    "threat": 0.9,
    "accuracy": 85,
    "crit_chance": 20,
    "basic_crit_chance": 20,
    "effects": [],
    "skills": [
        {
            "name": "Боевой клич",
            "description": "Увеличивает урон базовой атаки союзников. 2 заряда",
            "type": "damage_boost",
            "mana_cost": 30,
            "value": 1.5,
            "charges": 2
    },
        {
            "name": "Яростный взмах",
            "description": "Наносит 60 урона выбранному врагу. При убийстве врага мана не расходуется",
            "type": "execution",
            "mana_cost": 60,
            "value": 60,
            "duration": None
        }
    ]
}
werewolf = {
    "name": "Оборотень",
    "class": "damage",
    "icon": "🧔",
    "base_max_hp": 100,
    "base_hp": 100,
    "base_damage": 10,
    "base_threat": 1,
    "base_accuracy": 100,
    "base_crit_chance": 100,
    "max_mp": 100,
    "mp": 30,
    "effects": [],
    "max_hp": 100,
    "hp": 100,
    "damage": 10,
    "threat": 0.8,
    "accuracy": 85,
    "crit_chance": 20,
    "basic_crit_chance": 20,
    "transform_timer": 0,
    "form": "human",
    "forms": {
        "human": {
            "max_hp_mod": 1.0,
            "damage_mod": 1,
            "threat_mod": 0.8,
            "accuracy_mod": 0.85,
            "crit_chance_mod": 0.2,
            "icon": "🧔",
            "skills": [
                {
                    "name": "Жажда крови",
                    "description": "Атакует врага кинжалом. Урон увеличивается с потерей здоровья.",
                    "type": "berserk",
                    "mana_cost": 30,
                    "value": 20,
                    "duration": 0
                },
                {
                    "name": "Подавленная ярость",
                    "description": "Перевоплощение в зверя",
                    "type": "transform",
                    "mana_cost": 60,
                    "duration": 5,
                    "target_form": "wolf"
                }
            ]
        },
        "wolf": {
            "max_hp_mod": 0.6,
            "damage_mod": 2.5,
            "threat_mod": 1.2,
            "accuracy_mod": 1.0,
            "crit_chance_mod": 0.3,
            "icon": "🐺",
            "skills": [
                {
                    "name": "Жажда крови",
                    "description": "Кусает врага, нанося урон и восстанавливая здоровье.",
                    "type": "vampire",
                    "mana_cost": 30,
                    "value": 30,
                    "duration": None
                },
                {
                    "name": "Подавленная ярость",
                    "description": "Наносит 3 удара (по 20 урона) выбранному врагу.",
                    "type": "multiple_damage",
                    "mana_cost": 60,
                    "value": 20,
                    "duration": None
                }
            ]
        }
    },
}

#Все враги
orc = {
    "name": "Орк",
    "max_hp": 180,
    "hp": 180,
    "mp": 0,
    "max_mp": 0,
    "damage": 12,
    "threat": 1,
    "effects": [],
    "skills": []
}
goblin = {
    "name": "Гоблин",
    "max_hp": 130,
    "hp": 130,
    "mp": 0,
    "max_mp": 0,
    "damage": 16,
    "threat": 1,
    "effects": [],
    "skills": []
}
fox = {
    "name": "Лис",
    "max_hp": 90,
    "hp": 90,
    "mp": 0,
    "max_mp": 0,
    "damage": 20,
    "threat": 1,
    "effects": [],
    "skills": []
}
wolf = {
    "name": "Волк",
    "max_hp": 50,
    "hp": 50,
    "mp": 0,
    "max_mp": 0,
    "damage": 30,
    "threat": 1,
    "effects": [],
    "skills": []
}

#Прочие герои
placeholder = {
    "name": "",
    "class": "",
    "icon": "",
    "max_hp": 0,
    "hp": 0,
    "max_mp": 0,
    "mp": 0,
    "damage": 0,
    "threat": 1,
    "accuracy": 85,
    "crit_chance": 20,
    "basic_crit_chance": 20,
    "effects": [],
    "skills": [
        {
            "name": "",
            "description": "",
            "type": "",
            "mana_cost": 0,
            "value": 0,
            "duration": 0
        },
        {
            "name": "",
            "description": "",
            "type": "",
            "mana_cost": 0,
            "value": 0,
            "duration": 0
        }
    ]
}
stalker = {
    "name": "Сталкер",
    "class": "damage",
    "icon": damage_icon,
    "max_hp": 60,
    "hp": 60,
    "max_mp": 100,
    "mp": 30,
    "damage": 15,
    "threat": 0.8,
    "accuracy": 100,
    "crit_chance": 20,
    "basic_crit_chance": 20,
    "effects": [],
    "skills": [
        {
            "name": "Засада",
            "description": "Герой становится невидимым на 2 хода и повышает шанс критического удара на 30%.",
            "type": "shadow_ambush",
            "mana_cost": 30,
            "value": 30,
            "duration": 2
        },
        # {
        #     "name": "Разящий выстрел",
        #     "description": "Герой совершает мощный выстрел, урон которого увеличивается от шанса критического удара.",
        #     "type": "critical_shot",
        #     "mana_cost": 50,
        #     "value": 30,
        #     "duration": None
        # }
    ]
}
archer = {
    "name": "Лучница",
    "class": "damage",
    "icon": damage_icon,
    "max_hp": 80,
    "hp": 80,
    "max_mp": 100,
    "mp": 30,
    "damage": 20,
    "threat": 0.9,
    "accuracy": 100,
    "crit_chance": 20,
    "basic_crit_chance": 20,
    "effects": [],
    "skills": [
        {
            "name": "Град стрел",
            "description": "Обрушает град стрел на врагов. Каждый выстрел стоит 15 маны",
            "type": "massive_damage",
            "mana_cost": 10,
            "value": 20,
            "duration": None,
            "max_duration": None
        },
        # {
        #     "name": "Метка охотника",
        #     "description": "Ставит метку охотника на врага, увеличивая получаемый им урон в 2 раза. Действует 2 хода",
        #     "type": "damage_mark",
        #     "mana_cost": 80,
        #     "value": 2,
        #     "duration": 2
        # }
    ]
}

#Списки всех существ
all_hero = [warrior, medic_dog, tank_human, werewolf]
all_enemies = [goblin, orc, wolf, fox]
secret_heroes = [archer, stalker]
#Размеры команд
hero_team_size = 3
enemy_team_size = 3