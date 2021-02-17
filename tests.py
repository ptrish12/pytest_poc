import pytest
from dummy_functions import super_add, super_multiply


def test_add():
    assert super_add(3,2) == 13


def test_multiply():
    assert super_multiply(2, 3) == 36
