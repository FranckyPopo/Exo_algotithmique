import string
import random

def alphabet():
    alphabet = list(string.ascii_lowercase)
    return alphabet


def just_price():
    while True:
        try:
            enter_number = int(input("Veuillez entrer une nom comprit entrer 10 et 20"))
        except ValueError:
            print("Veuillez entrer un nombre")
        else:
            if enter_number >= 11 and enter_number <= 19:
                print("Félicitation vous avez trouvé le bon numéro")
                break
            elif enter_number > 20:
                print("Plus petit !")
            else:
                print("Plus grand !")
            

def greater_than():
    i = 10
    liste_number = []
    
    while i != 0:
        try:
            choice = int(input("Veuillez entrer un nombre"))
        except ValueError:
            print("Veuillez entrer un nombre")
        else:
            liste_number.append(choice)
            i -= 1
            
            if len(liste_number) == 10:
                pass


greater_than()