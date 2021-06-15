from alien_invasion import AlienInvasion
from bullet import Bullet

import pytest
import pygame

# Fixture
@pytest.fixture
def game():
    return AlienInvasion()

@pytest.fixture
def bullet(game):
    return Bullet(game)

# Test Bullet
def test_init(bullet, game):
    assert bullet.screen == game.screen
    assert bullet.settings == game.settings
    assert bullet.color == game.settings.bullet_color
    rect = pygame.Rect(0, 0, bullet.settings.bullet_width, bullet.settings.bullet_height)
    rect.midtop = game.ship.rect.midtop
    assert bullet.rect == rect
    assert bullet.y == float(bullet.rect.y)

@pytest.mark.parametrize("speed, delta", [
    (20.0, 20),    # Positive int speed
    (7.8,   8),    # Positive float speed
    (0.0,   0),    # zero speed
    (-3.0, -3),    # Negtive int speed
    (-5.2, -5),    # Negtive float speed
    
    (2000.0,   2000), # speed > 800
    (-2000.0, -2000), # speed < -800
])
def test_update(bullet, speed, delta):
    bullet.settings.bullet_speed = speed
    saved_y = bullet.y
    bullet.update()
    assert bullet.rect.y == saved_y - delta

def test_draw_bullet(bullet):
    pass
