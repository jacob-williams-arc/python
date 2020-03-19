import pytest
from fuel_counter_upper import fuelRequiredByMass

#Test cases provided with the question
def test_fuel_calculation():
    assert fuelRequiredByMass(12) == 2
    assert fuelRequiredByMass(14) == 2
    assert fuelRequiredByMass(1969) == 654
    assert fuelRequiredByMass(100756) == 33583
