import random
import time

points = 500

quitgame = False

print("PLINKO GAME")

def play_plinko():
    global points, quitgame
    print("Points:", points)
    print("Input 0 to quit the game.")
    
    try:
        betamount = int(input("Bet Amount: "))
    except ValueError:
        print("Invalid input. Please enter an integer.") # Checks to make sure input is integer
        return
    
    if betamount == 0:
        print("You chose to quit the game.")
        quitgame = True
        return
    
    # Setting bet parameters
    if betamount < 50:
        print("Bet must be 50 or higher.")
        return
    elif betamount > points:
        print("Not enough points.")
        return

    points -= betamount
    betmultiplier = betamount / 50

    def simulate_plinko_animated():
        position = int(input("Which column? "))  # Chooses column to drop ball
        rows = 14
        path = [max(0, min(10, position-1))]
        
        for _ in range(rows):
            move = random.choice([-1, 1])
            position += move
            position = max(0, min(10, position))  # Keep within bounds
            path.append(position)
        
        return path

    def print_board(path):
        print("|1 |2  |3  |4  |5  |6  |7  |8  |9  |10 |11|")
        for pos in path:
            row = ["    "] * 11
            row[pos] = " o "
            print("".join(row))
            time.sleep(0.14)  # Pause for animation effect
        print("|0 |25 |45 |75 |100|150|100|75 |45 |25 |0|")
    
    path = simulate_plinko_animated()
    print_board(path)

    final_pos = path[-1]
    scores = [0, 25, 45, 75, 100, 150, 100, 75, 45, 25, 0]
    fprize = round(scores[final_pos] * betmultiplier, 0)
    points += fprize
    points = round(points, 0)

    print("Bet multiplier:", betmultiplier)
    print("\nYou Win:", fprize, "\n")

while points >= 50 and not quitgame:
    play_plinko()
    
    if quitgame:
        break
    
    if points >= 37000:
        print("The carnival worker looks at you with shock(and a slight tint of malice) in his face and says;")
        time.sleep(2)
        print("'You have depleted the entire carnival's supply of money...'")
        time.sleep(2)
        print("'Thanks for putting me out of a job, jerk...'")
        time.sleep(2)
        print("The crowd that has slowly been gathering around you is looking at you, with a wide-eyed expression of greed.")
        time.sleep(2)
        print("One of the onlookers says, 'Well, since you got all that, could I, uh... maybe get $500 of it..?'")
        time.sleep(2)
        print("A chorus of 'me too' follows.")
        time.sleep(2)
        break

print("Game over. Final points:", points)
