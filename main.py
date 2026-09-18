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

# Create a font and set its size
font = pygame.font.Font(None, 50)

running = True

while running:

    # Handle events
    for event in pygame.event.get():

        #Handle the event "quiting the game"
        if event.type == pygame.QUIT:
            running = False

        # Handle the event "wich letter from keyboard is pressed"
        if event.type == pygame.KEYDOWN:
            letter = event.unicode.upper()

            #Check if the letter is in the secret word
            if letter in word :
                #Reveal the letter in every matching position
                for index, character in enumerate(word):
                    if character == letter:
                        hidden_word[index] = letter

    # Clearing the screen
    screen.fill("white")

    #Convert the hidden  word list into a string
    display_word =" ".join(hidden_word)

    # Create the text
    text = font.render(display_word, True,"black")

    # Draw the text 
    screen.blit(text,(300,300))

    # Show on the screen
    pygame.display.flip()

pygame.quit()