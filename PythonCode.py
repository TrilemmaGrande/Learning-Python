# import math

##############################
#  Author: Anon              #
#  Date:   19.07.2022        #
##############################

##################################### Größer OR Kleiner ##########################################################

# zahl = int(input("Geben Sie eine Zahl ein: "))
# if zahl > 5:
#    print("Die von Ihnen eingegebene Zahl ist größer als 5")
# elif zahl < 5:
#    print("Die Zahl ist kleiner als 5")
# else:
#    print("Die Zahl ist 5")

###################################### Größer AND Kleiner ########################################################

# gewicht = 0
# while gewicht != "exit":
#    gewicht = float(input("Bitte das Gewicht des Teilnehmers angeben: "))
#    if gewicht >= 235 and gewicht <= 265:
#        print("Teilnehmer ist für die Gewichtsklasse zugelassen")
#    else:
#        print("Gewicht des Teilnehmers außerhalb der Gewichtsklasse")

########################################## Größer OR Größer  ####################################################

# kontostandGiro = Eingabe()
# kontostandSpar = Eingabe()
# saldoGiro = float(input("Bitte geben Sie den Guthabensaldo Ihres Girokontos an: "))
# saldoSpar = float(input("Vielen Dank. \nBitte geben Sie nun den Guthabensaldo Ihres Sparkontos an: "))

# Wenn kontostandGiro > 1000 oder kontostandSpar > 1500
# if saldoGiro > 1000 or saldoSpar > 1500:

#    #dann "Keine Scheckgebühr"
#    print("Ihnen wird keine Scheckgebühr belastet")

# sonst "Scheckgebühr 0,15"
# else:
#    print("Die Scheckgebühr beträgt 0,15 EUR")
# wenn Ende
# Ende

######################################### Berechnung in IF ###############################################################

# #gewicht = Eingabe()
# gewicht = float(input("Bitte geben Sie das Gewicht des Paketes ein: "))
# gewicht = int(round(gewicht))
# #versandkosten = 0
# versandkosten = 0.00

# #wenn gewicht <= 10.00
# if gewicht <= 10.00:
#     #dann versandkosten = 3
#     versandkosten = 3.00
#     #sonst (gewicht -10) * 0,25)

# elif gewicht >= 20.00:
#     versandkosten = (gewicht - 10) * 0.50 + 3.00

# else:
#     versandkosten = (gewicht - 10) * 0.25 + 3.00
# #Ausgabe versandkosten
# print("Die versandkosten betragen:",str('%.2f' %versandkosten))

########################################## Waehrungsrechner ##############################################################

# #währung = 1.9
# waehrung = 1.95583
# #betrag = Eingabe()
# betrag = float(input("Bitte geben Sie den Betrag ein: "))
# #auswahl = Eingabe()
# auswahl = input("Bitte geben Sie \"e\" für die Umrechnung von DM -> EUR ein, oder ein anderes Zeichen für die Berechnung von EUR -> DM: ")
# #wenn auswahl = e
# if auswahl == 'e':
#     #dann Betrag = DM / 1.9
#     betrag /= waehrung
#     #Ausgabe = Betrag in EUR
#     print("Der Wechselkurs beläuft sich auf: {0} EUR/DM\nDer eingegebene Saldo hat einen Wert von: {1} EUR".format(waehrung, round(betrag, 2)))
#     #sonst Betrag = EUR * 1.9
# else:
#     betrag *= waehrung
#     #Ausgabe = Betrag in DM
#     print("Der Wechselkurs beläuft sich auf: {0} EUR/DM\nDer eingegebene Saldo hat einen Wert von: {1} DM".format(waehrung, round(betrag, 2)))

############################################### Geburtstagsrechner ########################################################

# alter = 0
# #eingabe Geburtstag
# geburtsjahr = int(input("Bitte geben Sie die letzten 2 Stellen des Jahres ein, in dem Sie geboren sind: "))
# #eingabe schon Geburtstag
# geburtstag = (input("Hatten Sie schon Geburtstag? Y/N: ")).lower()
# #eingabe aktuelles Jahr
# jahr = int(input("Bitte geben Sie die letzten 2 Stellen des aktuellen Jahres ein: "))

# #Alter = Geburtsjahr - 100 + aktuelles Jahr
# alter = 100 - geburtsjahr + jahr
# #wenn noch nicht Geburtstag gehabt Alter - 1
# if geburtstag == 'n':
#     alter -= 1
# #Ausgabe
# print("Sie sind {0} Jahre alt!".format(alter))

############################################## Inkrementierung ############################################################

# schleife = True
# i = 0
# while schleife:
#     i += 1
#     print(i)
#     if i == 200:
#         break

############################################## Mikrowellenrechner ########################################################

# def mikrowellenRechner():

#     portion = int(input("bitte geben Sie die Portionen an: \n"))
#     heatTimeNew = (portion + 1) * 0.5 * int(input("bitte geben Sie die angegebene Erhitzungszeit pro Portion in ganzen Minuten ein: \n"))

#     def output(portion, heatTimeNew):
#             print("Erhitzen Sie Ihre {0} Portion für {1} Minuten\n".format(portion, heatTimeNew))
            
#     match portion:
#         case 1:
#             output(portion, heatTimeNew)
#         case 2:
#             output(portion, heatTimeNew)
#         case 3:
#             output(portion, heatTimeNew)
#         case _:
#             print("Sie haben die maximalen Portionen überschritten, es wird nicht empfohlen mehr als 3 Portionen zu verwenden!\n")

# mikrowellenRechner()

############################################### Tanken ####################################################################

# tankKapazitaet = int(input("bitte geben Sie die Tankkapazität Ihres Fahrzeuges an: "))
# benzinAnzeige = int(input("bitte geben Sie den prozentualen Anteil in 25% Schritten Ihrer Benzinanzeige an (ohne % Zeichen): "))
# benzinVerbrauch = int(input("bitte geben Sie den durchschnittlichen Verbrauch des Fahrzeuges in km / Liter an: "))
# kilometerNoch = 200

# # Reichweite = km / Inhalt * Prozent
# reichweite = benzinVerbrauch * tankKapazitaet * benzinAnzeige / 100

# if reichweite < kilometerNoch:
#     print("bitte Tanken!")
# else:
#     print("gerne weiterfahren!")

################################################## Methoden ###############################################################

# def halloWelt():
#     print("Hallo Welt!")

################################################## Methoden 2 #############################################################

# def halloWelt():
#     print("Hallo Welt!")
#     print("Hello World!")
#     print("Moin Moin!")
#     print("Servus!")

################################################### Print 1-4 ##############################################################

# def output():
#     for i in range(1,5):
#            print(i)

# output()

################################################### Print 2.0 ##############################################################

# def output():
#     print("1.00\n2.00\n3.00\n4.00")

# output()

################################################### Print 3.0 ##############################################################

# def output():
#     for i in range(1,5):
#            print('%.5f' %i)

# output()

##################################################### Converter #############################################################

# def converterInt(i):
#     int(i)

#     return i

# def converterFloat(i):
#     float(i)

#     return i

# def converterChar(i):
#     char(i)

#     return i

# def converterString(i):
#     str(i)

#     return i

##################################################### Programmverlauf ########################################################

# def Main():
#     print("Aufruf der Methode Main")
#     Methode1()
#     print("Ende der Methode Main")

# def Methode1():
#     print("Aufruf der Methode 1")
#     Methode2()
#     print("Ende der Methode 1")

# def Methode2():
#     print("Aufruf der Methode 2")
#     Methode3()
#     print("Ende der Methode 2")

# def Methode3():
#     print("Aufruf der Methode 3")
#     print("Ende der Methode 3")

# Main()

##################################################### Programmverlauf 2 #######################################################

# def Main():
#     x = 1
#     print("Aufruf der Methode Main")
#     y = Methode1(x)    
#     print("Ende der Methode Main:", y , x)    
#     x = x + y
#     print(x)

# def Methode1(x):    
#     print("Aufruf der Methode 1:", x)
#     x = x + 1   
#     y = Methode2(x)    
#     print("Ende der Methode 1:", y, x)
#     x = x + y
#     return x

# def Methode2(x):
#     print("Aufruf der Methode 2:", x)
#     x = x + 1   
#     y = Methode3(x)
#     print("Ende der Methode 2:", x, y)
#     x = x + y
#     return x    

# def Methode3(x):
#     print("Aufruf der Methode 3:", x)
#     x = x + 1
#     print("Ende der Methode 3:", x)
#     return x

# Main()

