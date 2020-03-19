
def executeIntcode(program):
    readPosition = 0
    while program[readPosition] != 99:
        if program[readPosition] == 1:
            program[program[readPosition + 3]] = program[program[readPosition + 1]] + program[program[readPosition + 2]]
        elif program[readPosition] == 2:
            program[program[readPosition + 3]] = program[program[readPosition + 1]] * program[program[readPosition + 2]]
        readPosition += 4
    return program

def loadProgramFromFile(filename):
    with open(filename) as inputFile:
        rawProgram = inputFile.read().split(',')
    return [int(i) for i in rawProgram]

programFinalState = executeIntcode(loadProgramFromFile('./gravity_assist_program_updated'))
print("Value at position 0: " + str(programFinalState[0]))
