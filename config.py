#Цвета для текста
#from player_classes import warrior

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
CYAN = "\033[96m"

#Рамка и полоска
#h = horizontal
#v = vertical
#d = double
#t = top
#r = right
#d = down
#l = left
line_h= "\u2500"            # ─
line_hd = "\u2550"          # ═
line_v = "\u2502"           # │
line_vd = "\u2551"          # ║
corner_tl = "\u250C"        # ┌
corner_tld = "\u2554"       # ╔
corner_tr = "\u2510"        # ┐
corner_trd = "\u2557"       # ╗
corner_dl = "\u2514"        # └
corner_dld = "\u255A"       # ╚
corner_drd = "\u255D"       # ╝
corner_dr = "\u2518"        # ┘
t_top = "\u252C"            # ┬
t_bottom = "\u2534"         # ┴
t_left = "\u251C"           # ├
t_right = "\u2524"          # ┤
cross_line = "\u253C"       # ┼
full_bar_icon = "\u2588"    # █
empty_bar_icon = "\u2592"   # ▒

damage_icon = "⚔️️"
tank_icon = "🛡️"
healer_icon = "➕️"
support_icon = "⏫"
summoner_icon = "🌱"
control_icon = "🎯"

text_line_1 = f"{YELLOW}Ходят легенды, что в Зачарованном {GREEN}Лесу{YELLOW} исполняются желания.{RESET}"
text_line_2 = f"{YELLOW}Но это лишь слухи, никто не знает что там на самом деле.{RESET}"
text_line_3 = f"{YELLOW}Люди заходили туда по разным причинам: {RESET}"
text_line_4 = f"{YELLOW}одни в поисках выгоды, другие просто сбивались с пути.{RESET}"
text_line_5 = f"{YELLOW}Но правда в одном: уже много лет каждый, кто попадал в {GREEN}Лес{YELLOW}, пропадал без вести.{RESET}"

text_line_6 = f"{RED}ВЫ{YELLOW} - рыцарь по имени Лотарь.{RESET}"
text_line_7 = f"{YELLOW}Некогда королевский рыцарь, а теперь {RED}искатель приключений{YELLOW}.{RESET}"
text_line_8 = f"{YELLOW}Рыцарь больше не служит короне, но всё ещё храбр духом, чтобы сражаться со злом.{RESET}"
text_line_9 = f"{YELLOW}Когда он услышал о пропажах в Зачарованном {GREEN}Лесу{YELLOW}, то не смог остаться в стороне.{RESET}"
text_line_10 = f"{YELLOW}Вместе со своей командой вы отправились на задание.{RESET}"
text_line_11 = f"{YELLOW}Ваш отряд вошёл в {GREEN}Лес{YELLOW} совсем недавно...{RESET}"
text_line_12 = f"{RED}... но вы ничего не помните.{RESET}"
text_line_13 = f"{BLUE}Рыцарь пытается вспомнить свой отряд.{RESET}"