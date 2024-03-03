import random as rd
import matplotlib.pyplot as plt

total_funds = 10000     # money in hand
wager_amount = 100      # betting amount
total_plays = 1000      # number of times the player bets

def roll():
    dice = rd.randint(1,100)
    print(dice)
    if dice <= 51:
        return False
    else:
        return True


def play(total_funds, wager_amount, total_plays):
    Play_num = []
    Funds = []

    play = 1

    while play <= total_plays:
        if roll():
            total_funds += wager_amount
        else:
            total_funds -= 100
        
        Play_num.append(play)
        Funds.append(total_funds)
        play += 1
    
    plt.plot(Play_num, Funds)
    