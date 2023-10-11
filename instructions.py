def read_Instructions():
    with open("menu_eng/instructions.txt") as instructionsTxt:
        instructions = instructionsTxt.read()

    return instructions