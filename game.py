from random import randint as ri
import gamefunctions as f

again = True

while again:
    print("""
    +-----------------------------------------------------------------+
    |   Rock Paper Scissors! Type the letter of the desired option.   |
    +-----------------------------------------------------------------+
    |        _______           _______                _______         |
    |    ---'   ____)      ---'   ____)____       ---'   ____)____    |
    |          (_____)               ______)                ______)   |
    |          (_____)               _______)            __________)  |
    |          (____)               _______)            (____)        |
    |    ---.__(___)       ---.__________)        ---.__(___)         |
    |                                                                 |
    |     Rock (r)            Paper (p)             Scissors (s)      |
    +-----------------------------------------------------------------+
    """)

    player = f.chooseUser()
    computer = f.choosePc(ri(1, 3))

    print(f.winner(player, computer))

    again = f.playAgain()
    
    