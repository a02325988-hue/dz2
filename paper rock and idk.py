import random
def game(choice, result):
    print("\n===== Start Game rock, paper, scissors, lizard, spock =====")
    computer_choice = random.choice("rpslc")
    print("--------------------------------")
    print("Your select –", choice.upper())
    print("Computer select –", computer_choice.upper())
    if choice == computer_choice:
        print("Result of game – Draw")
    elif choice == "r" and computer_choice == "p":
        result["computer"] += 1
        print("------Computer Wins------")
    elif choice == "r" and computer_choice == "s":
        result["player"] += 1
        print("------Player Wins------")
    elif choice == "r" and computer_choice == "l":
        result["player"] += 1
        print("------Player Wins------")
    elif choice == "r" and computer_choice == "c":
        result["computer"] += 1
        print("------Computer Wins------")
    elif choice == "p" and computer_choice == "r":
        result["player"] += 1
        print("------Player Wins------")
    elif choice == "p" and computer_choice == "s":
        result["computer"] += 1
        print("------Computer Wins------")
    elif choice == "p" and computer_choice == "l":
        result["computer"] += 1
        print("------Computer Wins------")
    elif choice == "p" and computer_choice == "c":
        result["player"] += 1
        print("------Player Wins------")
    elif choice == "s" and computer_choice == "p":
        result["player"] += 1
        print("------Player Wins------")
    elif choice == "s" and computer_choice == "r":
        result["computer"] += 1
        print("------Computer Wins------")
    elif choice == "s" and computer_choice == "l":
        result["player"] += 1
        print("------Player Wins------")
    elif choice == "s" and computer_choice == "c":
        result["computer"] += 1
        print("------Computer Wins------")
    elif choice == "l" and computer_choice == "p":
        result["player"] += 1
        print("------Player Wins------")
    elif choice == "l" and computer_choice == "c":
        result["player"] += 1
        print("------Player Wins------")
    elif choice == "l" and computer_choice == "r":
        result["computer"] += 1
        print("------Computer Wins------")
    elif choice == "l" and computer_choice == "s":
        result["computer"] += 1
        print("------Computer Wins------")
    elif choice == "c" and computer_choice == "r":
        result["player"] += 1
        print("------Player Wins------")
    elif choice == "c" and computer_choice == "s":
        result["player"] += 1
        print("------Player Wins------")
    elif choice == "c" and computer_choice == "p":
        result["computer"] += 1
        print("------Computer Wins------")
    elif choice == "c" and computer_choice == "l":
        result["computer"] += 1
        print("------Computer Wins------")
    print("Score: Computer", result["computer"], "—", result["player"], "Player")
result = {"computer": 0, "player": 0}
while True:
    print("\n===== MENU =====")
    print("1 - Play")
    print("2 - Exit")
    menu = input("Select option: ")
    if menu == "1":
        choice = input("Select R / P / S / L / C – ").lower()
        if choice not in ["r", "p", "s", "l", "c"]:
            print("Wrong input")
            continue
        game(choice, result)
    elif menu == "2":
        print("Goodbye")
        break
    else:
        print("Choose 1 or 2")