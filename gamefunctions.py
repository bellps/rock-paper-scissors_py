from os import system

def chooseUser():
    player = (input('I choose: ')).lower()

    if player != 'r' and player != 'p' and player != 's':
        print("Invalid option! Type 'r' for rock, 'p' for paper or 's' to scissors.\n")
        return chooseUser()

    else:
        return player

def choosePc(chosen):
    if chosen == 1:
        print("""
               +-------------------------------------------+
               |                            _______        |
               |                        ---'   ____)____   |
               |                                  ______)  |
               |  The computer chose              _______) |
               |                                 _______)  |
               |                        ---.__________)    |
               |                                           |
               +-------------------------------------------+
        """)
        computer_op = 'p'

    elif chosen == 2:
        print("""
               +-------------------------------------------+
               |                            _______        |
               |                        ---'   ____)       |
               |                              (_____)      |
               |  The computer chose          (_____)      |
               |                              (____)       |
               |                        ---.__(___)        |
               |                                           |
               +-------------------------------------------+
        """)
        computer_op = 'r'

    else:
        print("""
               +-------------------------------------------+
               |                            _______        |
               |                        ---'   ____)____   |
               |                                  ______)  |
               |  The computer chose           __________) |
               |                              (____)       |
               |                        ---.__(___)        |
               |                                           |
               +-------------------------------------------+
        """)
        computer_op = 's'
    
    return computer_op


def winner(player, computer):
    if player == computer:
        return "IT'S A TIE! :O\n"

    elif player == 'r' and computer == 'p':
        return "I got wrapped! :(\n"

    elif player == 'p' and computer == 'r':
        return "I WON! BD\n"

    elif player == 's' and computer == 'r':
        return "I got smashed! :(\n"

    elif player == 'r' and computer == 's':
        return "I WON! BD\n"

    elif player == 's' and computer == 'p':
        return "I WON! BD\n"

    else:
        return "I got cut! :(\n"

def playAgain(): 
    again = (input("Wanna play again (Y/N)? ")).lower()
    
    if again == 'y':
        system('cls')
        return True

    elif again == 'n':
        return False

    else:
        print("Invalid option!\n")
        return playAgain()