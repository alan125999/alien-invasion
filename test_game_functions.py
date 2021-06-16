from game_functions import manage_events, draw_screen
from alien_invasion import AlienInvasion
from ship import Ship
import pygame
import pytest
from collections import namedtuple

# Fixture
@pytest.fixture
def game():
    return AlienInvasion()

@pytest.fixture
def ship(game):
    return Ship(game)

Event = namedtuple('Event', ['type', 'key'])
# Test Game Functions
def test_manage_events(mocker, ship):
    mocker.patch('pygame.event.get', return_value=[Event(pygame.KEYDOWN, pygame.K_RIGHT)])
    saved = ship.rect.centerx
    manage_events(ship)
    assert ship.rect.centerx == saved + 1