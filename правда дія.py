import random

heroes = [
    "Супермен",
    "Бетмен",
    "Людина-павук",
    "Залізна людина",
    "Халк"
]

gamer_list = []
roles = {}

def gamers(list):
    while True:
        name = input("Введіть ім'я гравця - ")
        if 0 < len(name) <= 2:
            continue
        list.append(str.capitalize(name))
        if len(list) >= 2:
            need_next_player = input("Додати ще гравців? - Так(т) / Ні(н): ")
            if need_next_player.lower() in ["т", "так"]:
                continue
            else:
                break

gamers(gamer_list)

def give_roles(players, heroes):
    if len(players) > len(heroes):
        print("❌ Забагато гравців! Героїв менше.")
        return

    random.shuffle(heroes)

    for i in range(len(players)):
        roles[players[i]] = heroes[i]

def show_roles(roles):
    print("\n🎭 Результати:")
    for player, hero in roles.items():
        print(f"{player} — {hero}")

# запуск
give_roles(gamer_list, heroes)
show_roles(roles)