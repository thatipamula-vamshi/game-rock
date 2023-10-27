import random
while True:
    
    crazy = ['rock','paper','scissors']

    computer = random.choice(crazy)
    player = None

    while player not in crazy:
        player = input('select rock, paper or scissors: ').lower()
#this is code
    if computer == player:
        print(computer)
        print(player)
        print('Tie!')
    elif player == 'rock':
        if computer == 'paper':
            print(computer)
            print(player)
            print('you lost')
        elif computer == 'scissors':
            print(computer)
            print(player)
            print('you win')
    elif player == 'paper':
        if computer == 'scissors':
            print(computer)
            print(player)
            print('you lost')
        elif computer == 'paper':
            print(computer)
            print(player)
            print('you win')        
    elif player == 'scissors':
        if computer == 'rock':
            print(computer)
            print(player)
            print('you lost')
        elif computer == 'paper':
            print(computer)
            print(player)
            print('you win')
    play_again = input('Do you want to play again? (Yes/NO)').lower()

    if play_again != 'yes':
        break
print('See you again. Bye!')


    




