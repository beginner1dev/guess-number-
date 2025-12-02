import random

while True:
    guess_pc = random.randint(1 , 99)
    #print(guess_pc)
    count=0
    print('The computer chose a number.')

    guess_me= int(input('If you can guess!!!!:  ')) 

    while guess_pc != guess_me:
        count = count + 1

        if  guess_me > guess_pc:
            print('guess a smaller number!')
            
        elif guess_me < guess_pc:
            print('guess a bigger number!')

        guess_me = int(input('guess again:  ')) 

    print('wwwowwwwwwww!!!!!! you did it. you rock!!!!!!')
    print('Number of your guesses:', count)

    play_again = input('Do you want to play again?!(yes/no)')
    if play_again.lower() != 'yes':
        print('I was happy that we played together.Goodbye for now.')
        break
