import random

balance = 500
print("PLINKO GAME")
def play_plinko():
    global balance
    print("Balance: ", balance)
    
    betamount = int(input("Bet Amount: "))
    
    if betamount < 50:
        print("Bet must be 50 or higher")
        return
    elif betamount > balance:
        print("Not enough points")
        return

    subtract = balance - betamount
    betmultiplier = betamount / 50

    print("                        |")
    print("                      | o |")
    print("                    | o | o |")
    print("                  | o | o | o |")
    print("                | o | o | o | o |")
    print("              | o | o | o | o | o |")
    print("            | o | o | o | o | o | o |")
    print("          | o | o | o | o | o | o | o |")
    print("        | o | o | o | o | o | o | o | o |")
    print("      | o | o | o | o | o | o | o | o | o |")
    print("    | o | o | o | o | o | o | o | o | o | o |")
    print("  | o | o | o | o | o | o | o | o | o | o | o |")
    print("|0 |25 |45 |75 |100 |150 |100 | 75 | 45 | 25 | 0|")

    rows = 14
    position = 6.5
    scores = [0, 25, 45, 75, 100, 150, 100, 75, 45, 25, 0]

    for _ in range(rows):
        position += random.choice([-0.5, 0.5])
    
    final_pos = min(max(round(position), 0), 10)
    fprize = scores[final_pos] * betmultiplier
    balance = subtract + fprize

    print("\tYou Win: ", fprize)
    


while balance >= 50:
    play_plinko()

print("Not enough points.")
