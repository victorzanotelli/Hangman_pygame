import pygame  #main structure for pygame :                                     1.Check event
#                                                                               2.Update game state         
pygame.init()#                                                                  3.Draw everything
#                                                                               4.Display.flip()
#create the window for the game and renamed it                                  5.Repeat
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hangman")

#Defining the secret word
word = "PYTHON"

#Create the hidden veersion of the secret word
hidden_word = "_ " * len(word)

#Create a font (more or less defining the detail for the display of the text)
font = pygame.font.Font(None, 50)

running = True

while running:

    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Clearing the screen
    screen.fill("white")

    #Create the text
    text = font.render(hidden_word, True,"black")

    #Draw the text 
    screen.blit(text,(300,300))

    #Show on the screen
    pygame.display.flip()

pygame.quit()