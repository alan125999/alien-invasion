from settings import Settings

import pytest

@pytest.fixture
def settings():
    return Settings()

# Test Settings
def test_init(settings):
    assert settings.screen_width == 1200
    assert settings.screen_height == 800
    assert settings.bg_color == (230, 230, 230)
    assert settings.ship_limit == 3
    assert settings.bullet_width == 3
    assert settings.bullet_height == 15
    assert settings.bullet_color == (60, 60, 60)
    assert settings.bullets_allowed == 3
    assert settings.fleet_drop_speed == 10
    assert settings.speedup_scale == 1.1
    assert settings.score_scale == 1.5

def test_initialize_dynamic_settings(settings):
    settings.initialize_dynamic_settings()
    assert settings.ship_speed == 1.5
    assert settings.bullet_speed == 3.0
    assert settings.alien_speed == 1.0
    assert settings.fleet_direction == 1
    assert settings.alien_points == 50

def test_increase_speed(settings):
    ship_speed = settings.ship_speed
    bullet_speed = settings.bullet_speed
    alien_speed = settings.alien_speed
    alien_points = settings.alien_points
    settings.increase_speed()
    assert settings.ship_speed == settings.speedup_scale * ship_speed
    assert settings.bullet_speed == settings.speedup_scale * bullet_speed
    assert settings.alien_speed == settings.speedup_scale * alien_speed
    assert settings.alien_points == int(settings.score_scale * alien_points)