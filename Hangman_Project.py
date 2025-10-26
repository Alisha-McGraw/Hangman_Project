

#Wrong guesses count
hangman_pics = [
    
    # 0 
    '''
    -----
    |   |
        |
        |
        |
        |
    =========
    ''',
    # 1 
    '''
    -----
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    # 2 
    '''
    -----
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    # 3 
    '''
    -----
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''',
    # 4
    '''
    -----
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    ''',
    # 5 
    '''
    -----
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    ''',
    # 6 
    '''
    -----
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    '''
]

#Dictionary of word choices for the user
word_categories = {
    'ANIMAL': ['ELEPHANT', 'MONKEY', 'PENGUIN', 'RHINOCEROS', 'DOLPHIN'],
    'FRUIT': ['PINEAPPLE', 'STRAWBERRY', 'GRAPES', 'APPLE', 'BLUEBERRY'],
    'SPORT': ['BASKETBALL', 'FOOTBALL', 'BASEBALL', 'VOLLEYBALL', 'SOCCER']
}

# Maximum number of incorrect guesses allowed
max_attemps = 6

# Ask the user to choose a category
def choose_word():
    '''
    Asks the user to select a category, then a word number within that category.
    Returns the chosen word as an uppercase string.
    '''
    print('\n Choose a Category')
    
    # Get category names and sorts them 
    categories = sorted(list(word_categories.keys()))
    num_categories = len(categories)
    
    # Select Category
    while True:
        print('\nAvailable Categories:')
        for i in range(num_categories):
            print(f'{i+1}. {categories[i]}')
            
        category_choice = input(f'Select a category number (1-{num_categories}): ').strip()
        
        try:
            category_index = int(category_choice) - 1
            if 0 <= category_index < num_categories:
                selected_category = categories[category_index]
                word_options = word_categories[selected_category]
                break
            else:
                print('Invalid category number. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    # Take the choosen category and pick a word for the game
    num_words = len(word_options)
    print(f'\nCategory "{selected_category}" selected. It has {num_words} possible words.')
    
    while True:
        
        word_choice = input(f'Select a word number (1-{num_words}) to choose your word: ').strip()
        
        try:
            word_index = int(word_choice) - 1
            # Check if the chosen index is valid
            if 0 <= word_index < num_words:
                chosen_word = word_options[word_index].upper()
                print(f'A {selected_category} word has been chosen for you.')
                return chosen_word
            else:
                print('Invalid number input. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number.')

def display_game_state(attempts_left, guessed_word_list, guessed_letters):
    '''
    Prints the current state of the game.
    '''
    # The index for the drawing 
    game_stage = max_attemps - attempts_left
    print(hangman_pics[game_stage]) # Draw the hangman
    
    # Displays the current word progress
    print('Word:', '' .join(guessed_word_list))
    # Displays already guessed letters
    print('Guessed letters:', ', '.join(guessed_letters))
    # Displays the amount to attempts remaining
    print(f'Attempts remaining: {attempts_left}')

# Ask the user to pick a letter
def play_game(word):
        
    word_to_guess = word          
    guessed_letters = []          
    attempts_left = max_attemps       
    guessed_word_list = ['_'] * len(word_to_guess)
    
    print('\n Hangman Game Started!')
    print(f'Your word has {len(word_to_guess)} letters.')

    while attempts_left > 0:

        display_game_state(attempts_left, guessed_word_list, guessed_letters)

        print(f'Attempts left: {attempts_left}') 

        # Checks for winner condition
        if '_' not in guessed_word_list:
            print('\n CONGRATULATIONS! You guessed the word correctly!')
            return
        
        # Validate user input
        while True:
           
            guess = input('Guess a letter: ').upper().strip() 
            
            # Checks if input is a single letter (A-Z)
            if len(guess) != 1 or not ('A' <= guess <= 'Z'):
                print('Invalid input. Please enter a single letter (A-Z).')
                continue
            
            # Checks if letter was already guessed
            if guess in guessed_letters:
                print(f'You already guessed "{guess}". Try a different letter.')
            else:
                guessed_letters.append(guess)
                break

        # Checks if the guessed letter is in the word
        if guess in word_to_guess:
            print(f'Good guess! "{guess}" is in the word.')
            
            # Update the guessed_word_list
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word_list[i] = guess
        else:
            print(f'Incorrect! "{guess}" is NOT in the word.')
            attempts_left -= 1 
    
    # Checks for loss condition
    display_game_state(attempts_left, guessed_word_list, guessed_letters)
    print('\n Game over! You are out of attempts.')
    print(f'The word was: {word_to_guess}')


print('Welcome to Hangman!')
while True:
    secret_word = choose_word()
    game_finished = play_game(secret_word)
            
    play_again = input('\nDo you want to play again? (yes/no): ').lower().strip()
        
    if play_again != 'yes':
        print("Thanks for playing! Goodbye.")
        break


