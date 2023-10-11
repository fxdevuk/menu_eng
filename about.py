def readAbout():
    with open("menu_eng/about.txt") as aboutTxt:
        about = aboutTxt.read()

    return about