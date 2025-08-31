from file_management.SimpleLogger import SimpleLogger
from games.CardGame import CardGame
from datetime import date, datetime

import file_management


game_logger = SimpleLogger(level='DEBUG', log_file="game.log")
card_game = CardGame()
#game_logger.info(card_game.print_deck())
game_logger.debug(card_game.pick_card())


with open('game.log', 'r') as f:
    f_first_line = f.readline()
    f_second_line = f.readline(20)

print(f_first_line)
print(f_second_line)