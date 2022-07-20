#############################
# Calculator                #
# Author: Anon              #
# Date:   20.07.2022        #                         
#############################


### Methode wird nur einmal am Anfang ausgeführt, erste Zahl wird gegeben.
def start():
    firstNumber = 0
    userInput = input("Sie können das Programm jederzeit mit \"Exit\" beenden.\nBitte geben Sie die erste Zahl ein: ")
    if userInput.lower() == "exit":
        exit()
    else:
        firstNumber = int(userInput)

    return firstNumber

### Methode für die Lösung, Aufforderung zum Weiter/Erneut-Rechnen oder Beenden    
def firstRepeater(solution):
    userInput = input("Das Ergebnis ist: {0} \nMöchten Sie mit dem Ergebnis weiterrechnen, geben Sie ein: \"Weiter\"\nFür eine erneute Rechnung geben Sie ein: \"Neu\"\nZum Beenden geben Sie ein: \"Exit\"\nEingabe: ".format(solution)).lower()

    match userInput:
        case "weiter": 
            nextCalcProg(solution)
        case "neu":
            newCalcProg()
        case "exit":
            exit()
        case _:
            print("Eingabe ungültig!")
            firstRepeater(solution)

### Methode für die Lösung, Aufforderung zum Weiter/Erneut-Rechnen, Rechnen vom letzten Ergebnis oder Beenden.
def secondRepeater(solution):
    userInput = input("Das Ergebnis ist: {0} \nMöchten Sie mit dem Ergebnis weiterrechnen, geben Sie ein: \"Weiter\"\nFür eine erneute Rechnung geben Sie ein: \"Neu\"\n"
    "Um die letzte Rechnung rückgängig zu machen, geben Sie ein: \"Fehler\"\nZum Beenden geben Sie ein: \"Exit\"\nEingabe: ".format(solution)).lower()

    match userInput:
        case "weiter": 
            nextCalcProg(solution)
        case "neu":
            newCalcProg()
        case "exit":
            exit()
        case "fehler":
            wrongCalcProg()
        case _:
            print("Eingabe ungültig!")
            firstRepeater(solution)

### Methode zur Anforderung der ersten Zahl ////////// Kommt nach firstRepeater() wenn "neu" gewählt wurde!
def getFirstNumber():
    userInput = input("Bitte geben Sie die erste Zahl ein: ")
    if userInput.lower() == "exit":
        exit()
    else:
        firstNumber = int(userInput)

    return firstNumber

### Methode kommt IMMER zur Anforderung der zweiten Zahl //////// Kommt nach firstRepeater() wenn "weiter" gewählt wurde!
def getNextNumber():
    userInput = input("Bitte geben Sie eine weitere Zahl ein: ")
    if userInput.lower() == "exit":
        exit()
    else:
        secondNumber = int(userInput)

    return secondNumber

### Methode zur Auswahl des Operators
def getOperator(firstNumber,secondNumber):
    userInput = input("Bitte geben Sie den Rechenoperator ein (+,-,*,/): ")
    if userInput.lower() == "exit":
        exit()
    else:
        match userInput:
            case "+":
                solution = calcAdd(firstNumber,secondNumber)
            case "-":
                solution = calcSub(firstNumber,secondNumber)
            case "*":
                solution = calcMul(firstNumber,secondNumber)
            case "/":
                solution = calcDiv(firstNumber,secondNumber)
            case _:
                print("Eingabe ist kein gültiges Zeichen!")
                getOperator(firstNumber,secondNumber)
    
    return solution

### Variable zur Speicherung des letzten Ergebnisses
def getBackupNumber(saveNumber):
    backupNumber = saveNumber

    return backupNumber

def calcAdd(a, b):
    solution = a + b

    return solution

def calcSub(a, b):
    solution = a - b

    return solution

def calcMul(a, b):
    solution = a * b

    return solution
    
def calcDiv(a, b):
    solution = a / b

    return solution

### Funktion wird als erstes aufgerufen für die erste Berechnung
def firstCalcProg():
    firstNumber = start()
    secondNumber = getNextNumber()
    solution = getOperator(firstNumber,secondNumber)
    getBackupNumber(solution)
    firstRepeater(solution)

### Funktion wird aufgerufen für eine "neue Berechnung"
def newCalcProg():
    firstNumber = getFirstNumber()
    secondNumber = getNextNumber()
    solution = getOperator(firstNumber,secondNumber)
    getBackupNumber(solution)
    firstRepeater(solution)

### Funktion wird aufgerufen für eine "folge-Berechnung"
def nextCalcProg(solution):
    firstNumber = solution
    secondNumer = getNextNumber()
    solution = getOperator(firstNumber,secondNumer)
    getBackupNumber(solution)
    secondRepeater(solution)

### Funktion wird aufgerufen um auf das letzte Ergebnis zurückzukommen.
def wrongCalcProg():
    firstNumber = getBackupNumber()
    secondNumber = getNextNumber()
    solution = getOperator(firstNumber,secondNumber)
    getBackupNumber(solution)
    firstRepeater(solution)

firstCalcProg()