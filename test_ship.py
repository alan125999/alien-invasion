from alien_invasion import AlienInvasion
from ship import Ship

import pytest
import pygame

from functools import reduce

# Fixture
@pytest.fixture
def game():
    return AlienInvasion()

@pytest.fixture
def ship(game):
    return Ship(game)

def imagesAreEqual(img1: pygame.Surface, img2: pygame.Surface):
    pxarr1 = pygame.PixelArray(img1)
    pxarr2 = pygame.PixelArray(img2)
    compared = pxarr1.compare(pxarr2)
    flatten = reduce(lambda accu, i: accu + list(i), compared, [])
    return len(list(filter(lambda x: x != 0xFFFFFF, flatten))) == 0

# Test Ship
def test_init(ship, game):
    assert ship.screen == game.screen
    assert ship.settings == game.settings
    assert ship.screen_rect == game.screen.get_rect()

    img = pygame.image.load('assets/ship.bmp')
    assert imagesAreEqual(ship.image, img)

    rect = img.get_rect()
    rect.midbottom = ship.screen_rect.midbottom
    assert ship.rect == rect
    assert ship.x == float(ship.rect.x)
    assert ship.moving_right == False
    assert ship.moving_left == False

@pytest.mark.parametrize("moving_right, moving_left, x, screen_rect_right, ship_speed, delta", [
    # The width of the ship is 60,
    # When setting rect.x := n, the rect.right := n + 60 and rect.left := n
    
    # r < scr_r, l < 0
    (True, True,    -10, 80, 10, 10),
    (True, False,   -10, 80, 10, 10),
    (False, True,   -10, 80, 10, 0),
    (False, False,  -10, 80, 10, 0),

    # r < scr_r, l > 0
    (True, True,    10, 90, 10, 0),
    (True, False,   10, 90, 10, 10),
    (False, True,   10, 90, 10, -10),
    (False, False,  10, 90, 10, 0),
    
    # r < scr_r, l == 0
    (True, True,    0, 80, 10, 10),
    (True, False,   0, 80, 10, 10),
    (False, True,   0, 80, 10, 0),
    (False, False,  0, 80, 10, 0),
    
    # r > scr_r, l < 0
    (True, True,    -10, 10, 10, 0),
    (True, False,   -10, 10, 10, 0),
    (False, True,   -10, 10, 10, 0),
    (False, False,  -10, 10, 10, 0),

    # r > scr_r, l > 0
    (True, True,    10, 10, 10, -10),
    (True, False,   10, 10, 10, 0),
    (False, True,   10, 10, 10, -10),
    (False, False,  10, 10, 10, 0),
    
    # r > scr_r, l == 0
    (True, True,    0, 10, 10, 0),
    (True, False,   0, 10, 10, 0),
    (False, True,   0, 10, 10, 0),
    (False, False,  0, 10, 10, 0),

    # r == scr_r, l < 0
    (True, True,    -10, 50, 10, 0),
    (True, False,   -10, 50, 10, 0),
    (False, True,   -10, 50, 10, 0),
    (False, False,  -10, 50, 10, 0),

    # r == scr_r, l > 0
    (True, True,    10, 70, 10, -10),
    (True, False,   10, 70, 10, 0),
    (False, True,   10, 70, 10, -10),
    (False, False,  10, 70, 10, 0),

    # r == scr_r, l == 0
    (True, True,    0, 60, 10, 0),
    (True, False,   0, 60, 10, 0),
    (False, True,   0, 60, 10, 0),
    (False, False,  0, 60, 10, 0),
])
def test_update(ship, moving_right, moving_left, x, screen_rect_right, ship_speed, delta):
    ship.settings.ship_speed = ship_speed
    ship.moving_right = moving_right
    ship.moving_left = moving_left
    ship.rect.x = x
    ship.screen_rect.right = screen_rect_right
    saved_x = ship.x
    ship.update()
    assert ship.rect.x == saved_x + delta

def test_draw(ship):
    pass


@pytest.mark.parametrize("screen, midbottom, x", [
    ((1300, 1300),  (650, 1300),    620),
    ((0, 1300),     (600, 800),     570),
    ((1300, 0),     (600, 800),     570),
])
def test_align_center(game, screen, midbottom, x):
    game.screen = pygame.display.set_mode(screen)
    ship = Ship(game)

    ship.rect.x = -1
    ship.align_center()

    assert ship.rect.midbottom == midbottom
    assert ship.x == x