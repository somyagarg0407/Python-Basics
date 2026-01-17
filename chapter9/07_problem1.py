import random

def game():
    print("you are playing the game")
    score=random.randint(1,100)  # randint use for random between two integers
    with open("hiscore.txt") as f:
        hiscore=f.read() #ye step karna jaruri kyun tha
        if (hiscore!=""):
            hiscore=int(hiscore)  #int lagaya kyunki file se data as string read and writehota hai
        else:
            hiscore=0

    print(f"your scor is {score}")
    if(score>hiscore):
        with open("hiscore.txt","w") as f:  #why w is imp here
            f.write(str(score))

    return score    #ye return kisko karte hai apan
    
game()
