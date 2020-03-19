import pytest
from fuel_counter_upper import fuelRequiredByMass, totalFuelRequiredForModule

#Test cases provided with the question
def test_fuel_calculation():
    assert fuelRequiredByMass(12) == 2
    assert fuelRequiredByMass(14) == 2
    assert fuelRequiredByMass(1969) == 654
    assert fuelRequiredByMass(100756) == 33583

# Test cases provided with the question
def test_total_fuel_by_module():
    assert totalFuelRequiredForModule(14) == 2
    assert totalFuelRequiredForModule(1969) == 966
    assert totalFuelRequiredForModule(100756) == 50346
