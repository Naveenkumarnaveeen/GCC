import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BG_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 30

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Load fonts
font = pygame.font.SysFont(None, FONT_SIZE)

# Function to display text on the screen
def display_text(text, x, y):
    text_surface = font.render(text, True, FONT_COLOR)
    screen.blit(text_surface, (x, y))

# Main game loop
def game_loop():
    player_score = 0
    computer_score = 0

    # Initialize player_choice to None
    player_choice = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Clear the screen
        screen.fill(BG_COLOR)

        # Display player and computer choices
        display_text("Your Choice:", 50, 50)
        display_text("Computer's Choice:", 200, 50)

        # Display player and computer scores
        display_text(f"Your Score: {player_score}", 50, 300)
        display_text(f"Computer's Score: {computer_score}", 50, 350)

        # Display winner
        if player_score > computer_score:
            display_text("You Win!", 200, 300)
        elif player_score < computer_score:
            display_text("Computer Wins!", 200, 300)
        else:
            display_text("It's a Tie!", 200, 300)

        # Draw Rock, Paper, Scissors buttons
        for i, choice in enumerate(choices):
            pygame.draw.rect(screen, FONT_COLOR, (50, 100 + i * 100, 100, 50), 2)
            display_text(choice, 70, 115 + i * 100)

        # Get player's move
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for i, choice in enumerate(choices):
            if 50 <= mouse_x <= 150 and 100 + i * 100 <= mouse_y <= 150 + i * 100:
                if pygame.mouse.get_pressed()[0]:
                    player_choice = choice

        # Check if the player made a choice
        if player_choice is not None:
            # Get computer's move
            computer_choice = random.choice(choices)

            # Determine the winner
            if player_choice == "Rock":
                if computer_choice == "Paper":
                    computer_score += 1
                elif computer_choice == "Scissors":
                    player_score += 1
            elif player_choice == "Paper":
                if computer_choice == "Scissors":
                    computer_score += 1
                elif computer_choice == "Rock":
                    player_score += 1
            elif player_choice == "Scissors":
                if computer_choice == "Rock":
                    computer_score += 1
                elif computer_choice == "Paper":
                    player_score += 1

            # Reset player_choice to None for the next round
            player_choice = None

        # Update the display
        pygame.display.update()

        # Set the frame rate
        pygame.time.Clock().tick(60)

# Start the game
game_loop()
