from itertools import groupby

def validLengthRequirement(candidate):
    return len(candidate) == 6


def validAdjacentRequirement(candidate):
    for i in range(len(candidate) - 1):
        if(candidate[i] == candidate[i + 1]):
            return True

    return False


def validAdjacentRequirementModified(candidate):
    digitCounts = [''.join(value) for key, value in groupby(candidate)]
    for digit in range(len(digitCounts)):
        if len(digitCounts[digit]) == 2:
            return True
        
    return False


def validNumericPatternRequirement(candidate):
    previousDigit = 0
    for digit in map(int, candidate):
        if digit < previousDigit:
            return False
        previousDigit = digit

    return True


def isValidPasswordPart1(candidate):
    return (validLengthRequirement(candidate)
        and validAdjacentRequirement(candidate)
        and validNumericPatternRequirement(candidate))


def isValidPasswordPart2(candidate):
    return (validLengthRequirement(candidate)
        and validAdjacentRequirementModified(candidate)
        and validNumericPatternRequirement(candidate))


validity = []
for candidate in range(264360, 746325):
    validity.append(isValidPasswordPart2(str(candidate)))

print(validity.count(True))
