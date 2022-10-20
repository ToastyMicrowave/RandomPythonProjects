def random_word_chooser():
    import random
    with open("C:\Python Projects\lulw.txt", "r") as file:
        lines = file.readlines()
        return (random.choice(lines)).strip().lower()
def hangman_ascii_art(guesses):
    
    HANGMANPICS = ['''
     +---+
     |   |
         |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========''']
    for x in range(0, 7):
        if guesses == x:
            return (HANGMANPICS[x])

game_on = True

while game_on:
    guesses = 6
    game_ongoing = True
    word = random_word_chooser()  
    hangman = "_ " * len(word)
    print("Welcome to a game of Hangman!\nTo get started, please guess a letter!\nRemember, you can type \"quit\" at any time to quit.")
    user_input = set()
    print(hangman_ascii_art(guesses))
    print(hangman)
    while guesses > 0 and game_ongoing:
        counting_guesses = True
        result = []
        letter_input = input(">>> ").lower()
        if letter_input == "quit":
            game_on = False
            game_ongoing = False
            break
        if letter_input in word:
                counting_guesses = False
        if letter_input not in user_input:
            if len(letter_input) == 1:
                user_input.add(letter_input)
            else:
                print("You cannot guess more than one letter at a time! please guess again.")
                continue
        else:
            print("You have already guessed that letter! please guess a different one!")
            continue
        for i in range(0, len(word)):
            if word[i] in user_input:
                result.append(word[i])
            elif word[i] not in user_input:
                if hangman[i] == "_":
                    result.append(hangman[i])
                else:
                    result.append(hangman[i + 1])
        if "".join(result) == word:
            print(hangman_ascii_art(guesses))
            print("The word was " + ("".join(result)) + "!")
            another_game_yes_or_no = input("Congratulations! You got the word right! It took you " + str(6 - guesses) + " guesses to do so.\nWould you like to play another game?\n>>> ").lower()
            while game_on:
                if another_game_yes_or_no == "yes":
                    game_on = True
                    game_ongoing = False
                    break
                elif another_game_yes_or_no == "no":
                    game_ongoing = False
                    game_on = False
                else:
                    print("invalid input, please try again")
                    another_game_yes_or_no = input("Would you like to play another game?\n>>> ").lower()
        else:
            if counting_guesses:
                guesses -= 1
            print(hangman_ascii_art(guesses))
            print(" ".join(result))
            if guesses > 0:
                print("You have " + str(guesses) + " guesses remaining.")
            if guesses == 0:
                another_game_yes_or_no = input("Oh no! You ran out of guesses!\nThe word was " + word + "!\nWould you like to play another game?\n>>> ")
                while game_on:
                    if another_game_yes_or_no == "yes":
                        game_on = True
                        game_ongoing = False
                        break
                    elif another_game_yes_or_no == "no":
                        game_ongoing = False
                        game_on = False
                        
                    else:
                        print("invalid input, please try again")
                        another_game_yes_or_no = input("Would you like to play another game?\n>>> ").lower()


