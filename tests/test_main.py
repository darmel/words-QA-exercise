
from main import enter_new_word
from main import main

import pytest


def test_empty_string(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: '')
    assert (main('')) == 'not valid'


def test_valid_word():
    assert 0 < (enter_new_word('casa')[1])


def test_amount_of_permutations():
    assert 64 == (enter_new_word('abcd')[2])


def test_amount_english_words():
    assert 9 == (enter_new_word('working')[1])


def test_test():
    assert 'a' == 'a'
