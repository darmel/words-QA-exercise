
from main import enter_new_word
import pytest


def test_valid_word():
    len(enter_new_word('casa')) > 0


def test_test():
    assert 'a' == 'a'