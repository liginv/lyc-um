""" Test for tables.py file"""
import example


def test_tables():
    computed_result = example.tables(5, 5)
    expected_result = """ 5 X 1 = 5
    5 X 2 = 10
    5 X 3 = 15
    5 X 4 = 20
    5 X 5 = 25"""
    assert computed_result == expected_result