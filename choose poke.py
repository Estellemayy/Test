import requests
import random


# Function to fetch data from API
def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
        }
    else:
        print(f"Failed to retrieve data for Pokemon with ID {pokemon_id}")
        return None


# Function to compare two Pokemon stats
def compare_pokemon(player, opponent, stat):
    player_stat = player[stat]
    opponent_stat = opponent[stat]

    if player_stat > opponent_stat:
        return "You win!"
    elif player_stat < opponent_stat:
        return "Opponent wins!"
    else:
        return "It's a tie!"


# Main game loop
def main():
    print("Welcome to Pokemon Top Trumps!")

    # Prompt the user to choose their Pokemon ID
    player_id = int(input("Enter the Pokemon ID you want to choose (1-151): "))

    # Randomly generate the opponent's Pokemon ID
    opponent_id = random.randint(1, 151)

    player_pokemon = get_pokemon_data(player_id)
    opponent_pokemon = get_pokemon_data(opponent_id)

    if player_pokemon and opponent_pokemon:
        print(f"Your Pokemon: {player_pokemon['name']} (ID: {player_pokemon['id']})")
        print(f"Opponent's Pokemon: {opponent_pokemon['name']} (ID: {opponent_pokemon['id']})")

        stat_choice = input("Choose a stat to compare (id, height, or weight): ").lower()

        if stat_choice in ["id", "height", "weight"]:
            result = compare_pokemon(player_pokemon, opponent_pokemon, stat_choice)
            print(result)
        else:
            print("Invalid stat choice. Choose 'id', 'height', or 'weight'.")


if __name__ == "__main__":
    main()
