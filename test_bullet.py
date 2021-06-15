from alien_invasion import AlienInvasion
from bullet import Bullet

import pytest

# Fixture
@pytest.fixture
def game():
    return AlienInvasion()

@pytest.fixture
def bullet(game):
    return Bullet(game)

# Test Bullet
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
