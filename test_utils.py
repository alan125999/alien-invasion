from utils import hide_mouse_cursor

import pygame

# Test Utils
def test_hide_mouse_cursor():
    hide_mouse_cursor()
    assert pygame.mouse.get_visible() == False