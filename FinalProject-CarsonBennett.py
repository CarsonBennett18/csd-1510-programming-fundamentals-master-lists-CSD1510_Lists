#
import random
import math

# ---------- Helper Functions ----------

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid input. Please enter a number.")

def land_price():
    return random.randint(17, 26)

def harvest_rate():
    return random.randint(1, 4)

def check_rats(wheat):
    if random.random() < 0.1:
        eaten = math.ceil(wheat * 0.25)
        return eaten
    return 0

def check_plague(pop):
    if random.random() < 0.1:
        died = math.ceil(pop * 0.4)
        return died
    return 0

def starvation(pop, food):
    fed_people = food // 20
    starved = max(0, pop - fed_people)
    return starved

def arrivals(pop, acres):
    return random.randint(1, 10)

# ---------- Main Game ----------

def main():
    acres = 200
    population = 20
    wheat = 1000
    total_starved = 0

    for round_num in range(1, 11):
        print(f"\n--- Round {round_num} ---")
        print(f"Population: {population}")
        print(f"Acres: {acres}")
        print(f"Wheat: {wheat}")

        price = land_price()
        print(f"Land price: {price} bushels per acre")

        # --- Buy/Sell Land ---
        while True:
            land = get_int_input("Acres to buy (+) or sell (-): ")
            if land > 0:
                cost = land * price
                if cost <= wheat:
                    acres += land
                    wheat -= cost
                    break
            else:
                if abs(land) <= acres:
                    acres += land
                    wheat -= land * price
                    break
            print("Invalid land transaction.")

        # --- Farming ---
        while True:
            farm = get_int_input("Acres to plant: ")
            if farm <= acres and farm <= population * 10 and farm <= wheat:
                wheat -= farm
                break
            print("Invalid farming amount.")

        # --- Feeding ---
        while True:
            food = get_int_input("Bushels to feed people: ")
            if food <= wheat:
                wheat -= food
                break
            print("Not enough wheat.")

        # --- Harvest ---
        rate = harvest_rate()
        harvested = farm * rate
        wheat += harvested
        print(f"Harvest rate: {rate} per acre")
        print(f"Harvested: {harvested} bushels")

        # --- Starvation ---
        starved = starvation(population, food)
        total_starved += starved
        population -= starved

        print(f"{starved} people starved.")

        if population == 0:
            print("All your people have died. Game over.")
            return

        if starved > (population + starved) * 0.45:
            print("Too many people starved! Game over.")
            return

        # --- New People ---
        new_people = arrivals(population, acres)
        population += new_people
        print(f"{new_people} people arrived.")

        # --- Rats ---
        eaten = check_rats(wheat)
        if eaten > 0:
            wheat -= eaten
            print(f"Rats ate {eaten} bushels!")

        # --- Plague ---
        died = check_plague(population)
        if died > 0:
            population -= died
            print(f"Plague killed {died} people!")

    # --- End Game ---
    print("\n--- Game Over ---")
    print(f"Final Population: {population}")
    print(f"Final Acres: {acres}")
    print(f"Final Wheat: {wheat}")
    print(f"Total Starved: {total_starved}")


if __name__ == "__main__":
    main()