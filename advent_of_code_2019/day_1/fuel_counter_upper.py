from math import floor


def fuelRequiredByMass(mass):
    return floor(mass / 3) - 2


def totalFuelRequiredForModule(mass):
    fuelRequired = fuelRequiredByMass(mass)
    if fuelRequired < 1:
        return 0
    return fuelRequired + totalFuelRequiredForModule(fuelRequired)


def loadModulesAndCalculate(filename):
    fuelCount = 0
    with open(filename) as inputFile:
        for mass in inputFile:
            fuelCount += totalFuelRequiredForModule(int(mass.rstrip()))
    return fuelCount


totalFuelRequired = loadModulesAndCalculate('./mass_specs_for_modules')
print("Total fuel required for the mass of the modules: "
      + str(totalFuelRequired))
