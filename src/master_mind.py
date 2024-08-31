import random
# from pygame import *
import os

black = '\033[30m'
orange = '\033[38;5;214m'
purple = '\033[95m'
cyan = '\033[96m'
darkcyan = '\033[36m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
bold = '\033[1m'
underline = '\033[4m'
end = '\033[0m'

all_colors = ['red', 'blue', 'black', 'purple', 'green', 'yellow', 'orange', 'white']

print('''
##     ##       ###        ######     ########    ########    ########     ##     ##    ####    ##    ##    ########  
###   ###      ## ##      ##    ##       ##       ##          ##     ##    ###   ###     ##     ###   ##    ##     ## 
#### ####     ##   ##     ##             ##       ##          ##     ##    #### ####     ##     ####  ##    ##     ## 
## ### ##    ##     ##     ######        ##       ######      ########     ## ### ##     ##     ## ## ##    ##     ## 
##     ##    #########          ##       ##       ##          ##   ##      ##     ##     ##     ##  ####    ##     ## 
##     ##    ##     ##    ##    ##       ##       ##          ##    ##     ##     ##     ##     ##   ###    ##     ## 
##     ##    ##     ##     ######        ##       ########    ##     ##    ##     ##    ####    ##    ##    ########  
''')

print(f'''
There are 8 colors namely {', '.join(all_color.title() for all_color in all_colors)}
The computer will choose a pattern of any four color balls from the following colors.
The same color may(not) be repeated.
You will have 10 guesses to guess the color code.
If you guess the {bold}{underline}correct{end} color with the {bold}{underline}correct{end} position you will get a {red}red peg{end}
If you guess the {bold}{underline}correct{end} color with the {bold}{underline}correct{end} position, you will get a white peg
You may get more than one pegs depending on the number of right color and position guesses
But remember that if the computer has chosen a particular color a single time, and you write it more than 1 time, 
you will get only one red or white peg depending on the situation.''')
all_colors_dic = {'1': 'red', '2': 'blue', '3': 'black', '4': 'purple', '5': 'green', '6': 'yellow', '7': 'orange',
                  '8': 'white'}

# add a while loop for next input

while True:
    mp_sp = input(f'''
{bold}Which mode would you like to choose- Multiplayer or Single Player {green}(MP/SP){end}
In a multi player mode one of the players will set up the color code while the other person will try to guess it.
While in single player, the computer will choose the color code which you will have to guess
''').lower()
    if mp_sp == 'sp':
        comcol1 = random.choice(all_colors)
        comcol2 = random.choice(all_colors)
        comcol3 = random.choice(all_colors)
        comcol4 = random.choice(all_colors)
        print('Computer has chosen its color code, your turn to guess it.')
        break
    elif mp_sp == 'mp':
        # Player 1 creates the color code
        print(f'''
Choose your Colour code for your opponent. Hide it from him the screen will be cleared later.
Colour guess code
1. Type 1 for {red}Red{end}
2. Type 2 for {blue}Blue{end}
3. Type 3 for {black}Black{end}
4. Type 4 for {purple}Purple{end}
5. Type 5 for {green}Green{end}
6. Type 6 for {yellow}Yellow{end}
7. Type 7 for {orange}Orange{end}
8. Type 8 for White''')

        while True:
            comcol1_no = input('First color: ').lower()
            comcol1 = all_colors_dic.get(comcol1_no, comcol1_no)
            if comcol1 in all_colors:
                break
            else:
                print(red + 'That is not a color or a correct color code number. Let us try it again' + end)
        while True:
            comcol2_no = input('Second color: ').lower()
            comcol2 = all_colors_dic.get(comcol2_no, comcol2_no)
            if comcol2 in all_colors:
                break
            else:
                print(red + 'That is not a color or a correct color code number. Let us try it again' + end)
        while True:
            comcol3_no = input('Third color: ').lower()
            comcol3 = all_colors_dic.get(comcol3_no, comcol3_no)
            if comcol3 in all_colors:
                break
            else:
                print(red + 'That is not a color or a correct color code number. Let us try it again' + end)
        while True:
            comcol4_no = input('Forth color: ').lower()
            comcol4 = all_colors_dic.get(comcol4_no, comcol4_no)
            if comcol4 in all_colors:
                break
            else:
                print(red + 'That is not a color or a correct color code number. Let us try it again' + end)
        correct_color_code = [comcol1, comcol2, comcol3, comcol4]
        print(f"{green}Your color code is: {', '.join(correct_color_code)}{end} ")
        input(f'{green}Pass the laptop to the other player and then press enter{end}')
        print(f'{red}Player 2: It is now your turn to guess the code{end}')
        break
    else:
        print(f'{red}It is not a command. The only commands are "mp/sp"{end}')

correct_color_code = [comcol1, comcol2, comcol3, comcol4]

guess = 0
all_guess_pegs = []
all_guess_col = []  # a list which has lists of colors inside it
while guess <= 10:
    print(f'''Colour guess code
1. Type 1 for {red}Red{end}
2. Type 2 for {blue}Blue{end}
3. Type 3 for {black}Black{end}
4. Type 4 for {purple}Purple{end}
5. Type 5 for {green}Green{end}
6. Type 6 for {yellow}Yellow{end}
7. Type 7 for {orange}Orange{end}
8. Type 8 for White''')

    pegs = []
    for index, color_guess in enumerate(all_guess_col):
        if all_guess_col:
            guess_pegs = all_guess_pegs[index]
            print(f"{green}[{index + 1}st guess: "
                  f"{', '.join(color.title() for color in color_guess)}] ; [Pegs: {', '.join(guess_pegs)}] {end}")
    while True:
        col1_no = input('First color: ').lower()
        col1 = all_colors_dic.get(col1_no, col1_no)
        if col1 in all_colors:
            break
        else:
            print(red + 'That is not a color or a correct color code number. Let us try it again' + end)
    while True:
        col2_no = input('Second color: ').lower()
        col2 = all_colors_dic.get(col2_no, col2_no)
        if col2 in all_colors:
            break
        else:
            print(red + 'That is not a color or a correct color code number. Let us try it again' + end)
    while True:
        col3_no = input('Third color: ').lower()
        col3 = all_colors_dic.get(col3_no, col3_no)
        if col3 in all_colors:
            break
        else:
            print(red + 'That is not a color or a correct color code number. Let us try it again' + end)
    while True:
        col4_no = input('Forth color: ').lower()
        col4 = all_colors_dic.get(col4_no, col4_no)
        if col4 in all_colors:
            break
        else:
            print(red + 'That is not a color or a correct color code number. Let us try it again' + end)

    color_code = [col1, col2, col3, col4]
    all_guess_col.append(color_code)
    print(bold + blue + f"\nYour color code guess is {', '.join(color.title() for color in color_code)}\n" + end)

    guess += 1
    if color_code == correct_color_code:
        print(bold + 'Perfect! You won' + end)
        break
    for index, col in enumerate(color_code):
        if col in correct_color_code:
            if index == correct_color_code.index(col):
                pegs.append('Red Peg')
            else:
                pegs.append('White Peg')

    # If someone mentions same color multiple times but it exists less times than mentioned
    # we want to remove the white pegs added for no reason
    unique_color_code = list(set(color_code))
    for col in unique_color_code:
        if col in correct_color_code:
            if color_code.count(col) > correct_color_code.count(col):
                for no in range(color_code.count(col) - correct_color_code.count(col)):
                    # try:
                    pegs.remove('White Peg')
                    # except ValueError:
                    #     pass

    if guess < 9:
        if pegs:
            output = ''
            for peg in pegs:
                if peg == 'Red Peg':
                    output += red + peg + end + '  '
                else:
                    output += peg + '  '
            print(f"Your pegs:  {output}")
            print('Keep Going You are close')
        else:
            print('None of the color matches the computer color')
    if pegs:
        all_guess_pegs.append(pegs)
    print(f'Number of guesses: {guess}')
else:
    print('You are out of guesses the computer won')
    print(bold + blue + f"\nThe correct color code was {', '.join(color.title() for color in correct_color_code)}\n" +
          end)

