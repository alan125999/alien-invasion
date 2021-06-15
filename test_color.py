from color import Color

# Test Color
def test_color():
    assert Color.GAME_COLOR == (230, 230, 230)
    assert Color.WHITE == (255, 255, 255)
    assert Color.RED == (255, 0, 0)
    assert Color.BLACK == (0, 0, 0)