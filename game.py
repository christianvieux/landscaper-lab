class player: 
    def __init__(self, name):
        self.name = name;
        self.money = 0;
        self.items = [];

def give_money(player, amount):
    player.money += amount;
    print(f"You've earned ${amount}! Your total money is ${player.money}");

def list_options(player):
    print(f"\n\n{player.name}, you currently have ${player.money}")
    print("\n\nPlease choose from one of these options:");
    
    print("\n\n1. Cut the lawn with your teeth                               (earn $1)");

    print(    "2. Spend the day cutting lawns with Scissors                  (earn $5)" +
        ("" if "scissors" in player.items else "   [Locked]"));

    print(    "3. Spend the day cutting lawns with Old-timey Push Lawnmower  (earn $25)" +
        ("" if "push_mower" in player.items else "  [Locked]"));

    print(    "4. Spend the day cutting lawns with Battery-powered Lawnmower (earn $100)" +
        ("" if "battery_mower" in player.items else " [Locked]"));

    print(    "5. Spend the day cutting lawns with Team of starving students (earn $250)" +
        ("" if "student_team" in player.items else " [Locked]"));

    print(    "6. View Shop");
    print(    "7. View my Options");

def list_shop_options(player):
    print("\nWhat would you like to buy? :\n\n");
    
    if "scissors" in player.items:
        print("1. Rusty Scissors ($5) [Already purchased]");
    else:
        print("1. Rusty Scissors ($5)" +
              ("" if player.money >= 5 else " [Not enough money]"));
    if "push_mower" in player.items:
        print("2. Old-timey Push Lawnmower ($25) [Already purchased]");
    else:
        print("2. Old-timey Push Lawnmower ($25)" +
              ("" if player.money >= 25 else " [Not enough money]"));
    if "battery_mower" in player.items:
        print("3. Battery-powered Lawnmower ($250) [Already purchased]");
    else:
        print("3. Battery-powered Lawnmower ($250)" +
              ("" if player.money >= 250 else " [Not enough money]"));
    if "student_team" in player.items:
        print("4. Hire a team of starving students ($500) [Already purchased]");
    else:
        print("4. Hire a team of starving students ($500)" +
              ("" if player.money >= 500 else " [Not enough money]"));

    print("5. Return");

def shop_option(player, listOptions=False):
    # Show options to the player only IF the listOptions flag is true.
    if listOptions: list_shop_options(player);
    
    # get player selection
    selection = input("\nSelect Item: ")
    
    # logic for the selection
    if selection == "1":
        if "scissors" not in player.items and player.money >= 5:
            player.items.append("scissors")
            player.money -= 5
            print("You have purchased Rusty Scissors!")
        else:
            print("You cannot buy Rusty Scissors.")
    elif selection == "2":
        if "push_mower" not in player.items and player.money >= 25:
            player.items.append("push_mower")
            player.money -= 25
            print("You have purchased Old-timey Push Lawnmower!")
        else:
            print("You cannot buy Old-timey Push Lawnmower.")
    elif selection == "3":
        if "battery_mower" not in player.items and player.money >= 250:
            player.items.append("battery_mower")
            player.money -= 250
            print("You have purchased Battery-powered Lawnmower!")
        else:
            print("You cannot buy Battery-powered Lawnmower.")
    elif selection == "4":
        if "student_team" not in player.items and player.money >= 500:
            player.items.append("student_team")
            player.money -= 500
            print("You have hired a team of starving students!")
        else:
            print("You cannot hire a team of starving students.")
    elif selection == "5":
        return main_option(player, True);
    else:
        print("Invalid selection. Please select a valid option.")
        return shop_option(player);

    return shop_option(player);

def main_option(player, listOptions=False):
    # Condition for player winning
    if player.money >= 100 and "student_team" in player.items:
        return print("\n\n\n\n\nCongrats, you got a team of starving students and made over $1000! You won the game!")

    # Show options to the player only IF the listOptions flag is true.
    if listOptions: list_options(player);

    # Get player choice
    playerChoice = input("\n\nWhat would you like to do?: ");

    print("\n\n") # New line

    if playerChoice == "1":
        give_money(player, 1);
        return main_option(player);
    elif playerChoice == "2":
        if "scissors" in player.items:
            give_money(player, 5);
        else:
            print("You don't have Scissors yet! Try buying it from the shop.");
        return main_option(player);
    elif playerChoice == "3":
        if "push_mower" in player.items:
            give_money(player, 25);
        else:
            print("You don't have the Old-timey Push Lawnmower yet!");
        return main_option(player);
    elif playerChoice == "4":
        if "battery_mower" in player.items:
            give_money(player, 100)
        else:
            print("You don't own the Battery-powered Lawnmower yet!");
        return main_option(player);
    elif playerChoice == "5":
        if "student_team" in player.items:
            give_money(player, 250)
        else:
            print("You haven't hired the team of starving students yet!");
        return main_option(player);
    elif playerChoice == "6":
        return shop_option(player, True);
    elif playerChoice == "7":
        list_options(player);
        return main_option(player);
    else:
        print("Invalid choice. Please choose a valid option.");
        return main_option(player);


# Define new player
playerName = input("Please enter your name: ");
newPlayer = player(playerName);

# Start the game
list_options(newPlayer);
main_option(newPlayer);