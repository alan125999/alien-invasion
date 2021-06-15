from alien_invasion import AlienInvasion
from alien import Alien

import pytest

# Fixture
@pytest.fixture
def game():
    return AlienInvasion()

@pytest.fixture
def alien(game):
    return Alien(game)

# Test Alien
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
    (1.0, 1, 1),    # Positive speed + positive direction
])
def test_update(alien, speed, direction, delta):
    alien.settings.alien_speed = speed
    alien.settings.fleet_direction = direction 
    saved_x = alien.x
    alien.update()
    assert alien.rect.x == saved_x + delta
