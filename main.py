import os

content: str = ""
filePath: str = ""
log = []

def setContent():
    global content
    global filePath

    while 1:
        inp = input("")

        if inp == ";efa":
            break
        elif inp == ";fu":
            fileUpd()
        elif inp == ";sfp":
            setFilePath()
        elif inp == ";u":
            undo()
        elif inp == ";sd":
            showDocumentation()
        elif inp == ";cc":
            os.system("cls")
        elif inp == ";rc":
            resetContent()
        elif inp == ";of":
            openFile()

        else:
            content += inp + "\n"
            log.append(inp)

def fileUpd():
    global filePath
    global content

    with open(filePath, "w") as f:
        f.writelines(content)
        f.close()

def openFile():
    global filePath
    global content
    global log

    with open(filePath, "r") as f:
        for line in f.readlines():
            content += line
            log.append(line.strip())

def undo():
    global log
    global content

    findText = input(": ")

    for i, v in enumerate(log):
        if v == findText:
            if v in content:
                content = content.replace(v, "")
                break

def resetContent():
    global content
    content = ""

def setFilePath():
    global filePath
    filePath = input(": ")

def printLogo():
    global fileName
    print("                                               \n" +
          "  _    _                       _               \n" +
          " | |  | |                     | |              \n" +
          " | |__| | ___  _   _ _ __ __ _| | __ _ ___ ___ \n" +
          " |  __  |/ _ || | | | '__/ _` | |/ _` / __/ __|\n" +
          " | |  | | (_) | |_| | | | (_| | | (_| |__ |__ |\n" +
          " |_|  |_||___/ |__,_|_|  |__, |_||__,_|___/___/\n" +
          "                          __/ |                \n" +
          "                         |___/                 \n" +
          "                                               \n")

def showDocumentation():
    printLogo()

    print("\nFile commands")
    print(";sfp (set file path), save file path to insert what you write after command ;sf")
    print(";fu (file update), saves files with content what you write")
    print(";rc (reset content), reset all what you write and after save nothing will be saved")
    print(";u (undo), delete one of needed string inside of content")

    print("\nApp commands")
    print(";cc (clear console), cleares whole console")
    print(";efa (exit from app), close app and asks before it save file or not")
    

def main():
    printLogo()
    setContent()
    

if __name__ == "__main__":
    main()