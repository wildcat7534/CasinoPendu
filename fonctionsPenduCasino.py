"""Fonctions automatisant l'ajout des scores dans le ficher binaire"""

"""with open(nom_fichier,"wb") as fich:  # Il est conseillé d'utiliser with

   pickle.dump(objet, fich)              # objet est enregistré dans fichier

   objet = pickle.load(fich)             # on récupère l'objet suivant de fichier """

#import os
import pickle
from time import sleep
from random import randrange
from math import ceil

remember = False
game = False
pendu = False
casino = False
NewPlayer = ""



NON = ['non', 'Non', 'NON', 'no', 'n', 'N']
OUI = ['oui', 'Oui', 'OIu', 'OUI', 'yes', 'Yes', 'YEs',
       'YES', 'ouais', 'Ouais', 'ok', 'Ok', 'OK', 'Oui !', 'o', 'O']

remerciements = "GOOD BYE, Thanks to you to try me ^____^ \n"" \
"               "Remerciement à Alice, Pouya, Drey"


def NumMagic() :
    return randrange(40, 80)
def NumMagicRoulette() :
    return randrange(1, 37)

def EspaceTemps(espace) :
   for a in range(espace) :
       print()
       sleep(0.25)

def openScore() :
    with open('donnees', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        score = mon_depickler.load()
        print('scores chargés :', score,'\n')
        return score


def ajoutS(new_score) :
    with open('donnees', 'wb') as fichier :
        pickle.dump(new_score, fichier)

def DelPseudo(pseudandscoretodelet):
    score = openScore()
    del score[pseudandscoretodelet]
    ajoutS(score)

def openMotPendu() :
    with open('motpendu', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        mot_pendu = mon_depickler.load()
        #print('dico chargés :', mot_pendu,'\n')
        return mot_pendu

def ajoutMotPendu(dico_des_mots) :
    with open('motpendu', 'wb') as fichier :
        pickle.dump(dico_des_mots, fichier)

def PairImpair(un_nbr) :
    if (un_nbr%2 == 0) :
        return('pair')
    else :
        return('impair')

def CheatCode(nom_du_joueur, mot):
    if nom_du_joueur == 'wildcat':
        print("CheatCode ON :", mot)
    elif nom_du_joueur == 'pouya':
        print("CheatCode ON :", mot, "\n"
              "salut Pouya ! Merci de corriger mon Pendu 3.1 haha, bisous à vous 2 \n"
              "Tu entre en mode GodeMode : your intelligence up to 23, you guess and \n"
              "you feel every words asked in pendu !")
    elif nom_du_joueur == 'drey':
        print("CheatCode ON :", mot, "\n"
              "Hey Drey ! Tu essais mon jeux ? :D\n"
              "merci de m'avoir trouvé ces bugs la dernière fois :)\n"
              "CheatCode ON :", mot)

def GetGame():
    global game
    return game

def GetCasino():
    global casino
    return casino

def GetPendu():
    global pendu
    return pendu

def GetRemember():
    global remember
    return remember

def GetNewPlayer():
    global NewPlayer
    return NewPlayer

def Menu():
    global game
    global pendu
    global casino
    menu = True
    while menu == True:
        ask = input("\n*°*-------*------MENU PRINCIPAL------*------*°*"
                    "\n ----> CHOIX DU JEUX : casino ou pendu ou non(N,n) ? --> ")
        if ask == 'pendu':
            game = True
            casino = False
            pendu = True
            EspaceTemps(3)
            print("Je vais lancer le pendu !")
            EspaceTemps(5)
            sleep(1)
            return game, casino, pendu

        elif ask == 'casino':
            game = True
            casino = True
            pendu = False
            print("Je vais lancer le casino !")
            EspaceTemps(7)
            print("      ┼ BIENVENUE DANS CE MAGNIFIQUE CASINO ┼ ")
            EspaceTemps(5)
            return game, casino, pendu

        elif ask in NON:
            game = False
            casino = False
            pendu = False
            print()
            print("GOOD BYE, Thanks to you to try me ^_-_^ ")
            print()
            return None

        else:
            print("Je n'ai pas compris.")
            print()

def Remember():
    global remember
    global NewPlayer
    while not remember:
        score = openScore()
        NewPlayer = (input("Salut ! Qu\'elle est ton pseudo ? : ")).lower()
        EspaceTemps(1)
        if NewPlayer in score:
            print('Salut', NewPlayer, "! Te revoila ! Ton ancien score est de : ", score[NewPlayer])
            EspaceTemps(3)
            remember = True
        if NewPlayer not in score:
            score[NewPlayer] = int(NumMagic())
            print("Voilà quelques points attribués pour commencer :", score[NewPlayer], "Pts/Btc")
            ajoutS(score)
            remember = True

def Casino():
    global game
    global casino
    mise = 0
    nbr = 0
    mise_player = False
    nbr_player = False
    score = openScore()
    print(NewPlayer, "vous disposez de :", score[NewPlayer], "Btc\n")
    if score[NewPlayer] != 0:
        EspaceTemps(1)
        while not mise_player:
            try:
                mise = int(input("\nCroupier : 'Faites vos jeux' ! \n"
                                 "Combien misez-vous ? :  "))
                mise_player = True
            except ValueError:
                print("\n ERREUR ! : Ceci n'est pas un chiffre non ?\n")
        EspaceTemps(1)

        if int(mise > 0) and (int(mise) <= score[NewPlayer]):
            while not nbr_player:
                try:
                    nbr = int(input("Sur quel chiffre misez-vous entre 1 et 36 inclu ? \n"))
                    nbr_player = True
                except ValueError:
                    print("\n ERREUR ! : Ceci n'est pas un chiffre non ?\n")
            EspaceTemps(2)

            if 0 < nbr < 37:
                print("Les dès sont lancés !")
                EspaceTemps(5)
                roulette = NumMagicRoulette()
                print("Le resultat est : ", roulette)
                if nbr == roulette:
                    sleep(3)
                    score[NewPlayer] = ceil(mise * 35) + (score[NewPlayer] - mise)
                    ajoutS(score)
                    sleep(1)
                    print("Gagné !!", mise, "x35 --!\n\n"
                                            "INCROYABLE !\n\n"
                          "Gain de : ", ceil(mise * 35), " ! ! -- !! -- !! -- !! -- !!!!!\n")
                elif PairImpair(nbr) == 'pair' and PairImpair(roulette) == 'pair':
                        EspaceTemps(2)
                        score[NewPlayer] = ceil(mise * 1.5) + (score[NewPlayer] - mise)
                        ajoutS(score)
                        sleep(1)
                        print("Double pair !", mise, "x1,5 -! \n"
                              "Gain de : ", ceil(mise * 1.5), " ! ! ")
                elif PairImpair(nbr) == 'impair' and PairImpair(roulette) == 'impair':
                    EspaceTemps(2)
                    score[NewPlayer] = ceil(mise * 1.5) + (score[NewPlayer] - mise)
                    ajoutS(score)
                    sleep(1)
                    print("Double impair !", mise, "x2,5 -! \n"
                          "Gain de : ", ceil(mise * 2.5), " ! ! ")
                else:
                    EspaceTemps(1)
                    score[NewPlayer] -= mise
                    ajoutS(score)
                    print("perdu... :/ \n")
                    regame = input("Veux-tu continuer le casino ? :")
                    if regame in OUI:
                        casino = True
                    elif regame in NON:
                        casino = False
                        game = True
                        print()
                        print(remerciements)
                        print()

            else:
                EspaceTemps(1)
                print("Merci de choisir un nombre entre 1 et 36 compris ;) \n")

        if int(mise < 0) or (int(mise) > score[NewPlayer]):
            EspaceTemps(1)
            print("Merci de vouloir miser l'argent que vous possèdez.")
    else:
        casino = False
        game = True
        ajoutS(score)
        EspaceTemps(1)
        print("Désolé vous n\'avez plus d\'argent, veullez sortir du casino. Merci")
        EspaceTemps(1)
        print("Vous n'avez plus de point vous ne pouvez plus jouer ici.")
        EspaceTemps(1)
        print(remerciements)


def Pendu():
    global game
    global casino
    global pendu
    score = openScore()
    mot_pendu = openMotPendu()
    chiffres_interdits = "1234567890"
    E = "é"
    e = "è"
    epitaphe = {0: "I never understood what the point to die far this kind of game.",
                1: "Too weird to live, too rare to die. HST",
                3: "We made never mistake without trying.",
                4: "Le marbre est le plancher des vivants et le toît des morts",
                5: "Verre vide, je te plains, verre plein, je te vide",
                6: "Les gens s'attendent à ce que nous échouions. Notre mission est de dépasser leur attente.",
                7: "Ci-gît Jackson, Regrets éthernels.Epitaphe de Jackson, qui découvrit les propriétés de l'éther",
                8: "I told you I was sick",
                9: "His final words was : \'It was so good this mushrooms\'",
                10: "When I was in the military they gave me a medal for killing two men a discharge 4 loving one",
                11: "a"}

    mort = '| | | | | | | | '
    #potence3 = '├'
    #potence4 = '├─'
    potence5 = '├┐'
    potence2 = '│'
    potence1 = '┴'
    jeux_pendu = True
    FIN = False
    depart = 1
    total_lettre = ""

    while jeux_pendu is True:

        if depart == 1:
            pendu = ''
            x = randrange(0, 30)
            choix_du_mot = mot_pendu[x]
            Xword = "x" * (len(choix_du_mot))
            list_Xword = list(''.join(Xword))
            liste_choix_du_mot = list(choix_du_mot)
            liste_choix_du_motR = list(choix_du_mot)
            total_lettre = ""
            print("Voici le mot à deviner ! :", Xword)
            CheatCode(NewPlayer, choix_du_mot)
            print()
            depart = 0

        if not FIN:
            sleep(0.5)
            lettre_proposee = input("Proposes une lettre qui serait contenue dans ce mot : ").lower()
            print()

        for chiffre in lettre_proposee:
            if chiffre in chiffres_interdits:
                print("Keske tu fous ?! C'est pas une lettre ça non ? ")
                jeux_pendu = True

        if len(lettre_proposee) > 1:
            print("Une seule lettre à la fois !")
            print()
            continue

        if lettre_proposee not in total_lettre:
            total_lettre += lettre_proposee
            try:
                variable_juste_pour_test = liste_choix_du_motR.index(lettre_proposee)
            except ValueError:
                print("Désolé :/")
                print()
                pendu += '| '
                score[NewPlayer] -= 1
                ajoutS(score)
                print(pendu)
                print("- 1 Pts")
                print(''.join(list_Xword))
                jeux_pendu = True
        else:
            print("Tu as déjà essayé ça !")
            print()
            print(''.join(list_Xword))
            print()

        if pendu == mort:
            x1 = randrange(0, 11)
            dead = 'Vous êtes mort --->  ±  *R.I.P.* ', epitaphe[x1]
            print(potence5)
            print(potence2)
            print(potence2)
            print(potence2)
            print(potence1)
            print(dead)
            FIN = True

        if (lettre_proposee not in liste_choix_du_mot) and (lettre_proposee in liste_choix_du_motR):
            lettre_proposee = lettre_proposee.upper()
            print("Tu as trouvé tous les", lettre_proposee, "dans ce mot ;)")
            lettre_proposee = lettre_proposee.lower()

        if lettre_proposee in liste_choix_du_mot:
            emplacement_lettre = liste_choix_du_mot.index(lettre_proposee)
            list_Xword[emplacement_lettre] = lettre_proposee
            liste_choix_du_mot[emplacement_lettre] = '0'
            print("Bravo !! Une lettre en moins à trouver ! ")
            print(''.join(list_Xword))

        if E in liste_choix_du_mot:
            emplacement_lettre = liste_choix_du_mot.index(E)
            list_Xword[emplacement_lettre] = E
            liste_choix_du_mot[emplacement_lettre] = '0'
            print("Les é et è te sont révélés *!*")
            print(''.join(list_Xword))

        if e in liste_choix_du_mot:
            emplacement_lettre = liste_choix_du_mot.index(e)
            list_Xword[emplacement_lettre] = e
            liste_choix_du_mot[emplacement_lettre] = '0'
            print("Les é et è te sont révélés *!*")
            print(''.join(list_Xword))

        if list(list_Xword) == liste_choix_du_motR:
            print("Tu as gagné !!! :D ")
            print()
            score[NewPlayer] += 350
            ajoutS(score)
            print("+ 350 Pts !!")
            FIN = True
            depart = 0

        while FIN:
            relance = input("Tu veux recommencer le pendu ? : ")
            print()
            if relance in OUI:
                depart = 1
                FIN = False
                continue
            if relance in NON:
                FIN = False
                jeux_pendu = False
                game = True
                pendu = False
            elif relance not in NON or OUI:
                print("Je n'ai pas compris ? ^___^!")
                print()
            if score[NewPlayer] <= 0:
                jeux_pendu = False
        else:
            EspaceTemps(1)
    if jeux_pendu is False:
        ajoutS(score)
        print()
        print(remerciements)
        print()


### Garage ###

#
# def charger_doc():
#     """Cette fonction va charger un fichier si il existe"""
#     # On essai de charger le fichier, on renvoie un dico vide si ça ne marche pas
#     try:
#         voc = pickle.load(open('donnees', "rb"))
#     except IOError:
#         voc = {}
#     return voc
#
# def sauvegarder_scores(dico_score, nom_fichier):
#     pickle.dump(dico_score, open(nom_fichier, "wb"))
#
# def Load():
#     d = {}
#     with open('donnees', 'rb') as f:
#         while True:
#             try:
#                 a = pickle.load(f)
#             except EOFError:
#                 break
#             else:
#                 d.update(a)
    # do stuff with d

#del score['chouki*']
# score.pop("40")
#def ajoutS(score) :
#    with open('donnees', 'ab') as fichier :
#        mon_pickler = pickle.Pickler(fichier)
#        mon_pickler.dump(score)
"""format du .format :"""
#print("{0} a eu {1} ans. On a fêté les {1} ans de {0}." .format("Pierre", 25))
"""concatenation %"""
# monA=12
# monB=35.6
# monC="abcd"
# monD=7.8251896
# print("A=%d, B=%f, D=%.3f, C=%s et Z=%f // A=%d " %(monA,monB,monD,monC,483,monA))
