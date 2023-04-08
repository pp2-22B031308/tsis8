import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLOCK_SIZE = 5
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')


# Define the Snake class
class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = BLOCK_SIZE

    def move(self, dx, dy):
        self.x += dx * self.size
        self.y += dy * self.size

    def draw(self):
        pygame.draw.rect(SCREEN, WHITE, (self.x, self.y, self.size, self.size))


# Create an instance of the Snake class
snake = Snake()


def main():
    running = True
    while running:
        SCREEN.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the snake
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake.move(-1, 0)
        elif keys[pygame.K_RIGHT]:
            snake.move(1, 0)
        elif keys[pygame.K_UP]:
            snake.move(0, -1)
        elif keys[pygame.K_DOWN]:
            snake.move(0, 1)

            def draw(self):
                # Draw the snake
                for segment in self.body:
                    pygame.draw.rect(SCREEN, WHITE, (segment[0], segment[1], self.size, self.size))

            def collide_with_wall(self):
                # Check if the snake collided with the walls
                if self.x < 0 or self.x >= WIDTH or self.y < 0 or self.y >= HEIGHT:
                    return True
                return False

            def collide_with_food(self, food_x, food_y):
                # Check if the snake collided with the food
                if self.x == food_x and self.y == food_y:
                    return True
                return False

            def grow(self):
                # Add a new segment to the snake's body
                self.body.append((self.x, self.y))

        # Define the Food class
        class Food:
            def __init__(self):
                self.x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
                self.y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
                self.size = BLOCK_SIZE

            def draw(self):
                # Draw the food
                pygame.draw.rect(SCREEN, RED, (self.x, self.y, self.size, self.size))

        # Create instances of the Snake and Food classes
        snake = Snake()
        food = Food()

        def main():
            running = True
            while running:
                SCREEN.fill(BLACK)

                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and snake.dx != 1:
                            snake.dx = -1
                            snake.dy = 0
                        elif event.key == pygame.K_RIGHT and snake.dx != -1:
                            snake.dx = 1
                            snake.dy = 0
                        elif event.key == pygame.K_UP and snake.dy != 1:
                            snake.dx = 0
                            snake.dy = -1
                        elif event.key == pygame.K_DOWN and snake.dy != -1:
                            snake.dx = 0
                            snake.dy = 1

                # Move the snake
                snake.move()

                # Check for collisions with the walls
                if snake.collide_with_wall():
                    running = False

                # Check for collisions with the food
                if snake.collide_with_food(food.x, food.y):
                    food = Food()
                    snake.grow()

                # Draw the snake and the food
                snake.draw()
                food.draw()


