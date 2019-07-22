import random

def get_player_history(human):
    player_history.append(human)
    if len(player_history) == 4:
        del player_history[0]
    return player_history

def get_computer_choice(player_history):
    if (player_history[0] == player_history[1] and player_history[0] == player_history[2])\
    and (player_history[0] == 'rock'):
        computer = 'paper'
    elif (player_history[0] == player_history[1] and player_history[0] == player_history[2])\
    and (player_history[0] == 'paper'):
        computer = 'scissors'
    elif (player_history[0] == player_history[1] and player_history[0] == player_history[2])\
    and (player_history[0] == 'scissors'):
        computer = 'rock'
    else:
        computer = random.choice(['rock', 'paper', 'scissors'])
    return computer
        
def input_human_choice():
    option_list = ['rock', 'paper', 'scissors']
    human = str(input('Make a move! (rock/paper/scissors): ')).lower()
    while human not in option_list:
        print('You must enter "rock," or "paper," or "scissors."')
        human = str(input('Make a move! (rock/paper/scissors): ')).lower()
    return human 

def get_scores_and_win_lose(human, computer, human_score, computer_score):
    win_lose = 0
    if (human == 'rock' and computer == 'paper')\
    or (human == 'paper' and computer == 'scissors')\
    or (human == 'scissors' and computer == 'rock'):
        computer_score += 1
        win_lose = 'lose'
    elif (computer == 'rock' and human == 'paper')\
    or (computer == 'paper' and human == 'scissors')\
    or (computer == 'scissors' and human == 'rock'):
        human_score += 1
        win_lose = 'win'
    elif human == computer:
        win_lose = 'tied'
    return computer_score, human_score, win_lose

player_history = ['','','']
computer_score = 0
human_score = 0
run = 'Y'
print('Welcome to Rock, Paper, Scissors.')
while run == 'Y' or run == 'YES':
    computer = get_computer_choice(player_history)
    human = input_human_choice()
    player_history = get_player_history(human)
    computer_score, human_score, win_lose = get_scores_and_win_lose(human, computer, human_score, computer_score)
    print('You chose ' + human + ' and the computer chose ' + computer + '. You ' + win_lose + '!')
    see_score = str(input('Enter "sc" if you like to see your the scores: ')).upper()
    if see_score == 'SC':
        print('human: ' + str(human_score) + ', computer: ' + str(computer_score) + '.')
    run = str(input('Do you want to play again? (y/n): ')).upper()
print('Thanks, bye!')



