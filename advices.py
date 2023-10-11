def readAdvices():
    with open("menu_eng/advicestext.txt") as advicesTxt:
        advices = advicesTxt.read()

    return advices # return as a tuple[str, str]
    # we can access a tupel based on index 


