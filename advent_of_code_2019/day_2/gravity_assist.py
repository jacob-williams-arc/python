
def executeIntcode(program):
    instructionPointer = 0
    while program[instructionPointer] != 99:
        if program[instructionPointer] == 1:
            program[program[instructionPointer + 3]] = (
                program[program[instructionPointer + 1]]
                + program[program[instructionPointer + 2]])
        elif program[instructionPointer] == 2:
            program[program[instructionPointer + 3]] = (
                program[program[instructionPointer + 1]]
                * program[program[instructionPointer + 2]])
        instructionPointer += 4
    return program


def loadProgramFromFile(filename):
    with open(filename) as inputFile:
        rawProgram = inputFile.read().split(',')
    return [int(i) for i in rawProgram]


programInitialState = loadProgramFromFile('./gravity_assist_program_updated')
programFinalState = executeIntcode(programInitialState)
print("Value at position 0: " + str(programFinalState[0]))

desiredOutput = 19690720
# noun position 1 in program, between 0 and 99, inclusive
# verb position 2 in program, between 0 and 99, inclusive

for noun in range(99):
    for verb in range(99):
        programInitialState = (
            loadProgramFromFile('./gravity_assist_program_updated'))
        programInitialState[1] = noun
        programInitialState[2] = verb
        programFinalState = executeIntcode(programInitialState)

        if(programFinalState[0] == desiredOutput):
            print("Noun: " + str(noun))
            print("Verb: " + str(verb))
            print("Try: " + str((100 * noun) + verb))
            break
