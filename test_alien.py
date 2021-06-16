from alien_invasion import AlienInvasion
from alien import Alien

import pytest
import pygame

from functools import reduce

# Fixture
@pytest.fixture
def game():
    return AlienInvasion()

@pytest.fixture
def alien(game):
    return Alien(game)

def imagesAreEqual(img1: pygame.Surface, img2: pygame.Surface):
    pxarr1 = pygame.PixelArray(img1)
    pxarr2 = pygame.PixelArray(img2)
    compared = pxarr1.compare(pxarr2)
    flatten = reduce(lambda accu, i: accu + list(i), compared, [])
    return len(list(filter(lambda x: x != 0xFFFFFF, flatten))) == 0

# Test Alien
def test_init(alien, game):
    assert alien.screen == game.screen
    assert alien.settings == game.settings
    img = pygame.image.load('assets/alien.bmp')
    assert imagesAreEqual(alien.image, img)
    rect = img.get_rect()
    rect.x = rect.width
    rect.y = rect.height
    assert alien.rect == rect
    assert alien.x == float(alien.rect.x)

@pytest.mark.parametrize("x, result", [
    (1280, True),   # Move alien to the rightmost
    (0, True),      # Move alien to the leftmost
    (640, False),   # Move alien to the middle
    (2560, True),   # Move alien outside the screen
    (-640, True),   # Move alien outside the screen
])
def test_check_edges(alien, x, result):
    alien.rect.x = x
    assert (alien.check_edges() == True) == result

@pytest.mark.parametrize("speed, direction, delta", [
    (20.0,     1, 20),    # Positive int speed    + positive direction
    (7.8,      1, 7),     # Positive float speed  + positive direction
    (0.0,      1, 0),     # zero speed            + positive direction
    (-3.0,     1, -3),    # Negtive int speed     + positive direction
    (-5.2,     1, -6),    # Negtive float speed   + positive direction

    (2.0,     -1, -2),    # Positive int speed    + negtive direction
    (10.9,    -1, -11),   # Positive float speed  + negtive direction
    (0.0,     -1, 0),     # zero speed            + negtive direction
    (-33.0,   -1, 33),    # Negtive int speed     + negtive direction
    (-80.795, -1, 80),    # Negtive float speed   + negtive direction

    (2000.0,   1, 2000),  # speed > 1200          + positive direction
    (-2000.0,  1, -2000), # speed < -1200         + positive direction
    (4000.0,  -1, -4000), # speed > 1200          + negtive direction
    (-4000.0, -1, 4000),  # speed < -1200         + negtive direction

    (20.0,     5, 100),    # Positive int speed    + positive direction
    (7.8,      5, 39),     # Positive float speed  + positive direction
    (0.0,      5, 0),     # zero speed            + positive direction
    (-3.0,     5, -15),    # Negtive int speed     + positive direction
    (-5.2,     5, -26),    # Negtive float speed   + positive direction

    (2.0,     -5, -10),    # Positive int speed    + negtive direction
    (10.9,    -5, -55),   # Positive float speed  + negtive direction
    (0.0,     -5, 0),     # zero speed            + negtive direction
    (-33.0,   -5, 165),    # Negtive int speed     + negtive direction
    (-80.795, -5, 403),    # Negtive float speed   + negtive direction

    (2000.0,  0, 0),  # speed > 1200          + positive direction
    (-2000.0, 0, 0), # speed < -1200         + positive direction
])
def test_update(alien, speed, direction, delta):
    alien.settings.alien_speed = speed
    alien.settings.fleet_direction = direction 
    saved_x = alien.x
    alien.update()
    assert alien.rect.x == saved_x + delta
