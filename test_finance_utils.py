

import pytest

from finance_utils import (
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_total_amount,
    calculate_discount,
    calculate_profit
)


def test_simple_interest():
    assert calculate_simple_interest(10000, 5, 2) == 1000


def test_compound_interest():
    assert calculate_compound_interest(10000, 5, 2) == 1025.0


def test_total_amount():
    assert calculate_total_amount(10000, 1000) == 11000


def test_discount():
    assert calculate_discount(2000, 10) == 1800


def test_profit():
    assert calculate_profit(500, 700) == 200


def test_zero_interest():
    assert calculate_simple_interest(10000, 0, 2) == 0


def test_no_discount():
    assert calculate_discount(1000, 0) == 1000
