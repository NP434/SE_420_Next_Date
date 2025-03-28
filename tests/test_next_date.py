import pytest
from src.Next_date import next_date,check_leap_year

def test_regular_next_date():
    month,day,year = next_date(4,16,2025)
    assert month == 4
    assert day == 17
    assert year == 2025

def test_even_next_date():
    month,day,year = next_date(4,30,2025)
    assert month == 5
    assert day == 1
    assert year == 2025
    
def test_odd_next_date():
    month,day,year = next_date(5,30,2025)
    assert month == 5
    assert day == 31
    assert year == 2025

def test_feb_next_date():
    month,day,year = next_date(2,28,2025)
    assert month == 3
    assert day == 1
    assert year == 2025

def test_leap_year_next_date():
    month,day,year = next_date(2,28,2020)
    assert month == 2
    assert day == 29
    assert year == 2020

def test_year_reset_next_date():
    month,day,year = next_date(12,31,2024)
    assert month == 1
    assert day == 1
    assert year == 2025
