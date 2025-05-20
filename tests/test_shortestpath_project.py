import pytest
from projekodlari.shortestpath import haversine

def test_zero_distance():
    assert haversine(0, 0, 0, 0) == 0

def test_known_distance():
    # Paris (48.8566, 2.3522) to London (51.5074, -0.1278)
    result = round(haversine(48.8566, 2.3522, 51.5074, -0.1278), 1)
    assert result == 343.4  # Approximate known distance

