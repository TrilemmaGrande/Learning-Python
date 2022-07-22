#############################
# Calculator                #
# Author: Anon              #
# Date:   20.07.2022        #                         
#############################

import Operations

### Methode wird nur einmal am Anfang ausgeführt, erste Zahl wird vom User verlangt.
def start():
    firstNumber = 0
    userInput = input("Sie können das Programm jederzeit mit \"Exit\" beenden.\nBitte geben Sie die erste Zahl ein:\t\t\t ")
    if userInput.lower() == "exit":
        exit()
    else:  
        try:
            firstNumber = int(userInput)    
                       
            return firstNumber
        except:
            print("\nEingabe ungültig!\n")
            start()

### Methode zur Anforderung der ersten Zahl vom User ////////// Kommt nach firstRepeater() wenn "neu" gewählt wurde!
def userInputFirstNumber():
    userInput = input("Bitte geben Sie die erste Zahl ein:\t\t\t ")
    if userInput.lower() == "exit":
        exit()
    else:
        try:
            firstNumber = int(userInput)

            return firstNumber
        except:
            print("\Eingabe ungültig!\n")
            start()    

### Methode für die Lösung, Aufforderung User zum Weiter/Erneut-Rechnen oder Beenden    
def Repeater(solution2):
    userInput = input("Das Ergebnis ist:\t\t\t\t\t {0} \nMit dem Ergebnis weiterrechnen: \"Weiter\"\nErneute Rechnung:"
    " \"Neu\"\nBeenden: \"Exit\"\nEingabe:\t\t\t\t\t\t ".format(solution2)).lower()

    match userInput:
        case "weiter":
            nextCalcProg(solution2)
        case "neu":
            newCalcProg()
        case "exit":
            exit()
        case _:
            print("\nEingabe ungültig!")
            Repeater(solution2)

### Methode zur Auswahl des Operators durch User
def userInputOperator(firstNumber):
    userInput = input("Bitte geben Sie den Rechenoperator ein (+,-,*,/):\t ")
    if userInput.lower() == "exit":
        exit()
    else:
        match userInput:
            case "+":
                solution = Operations.calcAdd(firstNumber)
            case "-":
                solution = Operations.calcSub(firstNumber)
            case "*":
                solution = Operations.calcMul(firstNumber)
            case "/":
                solution = Operations.calcDiv(firstNumber)
            case _:
                print("\nEingabe ist kein gültiges Zeichen!\n")
                userInputOperator(firstNumber)
    
    return solution

### Funktion wird als erstes aufgerufen für die erste Berechnung
def Main():
    firstNumber = start()    
    solution2 = userInputOperator(firstNumber)    
    Repeater(solution2)

### Funktion wird aufgerufen für eine "neue Berechnung"
def newCalcProg():
    firstNumber = userInputFirstNumber()    
    solution2 = userInputOperator(firstNumber)    
    Repeater(solution2)

### Funktion wird aufgerufen für eine "folge-Berechnung"
def nextCalcProg(solution):
    firstNumber = solution    
    solution2 = userInputOperator(firstNumber)    
    Repeater(solution2)

Main()

