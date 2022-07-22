### Abfrage 2. Zahl vom User und Kalkulation, Rückgabe Ergebnis

def calcAdd(firstNumber):
    userInput = input("Bitte geben Sie eine weitere Zahl ein:\t\t\t ")
    if userInput.lower() == "exit":
        exit()
    else:        
        try:
            secondNumber = int(userInput)    
            solution = firstNumber + secondNumber

            return solution          
            
        except:
            print("\nEingabe ungültig!\n")
            calcAdd()


def calcSub(firstNumber):
    userInput = input("Bitte geben Sie eine weitere Zahl ein:\t\t\t ")
    if userInput.lower() == "exit":
        exit()
    else:
        try:
            secondNumber = int(userInput)    
            solution = firstNumber - secondNumber

            return solution          
            
        except:
            print("\nEingabe ungültig!\n")
            calcSub()


def calcMul(firstNumber):
    userInput = input("Bitte geben Sie eine weitere Zahl ein:\t\t\t ")
    if userInput.lower() == "exit":
        exit()
    else:
        try:
            secondNumber = int(userInput)    
            solution = firstNumber * secondNumber

            return solution          
            
        except:
            print("\nEingabe ungültig!\n")
            calcMul()

    
def calcDiv(firstNumber):
    userInput = input("Bitte geben Sie eine weitere Zahl ein:\t\t\t ")
    if userInput.lower() == "exit":
        exit()
    else:
        try:
            secondNumber = int(userInput)    
            solution = firstNumber / secondNumber

            return solution          
            
        except:
            print("\nEingabe ungültig!\n")
            calcDiv()
