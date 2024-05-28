import pygame
from food import Food
from snake import Snake
from direction import Direction


class GameBoard:
    def __init__(self):
        """
        Initializes a GameBoard object.
        """
        pygame.init()
        self.__screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("COMP 3522 Assignment 1 - Snake Game")
        self.__screen.fill((20, 20, 20))

        # initialize game entities
        self.__food = Food(self.__screen)
        self.__snake = Snake(self.__screen)
        self.__score = 0

    def run(self):
        """
        Runs the game. The game is paused (game over) when the snake collides with the wall or itself.
        The game is resumed when the user presses the space bar.
        The Snake can be controlled by the arrow keys and can be set to autopilot mode by pressing 'a'.
        A scoreboard is displayed on the top right of the screen window.
        """
        clock = pygame.time.Clock()
        fps = 15
        game_running = True
        game_paused = False
        while game_running:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                if event.type == pygame.KEYDOWN:
                    direction_map = {
                        pygame.K_UP: Direction.UP,
                        pygame.K_DOWN: Direction.DOWN,
                        pygame.K_LEFT: Direction.LEFT,
                        pygame.K_RIGHT: Direction.RIGHT,
                    }
                    if not game_paused:
                        if event.key in direction_map:
                            self.__snake.direction = direction_map[event.key]
                        elif event.key == pygame.K_a:
                            # toggle auto pilot mode by pressing 'a'
                            self.__snake.auto_pilot = not self.__snake.auto_pilot
                            print(
                                f"Auto pilot mode {'activated' if self.__snake.auto_pilot else 'deactivated'}"
                            )
                    else:
                        if event.key == pygame.K_SPACE:
                            game_paused = False
                            self.__score = 0
                            self.__snake = Snake(self.__screen)
                            self.__food = Food(self.__screen)

            try:
                if not game_paused:
                    self.__update()
                    self.__display_score()
            except Exception as e:
                game_paused = True
                self.__display_game_over(e)

    def __update(self):
        """
        Updates the game entities and checks for collision between the snake and food.
        Moves the snake and updates the food position if the snake collides with the food.
        Update the score if the snake collides with the food.
        :precondition: snake and food must be initialized
        :postcondition: snake and food are updated
        :raises Exception: if the snake collides with the wall or itself
        """
        # update display
        pygame.display.update()

        # clear screen
        self.__screen.fill((20, 20, 20))

        # draw entities
        self.__draw_entities([self.__food, self.__snake])
        self.__snake.move(self.__food)
        # pass over Snake segment positions to Food so that
        # Food can reset its position correctly when collided
        self.__food.set_snake_position(self.__snake.get_positions())

        # check for collision between snake and food and update entities
        # update the score if Snake collides with food
        if self.__snake.is_collided(self.__food):
            for entity in [self.__food, self.__snake]:
                entity.collided()
            self.__score += 1

        pygame.display.flip()

    def __display_game_over(self, exception):
        """
        Displays the game over screen.
        :param exception: Exception object
        """
        print(f"Game Over: {exception}")

        # Game over title
        title_font = pygame.font.SysFont("Arial", 100)
        title = title_font.render("Game Over", True, (255, 255, 255))
        text_rect = title.get_rect()
        text_rect.center = (
            self.__screen.get_width() // 2,
            self.__screen.get_height() // 2 - 40,
        )
        self.__screen.blit(title, text_rect)

        # Play again subtitle
        subtitle_font = pygame.font.SysFont("Arial", 30)
        subtitle = subtitle_font.render(
            f"Score: {self.__score} points!", True, (255, 255, 255)
        )
        subtitle_rect = subtitle.get_rect()
        subtitle_rect.center = (
            self.__screen.get_width() // 2,
            self.__screen.get_height() // 2 + 40,
        )
        self.__screen.blit(subtitle, subtitle_rect)

        # Play again text
        play_again_font = pygame.font.SysFont("Arial", 30)
        play_again = play_again_font.render(
            "Press Space to Play Again", True, (255, 255, 255)
        )
        play_again_rect = play_again.get_rect()
        play_again_rect.center = (
            self.__screen.get_width() // 2,
            self.__screen.get_height() - 100,
        )
        self.__screen.blit(play_again, play_again_rect)

        pygame.display.flip()

    def __display_score(self):
        """
        Display a scoreboard on the top right of the screen window. The score is the size of the Snake's body
        and is updated when Snake collides (eats) the Food object.
        """
        score_font = pygame.font.SysFont("Arial", 30)
        score = score_font.render(f"Score: {self.__score}", True, (255, 255, 255))
        text_rect = score.get_rect()
        text_rect.center = (self.__screen.get_width() - 75, 25)
        self.__screen.blit(score, text_rect)
        pygame.display.flip()

    @staticmethod
    def __draw_entities(entities):
        """
        Draws the entities on the screen.
        :param entities: list of Entity objects
        """
        for entity in entities:
            entity.draw()
