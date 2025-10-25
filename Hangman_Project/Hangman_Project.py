

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
            print(f'[{i+1}] {categories[i]}')
            
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

choose_word()
# Take the choosen category and pick a word for the game


# Ask the user to pick a letter



