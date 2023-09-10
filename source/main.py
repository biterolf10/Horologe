import os
import art

debugMode = False
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
        elif inp == "[rl":
            replaceLine()
        elif inp == "[dm":
            enterDebugMode()
        elif inp == "[pl":
            printLog()
        elif inp == "[pp":
            printPath()

        elif len(inp) >= 1:
            if inp[0] == "]":
                log.append(inp)
            else:
                if int(pos) != 0:
                    content = "{}{}{}\n".format(content[:int(pos)], inp, content[int(pos):])
                    log.append(inp)
                else:
                    content = content + inp + "\n"
                    log.append(inp)

def fileUpd():
    global filePath
    global content

    if filePath != "":
        with open(filePath, "w") as f:
            f.writelines(content)
            f.close()
    else:
        input(")\n")

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
        input(")\n")

def replaceLine():
    global filePath
    global content
    global log

    oldLine = input("( ")
    newLine = input("( ")

    for i, v in enumerate(log):
        if v == oldLine:
            if v in content:
                content = content.replace(v, newLine)
                log[i] = newLine
                break

def undo():
    global log
    global content

    findText = input("( ")

    for i, v in enumerate(log):
        if v == findText:
            if v in content:
                content = content.replace(v, "")
                log.pop[i]
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

def enterDebugMode():
    global debugMode

    if debugMode != True:
        correctPasswd = "246"
        inputPasswd = input("( ")
        if correctPasswd == inputPasswd:
            debugMode = True

def printLog():
    global log
    global debugMode

    if debugMode == True:
        print(log)

def printPath():
    global filePath
    global debugMode
    
    if debugMode == True:
        print(filePath)

def printLogo():
    art.tprint("Horologe", space=1)

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
    print("[rl (replace line), replace one line by another (required params: old line, new line)")
    print("[u (undo), delete one of needed string inside of content (required params: text to delete)")

    print("\nSymbols used in program")
    print("\"(\" program wait until user write needed params to command")
    print("\")\" program showing error")
    print("\"[\" used to execute commands")
    print("\"]\" comment, program ignore this line")
    

def main():
    printLogo()
    setContent()
    

if __name__ == "__main__":
    main()