import time
import random

# Input for player ratings
gk = int(input("enter goalkeeper rating 0-99: "))
atk = int(input("enter attackers rating 0-99: "))

# Store original values to reset after each play
original_gk = gk
original_atk = atk

play = random.randint(1, 4) 
attempts = 0
atk_score = 0
gk_score = random.randint(1, 3) # Creates goalkeeper's team score

def goal(gk, atk, atk_score):
    if atk > gk:
        print("GOAL!!!")
        time.sleep(2)
        atk_score += 1
        print("The score is now", gk_score, "-", atk_score)
    else:
        print("Save from the keeper!")
    return atk_score

def freekick():
    print("Its a freekick!")

def pen():
    print("Penalty!")
    
def freeplay():
    print("Its a 1v1!")
    
def longshot():
    print("Shot taken from distance!!!")





print("The sub is coming on at half time and his team is down ", gk_score, " - ", atk_score)
time.sleep(1)

while attempts < 4:
    # Reset atk and gk to their original values at the start of each play
    atk = original_atk
    gk = original_gk
    play = random.randint(1, 4) 
    print("\nChance here for the attacker!")
    time.sleep(2)
    attempts = attempts + 1 # Increase attempt count

    if play == 1:
        atk = int(atk * 1.2) # Boost ATK rating
        freekick()
        time.sleep(2)
        atk_score = goal(gk, atk, atk_score)

    elif play == 2:
        atk = int(atk * 2) # Boost ATK rating
        pen()
        time.sleep(2)
        atk_score = goal(gk, atk, atk_score)

    elif play == 3:
        freeplay()
        time.sleep(2)
        atk_score = goal(gk, atk, atk_score)

    else:
        gk *= 1.3 # Boost GK rating
        longshot()
        time.sleep(2)
        atk_score = goal(gk, atk, atk_score)

print("\nFinal Score:", gk_score, "-", atk_score)
if atk_score > gk_score:
    print("The attacker's team wins!")
elif atk_score < gk_score:
    print("The goalkeeper's team wins!")
else:
    print("It's a draw!")

