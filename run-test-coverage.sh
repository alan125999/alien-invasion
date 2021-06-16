#!/bin/bash
pytest \
    --cov=alien \
    --cov=alien_invasion \
    --cov=bullet \
    --cov=button \
    --cov=color \
    --cov=driver \
    --cov=game_functions \
    --cov=game_stats \
    --cov=scoreboard \
    --cov=settings \
    --cov=ship \
    --cov=utils \
    test_*.py