import random 
import logging
import os
logging.basicConfig(filename='erros.log', level=logging.DEBUG, filemode='a', 
                    format='%(levelname)s - %(message)s - %(asctime)s')
number_user = -1

def number_randomic():
    return random.randint(0, 100)
    
def toplay_game(number,number_randomic):
    while number != number_randomic:
        try:
            number = int(input('Guess a number between 0 and 100: '))
            if number > number_randomic:
                print('number higher than expected')
            elif number < number_randomic:
                print('number smaller than expected')
            else:
                print(f'Nice, you are right the number {number_randomic}')
                to_play_again()    
        except ValueError as error:
            print('Only numbers!')
            logging.warning(error)
                
def ask_toplay():
    play_again = input('Would you like to play again? (y/n) ')
    return play_again

def play_continue(is_play):
    if is_play == 'y':
        toplay_game(number_user,number_randomic())
    elif is_play == 'n':
        print('Game finished, by! ©Sautier Alexsander')
        exit()
    else:
        is_play = ask_toplay()
        play_continue(is_play)    

def to_play_again():
    is_play = ask_toplay()
    try:
        play_continue(is_play)
            
    except ValueError as error:
        print('Only numbers!')
        logging.warning(error)
        


enter = input(' welcome to this game, press "ENTER" to start!')
if enter == '':
    toplay_game(number_user,number_randomic())