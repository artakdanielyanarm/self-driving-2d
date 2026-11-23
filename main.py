
"""Assignment 1: Make a Car Drive Itself - starter code.

Run it with: python main.py
Keys: Left/Right arrows = steer
      A = autopilot on/off
      R = reset
      Esc = quit
"""

import math
import pygame


# ---------------- Settings ----------------
WIDTH, HEIGHT = 900, 600
BG_COLOR = (235, 235, 225)       # light floor
LINE_COLOR = (40, 40, 40)        # dark line the car must follow
CAR_COLOR = (220, 60, 50)
SENSOR_COLOR = (0, 120, 255)
FPS = 60                         # loop runs 60 times per second
TURN_RATE = 4.0                  # degrees per frame at full steer
START = (450, 115, 0)            # x, y, heading


class Car:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading
        self.speed = 2.0          # pixels per frame

    def move(self, steer):
        """steer: -1.0 = full left, 0.0 = straight, +1.0 = full right."""
        steer = max(-1.0, min(1.0, steer))
        self.heading += steer * TURN_RATE
        rad = math.radians(self.heading)
        self.x += math.cos(rad) * self.speed
        self.y += math.sin(rad) * self.speed

    def draw(self, screen):
        rad = math.radians(self.heading)

        nose = (
            self.x + math.cos(rad) * 14,
            self.y + math.sin(rad) * 14
        )
        left = (
            self.x + math.cos(rad + 2.5) * 10,
            self.y + math.sin(rad + 2.5) * 10
        )
        right = (
            self.x + math.cos(rad - 2.5) * 10,
            self.y + math.sin(rad - 2.5) * 10
        )

        pygame.draw.polygon(screen, CAR_COLOR, [nose, left, right])


def make_track():
    """Draw the track once on its own surface, so sensors can read it."""
    track = pygame.Surface((WIDTH, HEIGHT))
    track.fill(BG_COLOR)
    pygame.draw.ellipse(track, LINE_COLOR, (100, 100, 700, 400), 30)
    return track


# ---------------- SENSE ----------------
def sensor_points(car):
    """Return a list of (x, y) points just ahead of the car."""
    # TODO Step 8
    return []


def read_sensors(car, track):
    """Return one True/False per sensor point: is it on the dark line?"""
    # TODO Step 8
    return []


# ---------------- THINK ----------------
def brain(readings):
    """Turn the sensor readings into a steering value from -1.0 to +1.0."""
    # TODO Step 9
    return 0.0


# ---------------- Manual driving ----------------
def keyboard_steer():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        return -1.0

    if keys[pygame.K_RIGHT]:
        return 1.0

    return 0.0


def on_line(track, x, y):
    """True if the point is inside the window and on the dark line."""
    if not (0 <= x < WIDTH and 0 <= y < HEIGHT):
        return False

    r, g, b, _ = track.get_at((int(x), int(y)))
    return r + g + b < 300


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Self-driving 2D car")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 26)

    track = make_track()
    car = Car(*START)

    autopilot = False
    frames_off_line = 0
    steer = 0.0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_a:
                    autopilot = not autopilot

                elif event.key == pygame.K_UP:
                    car.speed += 0.5

                elif event.key == pygame.K_DOWN:
                    car.speed = max(0.0, car.speed - 0.5)

                elif event.key == pygame.K_r:
                    car = Car(*START)
                    frames_off_line = 0

        readings = read_sensors(car, track)  # SENSE
        steer = brain(readings) if autopilot else keyboard_steer()  # THINK
        car.move(steer)  # ACT

        if not on_line(track, car.x, car.y):
            frames_off_line += 1

        screen.blit(track, (0, 0))
        car.draw(screen)

        for (sx, sy) in sensor_points(car):
            pygame.draw.circle(
                screen, SENSOR_COLOR, (int(sx), int(sy)), 4
            )

        mode = "AUTOPILOT" if autopilot else "MANUAL"
        text = f"{mode}   steer {steer:+.2f}   frames off line: {frames_off_line}"

        screen.blit(font.render(text, True, (20, 20, 20)), (12, 12))
        screen.blit(
            font.render(
                "[A] autopilot                     [R] reset   [Esc] quit",
                True,
                (90, 90, 90)
            ),
            (12, 36)
        )

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
