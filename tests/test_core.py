import pytest

from src.main import is_armstrong, is_palindrome


def test_is_armstrong_true():
    assert is_armstrong(153) is True


def test_is_armstrong_false():
    assert is_armstrong(123) is False


def test_is_armstrong_negative():
    assert is_armstrong(-1) is False


def test_is_palindrome_true():
    assert is_palindrome(121) is True


def test_is_palindrome_false():
    assert is_palindrome(123) is False


def test_is_palindrome_negative():
    assert is_palindrome(-121) is False
