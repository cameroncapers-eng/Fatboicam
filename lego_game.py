import pgzrun  # type: ignore
from pgzero.builtins import screen, keyboard  # type: ignore
from pygame import Rect  # type: ignore
from random import randint

WIDTH = 800
HEIGHT = 600
TITLE = "LEGO Brick Adventure"

# Player
player = Rect(380, 280, 40, 40)

# LEGO brick
brick = Rect(
    randint(50, 750),
    randint(50, 550),
    30,
    20
)

score = 0


def draw():
    screen.clear()
    screen.fill((120, 200, 255))  # Blue sky

    # Draw LEGO character
    screen.draw.filled_circle(
        (player.x + 20, player.y),
        15,
        "yellow"
    )
    screen.draw.filled_rect(
        player,
        "yellow"
    )

    # Draw LEGO brick
    screen.draw.filled_rect(
        brick,
        "red"
    )

    # Display score
    screen.draw.text(
        "LEGO Bricks: " + str(score),
        (20, 20),
        color="black",
        fontsize=35
    )


def update():
    global score

    # Move LEGO character
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    # Keep player inside the screen
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH
    if player.top < 0:
        player.top = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT

    # Collect brick
    if player.colliderect(brick):
        score += 1
        brick.x = randint(50, WIDTH - 50)
        brick.y = randint(50, HEIGHT - 50)


pgzrun.go()