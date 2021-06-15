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
])
def test_update(alien, speed, direction, delta):
    alien.settings.alien_speed = speed
    alien.settings.fleet_direction = direction 
    saved_x = alien.x
    alien.update()
    assert alien.rect.x == saved_x + delta
