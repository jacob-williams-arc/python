from math import floor

def fuelRequiredByMass(mass):
    return floor(mass / 3) - 2

def totalFuelRequiredForModule(mass):
    fuelRequired = fuelRequiredByMass(mass)
    if fuelRequired < 1:
        return 0
    return fuelRequired + totalFuelRequiredForModule(fuelRequired)

def loadModulesAndCalculateTotalFuelRequirements(filename):
    fuelCounts = []
    with open(filename) as inputFile:
        for mass in inputFile:
            fuelCounts.append(totalFuelRequiredForModule(int(mass.rstrip())))
    return sum(fuelCounts)

totalFuelRequired = loadModulesAndCalculateTotalFuelRequirements('mass_specs_for_modules')
print("Total fuel required for the mass of the modules: " + str(totalFuelRequired))
