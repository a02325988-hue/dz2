details_damage_price = {
    "energy gun": 100,
    "minigun": 70,
    "Thor hammer": 50,
    "laser gun": 80,
    "rail gun": 90,
    "sniper rifle": 150
}

details_survive_price = {
    "shield": 50,
    "energy shield": 80,
    "resist": 30,
    "evasion": 100,
    "armor": 140
}
users_bot = {}
player_list = []
def corrector(text, width, symbol):
    return text.center(width, symbol)
def player_maker(players):
    while True:
        name = input("Enter player name: ")
        if len(name) < 3:
            print("Too short name")
            continue
        players.append(name.capitalize())
        more = input("Add more players? (y/n): ").lower()
        if more != "y":
            break
    print("Players:", ", ".join(players))
def bot_maker(start_sum, players):
    for player in players:
        wallet = start_sum
        users_bot[player] = {}
        while wallet >= 30:  # мінімальна ціна
            print(corrector(f"{player} | coins: {wallet}", 60, "="))
            print(corrector("SHOP", 60, "-"))
            print(corrector("Weapons", 60, "^"))
            for item, price in details_damage_price.items():
                print(f"{item} - {price}")
            print(corrector("Defense", 60, "^"))
            for item, price in details_survive_price.items():
                print(f"{item} - {price}")
            choice = input("Choose item: ").lower()
            if choice in users_bot[player]:
                print("Already have this!")
                continue
            if choice in details_damage_price:
                price = details_damage_price[choice]
            elif choice in details_survive_price:
                price = details_survive_price[choice]
            else:
                print("Wrong choice")
                continue
            if wallet < price:
                print("Not enough coins")
                continue
            wallet -= price
            users_bot[player][choice] = price

            print("Your bot:", ", ".join(users_bot[player].keys()))
            print()
    print("\nFinal bots:")
    for player in players:
        print(player, "->", ", ".join(users_bot[player].keys()))
player_maker(player_list)
start_sum = int(input("Start coins: "))
bot_maker(start_sum, player_list)

