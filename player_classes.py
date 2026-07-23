from config import *

#Классы
    #damage
    #support
    #tank

#Все герои
warrior = {
    "name": "Воин",
    "description": "Воин - опытный воин и вдохновляющий лидер команды, мастерски владеющий рапирой. Он не только наносит уверенные удары, но и служит сердцем команды и опорой для союзников, усиливая их в атаке. Его присутствие на поле боя вселяет уверенность и помогает команде выдержать самые сложные испытания.",
    "class": "damage",
    "icon": damage_icon,
    "max_hp": 80,
    "hp": 80,
    "max_mp": 100,
    "mp": 30,
    "attack": [
        {
            "name": "Укол",
            "description": "Совершает быстрый укол рапирой, нанося 20 урона",
            "damage": 20,
            "damage_type": "physical",
            "accuracy": 85,
            "basic_crit_chance": 20,
            "crit_chance": 20,
            "effects": []
        }
    ],
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
            "name": "Выпад",
            "description": "Мощный колющий удар рапирой, наносящий 60 урона. При убийстве мана не расходуется",
            "type": "execution",
            "mana_cost": 60,
            "value": 60,
            "duration": None
        }
    ]
}
medic_dog = {
    "name": "Берри",
    "description": "Берри - непревзойдённый защитник и верный спутник. Его громкий лай способен остановить любого противника, а навыки полевого медика делают его незаменимым членом отряда. Всегда готов прийти на помощь, прикрыть товарища и вцепиться в горло обидчику.",
    "class": "support",
    "icon": healer_icon,
    "max_hp": 60,
    "hp": 60,
    "max_mp": 100,
    "mp": 30,
    "attack": [
        {
            "name": "Крепкая хватка",
            "description": "Берри кусает врага, нанося 10 урона.",
            "damage": 10,
            "damage_type": "physical",
            "accuracy": 85,
            "basic_crit_chance": 20,
            "crit_chance": 20,
            "effects": []
    }
    ],
    "damage": 10,
    "threat": 0.8,
    "accuracy": 85,
    "crit_chance": 20,
    "basic_crit_chance": 20,
    "effects": [],
    "skills": [
        {
            "name": "Экстренная помощь",
            "description": "Берри использует содержимое своего рюкзака, чтобы мгновенно восстановить 20 здоровья союзнику.",
            "type": "instant_heal",
            "mana_cost": 10,
            "value": 20,
            "duration": None
        },
        {
            "name": "Оглушающий лай",
            "description": "Громкий, пронзительный лай оглушает выбранного врага на 1 раунд",
            "type": "stun",
            "mana_cost": 30,
            "duration": None
        }
    ]
}
tank_human = {
    "name": "Паладин",
    "description": "Паладин - ???",
    "class": "tank",
    "icon": tank_icon,
    "max_hp": 150,
    "hp": 150,
    "max_mp": 100,
    "mp": 30,
    "attack": [
        {
            "name": "Священный молот",
            "description": "Паладин совершает мощный удар молотом, нанося 15 урона врагу.",
            "damage": 15,
            "damage_type": "physical",
            "accuracy": 85,
            "basic_crit_chance": 20,
            "crit_chance": 20,
            "effects": []
        }
    ],
    "damage": 15,
    "threat": 1.0,
    "accuracy": 85,
    "crit_chance": 20,
    "basic_crit_chance": 20,
    "effects": [],
    "skills": [
        {
            "name": "Щит веры",
            "description": "Накладывает на союзника защитный барьерБ который полностью поглощает входящий ФИЗИЧЕСКИЙ урон до исчерпания своего запаса прочности",
            "type": "physical_shield",
            "mana_cost": 30,
            "value": 30,
            "duration": 0
        },
        {
            "name": "Провокация",
            "description": "Заставляет всех врагов атаковать себя на 1 раунд",
            "type": "taunt",
            "mana_cost": 50,
            "value": None,
            "duration": 1
        },

    ]
}
werewolf = {
    "name": "Оборотень",
    "description": "Две личности борются за контроль над телом: холодный разум человека и неистовая ярость зверя. Когда луна восходит, его когти рвут плоть, а когда заходит - остаются лишь кровавые следы и тихий стон, застрывший между человеческим <почему?> и звериным <ещё>...",
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
                    "name": "Высвобождение ярости",
                    "description": "Превращается в зверя",
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
            "crit_chance_mod": 0.2,
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
                    "name": "Высвобождение ярости",
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
stalker = {
    "name": "Сталкер",
    "description": "Сталкер - призрачная фигура, возникаящая из ниоткуда и исчезающая в никуда. Он хладнокровно выжидает нужный момент, чтобы одним точным выстрелом пробить защиту врага и переломить ход сражения. Смертоносная тень, от которой не уйти и не спрятаться.",
    "class": "damage",
    "icon": damage_icon,
    "max_hp": 60,
    "hp": 60,
    "max_mp": 100,
    "mp": 30,
    "attack": [
        {
            "name": "Жнец душ",
            "description": "Сталкер совершает выстрел по врагу из своего арбалета, нанося 15 урона.",
            "damage": 15,
            "damage_type": "physical",
            "accuracy": 100,
            "basic_crit_chance": 20,
            "crit_chance": 20,
            "skills": []
        }
    ],
    "damage": 15,
    "threat": 0.8,
    "accuracy": 100,
    "crit_chance": 20,
    "basic_crit_chance": 20,
    "effects": [],
    "skills": [
        {
            "name": "Засада",
            "description": "Герой становится невидимым на 2 раунда и повышает шанс критического удара на 30%.",
            "type": "shadow_ambush",
            "mana_cost": 30,
            "value": 30,
            "duration": 2
        },
        {
            "name": "Разящий выстрел",
            "description": "Герой совершает мощный выстрел, урон которого увеличивается от шанса критического удара.",
            "type": "critical_shot",
            "mana_cost": 50,
            "value": 10,
            "duration": None
        }
    ]
}

#Все враги
orc = {
    "name": "Орк",
    "max_hp": 150,
    "hp": 150,
    "mp": 0,
    "max_mp": 0,
    "damage": 12,
    "threat": 1,
    "effects": [],
    "skills": []
}
goblin = {
    "name": "Гоблин",
    "max_hp": 120,
    "hp": 120,
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

#Прочие герои (не готовы)
placeholder = {
    "name": "",
    "description": "",
    "class": "",
    "icon": "",
    "max_hp": 0,
    "hp": 0,
    "max_mp": 0,
    "mp": 0,
    "attack": [
        {
            "name": "",
            "description": "",
            "damage": 0,
            "damage_type": "physical",
            "accuracy": 85,
            "basic_crit_chance": 20,
            "crit_chance": 20,
            "effects": []
        }
    ],
    "threat": 1,
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
archer = {
    "name": "Лучница",
    "class": "damage",
    "icon": damage_icon,
    "max_hp": 80,
    "hp": 80,
    "max_mp": 100,
    "mp": 30,
    "attack": [
        {
            "damage": 20,
            "damage_type": "physical",
            "accuracy": 100,
            "basic_crit_chance": 20,
            "crit_chance": 20,
            "skills": []
        }
    ],
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
        {
            "name": "Метка охотника",
            "description": "Ставит метку охотника на врага, увеличивая получаемый им урон в 2 раза. Действует 2 хода",
            "type": "damage_mark",
            "mana_cost": 80,
            "value": 2,
            "duration": 2
        }
    ]
}
bard_human = {
    "name": "Себастьян",
    "description": "Бард",
    "class": "support",
    "icon": support_icon,
    "max_hp": 60,
    "hp": 60,
    "max_mp": 100,
    "mp": 30,
    "attack": [
        {
            "name": "",
            "description": "",
            "damage": 0,
            "damage_type": "physical",
            "accuracy": 85,
            "basic_crit_chance": 20,
            "crit_chance": 20,
            "effects": []
        }
    ],
    "threat": 1,
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
    ]}
tank_bear = {
    "name": "Медведь",
    "description": "Медведь - грозный страж из дремучего леса, чья природная сила и невероятная выносливость делают его почти неостановимым в бою. Его рёв заставляет врагов замереть на месте, а мощные удары когтей сокрушают даже самых крепких противников. Лесные ягоды - одно из его любимых угощений.",
    "class": "tank",
    "icon": tank_icon,
    "max_hp": 200,
    "hp": 200,
    "max_mp": 100,
    "mp": 30,

    "damage": "20",

    "attack": [
        {
            "name": "Массивные когти",
            "description": "Совершает удар когтистой лапой, нанося ?? урона врагу.",
            "damage": 0,
            "damage_type": "physical",
            "accuracy": 85,
            "basic_crit_chance": 20,
            "crit_chance": 20,
            "effects": []
        }
    ],
    "threat": 1,
    "effects": [],
    "skills": [
        {
            "name": "Рёв зверя",
            "description": "Медведь издаёт оглушительный рёв, провоцируя всех врагов атаковат =ь только его.",
            "type": "stun",
            "mana_cost": 20,
            "value": 0,
            "duration": 1
        },
        {
            "name": "Сокрушение",
            "description": "Медведь обрушает всю свою силу на врага, нанося ?? урона и оглушая цель.",
            "type": "",
            "mana_cost": 30,
            "damage_type": "physical",
            "value": 0,
            "duration": 1
        },
        {
            "name": "Сладкий мёд",
            "description": "Медведь съедает мёд, восстанавливая часть здоровья в начале каждого хода.",
            "type": "",
            "mana_cost": 40,
            "value": 20,
            "duration": 8
        }
    ]
}
witch_doctor = {}
gardener = {}
mushroom = {}
engineer = {}
tank_bot = {}
priestess = {}
mage = {}
shadow = {}

#Списки всех существ
all_hero = [warrior, medic_dog, tank_human, werewolf, stalker]
all_enemies = [goblin, orc, wolf, fox]
secret_heroes = [archer, bard_human, tank_bear, witch_doctor, gardener, mushroom, engineer, tank_bot, priestess, mage, shadow]

#Размеры команд
hero_team_size = 4
enemy_team_size = 3