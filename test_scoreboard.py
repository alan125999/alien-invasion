from scoreboard import Scoreboard
from alien_invasion import AlienInvasion
import pytest
import pygame

@pytest.fixture
def game():
    return AlienInvasion()

@pytest.fixture
def scoreboard(game):
    return Scoreboard(game)

def imagesAreEqual(img1: pygame.Surface, img2: pygame.Surface):
    from functools import reduce
    pxarr1 = pygame.PixelArray(img1)
    pxarr2 = pygame.PixelArray(img2)
    compared = pxarr1.compare(pxarr2)
    flatten = reduce(lambda accu, i: accu + list(i), compared, [])
    return len(list(filter(lambda x: x != 0xFFFFFF, flatten))) == 0

# Test Scoreboard
def test_init(scoreboard, game):
    assert scoreboard.ai_game == game
    assert scoreboard.screen == game.screen
    assert scoreboard.screen_rect == game.screen.get_rect()
    assert scoreboard.settings == game.settings
    assert scoreboard.stats == game.stats
    assert scoreboard.text_color == (30, 30, 30)
    #assert scoreboard.font == pygame.font.SysFont(None, 48)

def test_prep_score(scoreboard):
    rounded_score = round(scoreboard.stats.score, -1)
    score_str = "{:,}".format(rounded_score)
    score_image = scoreboard.font.render(score_str, True, scoreboard.text_color, scoreboard.settings.bg_color)
    rect = score_image.get_rect()
    rect.right = scoreboard.screen_rect.right - 20
    rect.top = 20

    scoreboard.prep_score()
    
    #assert imagesAreEqual(scoreboard.score_image, score_image)
    assert scoreboard.score_rect == rect
    

def test_prep_high_score(scoreboard):
    high_score = round(scoreboard.stats.high_score, -1)
    high_score_str = "{:,}".format(high_score)
    high_score_image = scoreboard.font.render(high_score_str, True, scoreboard.text_color, scoreboard.settings.bg_color)
    rect = high_score_image.get_rect()
    rect.centerx = scoreboard.screen_rect.centerx
    rect.top = scoreboard.score_rect.top

    scoreboard.prep_high_score()
    
    #assert imagesAreEqual(scoreboard.high_score_image, high_score_image)
    assert scoreboard.high_score_rect == rect


def test_prep_level(scoreboard):
    level_str = str(scoreboard.stats.level)
    level_image = scoreboard.font.render(level_str, True, scoreboard.text_color, scoreboard.settings.bg_color)
    rect = level_image.get_rect()
    rect.right = scoreboard.score_rect.right
    rect.top = scoreboard.score_rect.bottom + 10

    scoreboard.prep_level()

    #assert imagesAreEqual(scoreboard.level_image, level_image)
    assert scoreboard.level_rect == rect

def test_prep_ships(scoreboard):
    scoreboard.prep_ships()

    for i, v in enumerate(scoreboard.ships):
        assert v.rect.x == 10 + i * v.rect.width
        assert v.rect.y == 10

@pytest.mark.parametrize("score, high_score, result", [
    (1280, 777, 1280), # >
    (777, 777, 777),   # =
    (111, 777, 777),   # <
])
def test_check_high_score(scoreboard, score, high_score, result):
    scoreboard.stats.score = score
    scoreboard.stats.high_score = high_score
    
    scoreboard.check_high_score()

    assert scoreboard.stats.high_score == result

def test_show_score(scoreboard):
    pass