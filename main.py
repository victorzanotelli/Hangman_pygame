import pygame
# Game loop:
# 1. Check events
# 2. Update game state
# 3. Draw everything
# 4. Display the result
# 5. Repeat
                                                                                  
pygame.init()                                                                
                                                                              
# Create the game window and store it in the "screen" variable                 
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hangman")

# Defining the secret word
word = "PYTHON"

# Create the hidden version of the secret word
hidden_word = ["_"] * len(word)
#List for the wrong answer
wrong_guesses =[]
#List the already guessed letter
guessed_letter = []

# Create a font and set its size
font = pygame.font.Font(None, 50)
small_font =pygame.font.Font(None, 35)

running = True
game_won = False

while running:

    # Handle events
    for event in pygame.event.get():

        #Handle the event "quiting the game"
        if event.type == pygame.QUIT:
            running = False

        # Handle the event "wich letter from keyboard is pressed"
        if event.type == pygame.KEYDOWN and not game_won:
            #Only accept letter
            if event.unicode.isalpha():

                letter = event.unicode.upper()

                if letter not in guessed_letter :
                    guessed_letter.append(letter)

                    #Check if the letter is in the secret word
                    if letter in word :
                        #Reveal the letter in every matching position
                        for index, character in enumerate(word):
                            if character == letter:
                                hidden_word[index] = letter
                        if "_" not in hidden_word :
                            game_won = True      
                    #Add the wrong guesses to list 
                    else:
                        wrong_guesses.append(letter)        

    # Clearing the screen
    screen.fill("white")

    #Convert the hidden  word list into a string
    display_word =" ".join(hidden_word)
    display_wrong_guesses = " ".join(wrong_guesses)

    # Create the text
    text = font.render(display_word, True,"black")
    wrong_text = small_font.render(display_wrong_guesses, True, "red")

    # Draw the text 
    screen.blit(text,(300,300))
    screen.blit(wrong_text,(100,500))

    #Display winning message
    if game_won == True:
        win_text = font.render("YOU WIN BAD MOTHAFUCKA !", True, "Green")
        screen.blit(win_text,(200,150))

    # Show on the screen
    pygame.display.flip()

pygame.quit()