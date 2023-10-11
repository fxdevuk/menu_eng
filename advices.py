def readAdvices():
    with open("advicestext.txt") as advicesTxt:
        advices = advicesTxt.read()

    return advices # return as a tuple[str, str]
    # we can access a tupel based on index 


