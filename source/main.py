import os
import art

pos = "0"
content: str = ""
filePath: str = ""
log = []

def setContent():
    global content
    global filePath

    while 1:
        inp = input("")

        if inp == "[efa":
            break
        elif inp == "[fu":
            fileUpd()
        elif inp == "[fp":
            setFilePath()
        elif inp == "[u":
            undo()
        elif inp == "[sd":
            showDocumentation()
        elif inp == "[cc":
            os.system("cls")
        elif inp == "[rc":
            resetContent()
        elif inp == "[of":
            openFile()
        elif inp == "[cp":
            setCursorPosition()
        elif inp == "[sc":
            showContent()

        elif inp[0] == "]":
            log.append(inp)

        else:
            content = "{}{}{}".format(content[:int(pos)], inp, content[int(pos):])
            log.append(inp)

def fileUpd():
    global filePath
    global content

    if filePath != "":
        with open(filePath, "w") as f:
            f.writelines(content)
            f.close()
    else:
        print(")\n")

def openFile():
    global filePath
    global content
    global log

    if filePath != "":
        with open(filePath, "r") as f:
            for line in f.readlines():
                content += line
                log.append(line.strip())
    else:
        print(")\n")

def undo():
    global log
    global content

    findText = input("( ")

    for i, v in enumerate(log):
        if v == findText:
            if v in content:
                content = content.replace(v, "")
                break

def resetContent():
    global content
    content = ""

def showContent():
    global content
    print(content)

def setFilePath():
    global filePath
    filePath = input("( ")

def setCursorPosition():
    global pos
    pos = input("( ")

def printLogo():
    art.tprint("Hourglass", space=1)

def showDocumentation():
    printLogo()

    print("\nFile commands")
    print("[fp (file path), sets file path (required params: path to file)")
    print("[fu (file update), sets file text to current content")
    print("[of (open file), open file with current path, content sets to file text")

    print("\nApp commands")
    print("[efa (exit from app), command to close app")
    print("[cc (clear console), command to cleare console")

    print("\nText commands")
    print("[sc (show content), prints all content")
    print("[cp (cursor position), sets cursor position (required params: position (symbol number))")
    print("[rc (reset content), reset all content")
    print("[u (undo), delete one of needed string inside of content (required params: text to delete)")

    print("\nSymbols used in program")
    print("\"(\" program wait until user write needed params to command")
    print("\")\" program shows error, you make something wrong")
    print("\"[\" used to execute commands")
    print("\"]\" comment, program ignore this line")
    

def main():
    printLogo()
    setContent()
    

if __name__ == "__main__":
    main()