from utils import *
from player_classes import *

game_state = {
    #Сбор команд
    "hero_team_size": 4,
    "enemy_team_size": 4,
    "heroes_team": [],
    "enemies_team": [],
    "all_heroes": [warrior, medic_dog, tank_human, stalker, werewolf, archer, tank_bear, tank_bot, bard_human, witch_doctor, gardener, mushroom, engineer, priestess, mage, shadow],
    "all_enemies": [goblin, orc, wolf, fox],
    "secret_heroes": [werewolf, archer, tank_bear, tank_bot],
    "available_heroes": [warrior, medic_dog, tank_human, stalker],
    #Сражение
    "round": 1,
    "phase": "intro",
    "current_hero": 0,
    "current_enemy": 0,
    #Конец боя
    "game_over": False,
    "winner": None,
    #Остальное
    "effects_list": {},
    "secret_heroes_unlocked": False,
    "secret_code": "+",
    "await_input": False,
    "log": []
}

def render(game_state):
    if game_state["log"]:
        for line in game_state["log"]:
            print(line)
        game_state["log"].clear()

    if game_state["phase"] == "intro":
        writes_the_introduction()
        #print(f"{BLUE}Нажмите ENTER, чтобы продолжить.{RESET}")
    elif game_state["phase"] == "secret_key":
        print(f"{BLUE}Введите секретный код (или ENTER, чтобы пропустить).{RESET}")
    elif game_state["phase"] == "choose_heroes":
        for i in range(len(game_state["available_heroes"])):
            hero = game_state["available_heroes"][i]
            #print(f"{hero['icon']} {GREEN}{hero['name']}{RESET}: {RED}{hero['max_hp']} HP{RESET}, {BLUE}{hero['damage']} DAMAGE{RESET}")

            print(f"{hero['icon']} {GREEN}{hero['name']}{RESET}: {BLUE}{hero['damage']} DAMAGE{RESET}")
            shows_hp_bar(hero)

            print(f"    {BLUE}{t_left}{line_h} {YELLOW}Атака{RESET} = {hero.get('attack', {}).get('name', 'удар')}{RESET} = {hero.get('attack', {}).get('description', 'мощный удар')}{RESET}")
            skills = get_current_skills(hero)

            num_of_skills = 0
            for _ in skills:
                num_of_skills += 1
            for skill in skills:
                if num_of_skills == 1:
                    line_or_corner = corner_dl
                else:
                    line_or_corner = t_left

                print(f"    {BLUE}{line_or_corner}{line_h} {YELLOW}{skill['name']}{RESET} = {skill['description']}")
                num_of_skills -= 1
            time.sleep(0.4)

def update(game_state, action):
    game_state["await_input"] = True

    if game_state["phase"] == "intro":
        game_state["phase"] = "secret_key"
    elif game_state["phase"] == "secret_key":
        if action.strip() == game_state["secret_code"]:
            game_state["available_heroes"].extend(game_state["secret_heroes"])
            game_state["secret_heroes_unlocked"] = True
            game_state["log"].append(f"{YELLOW}Секретные герои разблокированы!{RESET}")
        else:
            game_state["log"].append(f"{YELLOW}Код не подошёл.{RESET}")
        game_state["phase"] = "choose_heroes"
        game_state["await_input"] = False
    if True:
        pass

def game_loop():
    while game_state["phase"] != "done":
        render(game_state)
        if game_state["await_input"]:
            action = input(">>> ")
            update(game_state, action)
        else:
            update(game_state, "")

game_loop()