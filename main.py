import pygame

pygame.init()

# display the size of the wondow and renamed it
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hangman")

word = "PYTHON"
hidden_word ="_" * len(word)

#creating the font for the text
font = pygame.font.Font(None,50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #clear the screen
    screen.fill("white")

    #create the text
    text = font.render(hidden_word, True, "black")
    
    #draw the text
    screen.blit(text, (300,300))

    pygame.display.flip()

pygame.quit()
