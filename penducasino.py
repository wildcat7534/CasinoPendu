# -*-coding:utf-8 -*
import os
from fonctions import *
from math import ceil

remember = False
game = False
pendu = False
casino = False
mise = 0
a = ceil(6/4)
OUI = ['oui', 'Oui', 'OIu', 'OUI', 'yes', 'Yes', 'YEs',
       'YES', 'ouais', 'Ouais', 'ok', 'Ok', 'OK', 'Oui !', 'o', 'O']
NON = ['non', 'Non', 'NON', 'no', 'n', 'N']
score = (openScore())

while not remember:
    NewPlayer = (input("Salut ! Qu\'elle est ton pseudo ? : ")).lower()
    EspaceTemps(10)
    if NewPlayer in score:
        print('Salut', NewPlayer, "! Te revoila ! Ton ancien score est de : ", score[NewPlayer])
        EspaceTemps(3)
        remember = True
    if NewPlayer not in score:
        score[NewPlayer] = int(NumMagic())
        print("Voilà quelques points attribués pour commencer :", score[NewPlayer], "Pts/Btc")
        remember = True

while not game:
    pendu = False
    casino = False
    print()
    ask = input("*°*-------*------MENU PRINCIPAL------*------*°*"
                "\n ----> CHOIX DU JEUX : casino ou pendu ou non(N,n) ? --> ")
    if ask == 'pendu':
        EspaceTemps(3)
        print("Je vais lancer le pendu !")
        EspaceTemps(5)
        sleep(1)
        pendu = True
        game = True

    elif ask == 'casino':
        casino = True
        game = True
        print("Je vais lancer le casino !")
        EspaceTemps(7)
        print("      ┼ BIENVENUE DANS CE MAGNIFIQUE CASINO ┼ ")
        EspaceTemps(5)

    elif ask in NON:
        ajoutS(score)
        print()
        print("GOOD BYE, Thanks to you to try me ^_-_^ ")
        print()
        break

    else:
        print("Je n'ai pas compris.")
        print()
        game = False


    while casino:
        print()
        print(NewPlayer, "vous disposez de :", score[NewPlayer], "Btc\n")
        if score[NewPlayer] != 0:
            EspaceTemps(1)
            try:
                mise = int(input("Croupier : 'Faites vos jeux' ! \n"
                                 "Combien misez-vous ? : "))
            except ValueError:
                print(" ERREUR ! : Ceci n'est pas un chiffre non ?")
                continue
            EspaceTemps(1)

            if int(mise > 0) and (int(mise) <= score[NewPlayer]):
                nbr = int(input("Sur quel chiffre misez-vous entre 1 et 36 inclu ? \n"))
                EspaceTemps(3)

                if 0 < nbr < 37:
                    sleep(1)
                    print("Les dès sont lancés !")
                    EspaceTemps(5)
                    sleep(1)
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
                            score[NewPlayer] = ceil(mise * 2.5) + (score[NewPlayer] - mise)
                            ajoutS(score)
                            sleep(1)
                            print("Double pair !", mise, "x2,5 -! \n"
                                  "Gain de : ", ceil(mise * 2.5), " ! ! ")
                    elif PairImpair(nbr) == 'impair' and PairImpair(roulette) == 'impair':
                        EspaceTemps(2)
                        score[NewPlayer] = ceil(mise * 2.5) + (score[NewPlayer] - mise)
                        ajoutS(score)
                        sleep(1)
                        print("Double impair !", mise, "x2,5 -! \n"
                              "Gain de : ", ceil(mise * 2.5), " ! ! ")
                    else:
                        EspaceTemps(1)
                        score[NewPlayer] -= mise
                        ajoutS(score)
                        print("perdu... :/ \n")
                        regame = input("Voulez-vous continuer ? :")
                        if regame in OUI:
                            casino = True
                        elif regame in NON:
                            casino = False
                            game = False
                            continue
                else:
                    EspaceTemps(1)
                    print("Merci de choisir un nombre entre 1 et 36 compris ;) \n")

            if int(mise < 0) or (int(mise) > score[NewPlayer]):
                EspaceTemps(1)
                print("Merci de vouloir miser l'argent que vous possèdez.")
        else:
            casino = False
            ajoutS(score)
            EspaceTemps(1)
            print("Désolé vous n\'avez plus d\'argent, veullez sortir du casino. Merci")
            EspaceTemps(1)
            print("Vous n'avez plus de point vous en pouvez plus jouer ici.")
            EspaceTemps(1)


    while pendu:
        mot_pendu = openMotPendu()
        chiffres_interdits = "1234567890"
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

        mort = '| | | | | | | | | | | | | '
        potence3 = '├'
        potence2 = '│'
        potence1 = '┴'
        potence4 = '├─'
        potence5 = '├┐'
        jeux_pendu = True
        FIN = False
        depart = 1

        while jeux_pendu is True:
            if depart == 1:
                pendu = ''
                x = randrange(0, 30)
                choix_du_mot = mot_pendu[x]
                Xword = "x" * (len(choix_du_mot))
                list_Xword = list(''.join(Xword))
                liste_choix_du_mot = list(choix_du_mot)
                liste_choix_du_motR = list(choix_du_mot)
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
                jeux_pendu = True

            if pendu == mort:
                x1 = randrange(0, 11)
                dead = 'Vous êtes mort --->  ±  *R.I.P.* ', epitaphe[x1]
                print(potence5)
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

            if list(list_Xword) == liste_choix_du_motR:
                print("Tu as gagné !!! :D ")
                print()
                score[NewPlayer] += 350
                ajoutS(score)
                print("+ 350 Pts !!")
                FIN = True
                depart = 0

            while FIN and not casino:
                relance = input("Tu veux recommencer ? : ")
                print()
                if relance in OUI:
                    depart = 1
                    FIN = False
                    continue
                if relance in NON:
                    FIN = False
                    casino = False
                    jeux_pendu = False
                    game = False
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
            print("GOOD BYE, Thanks to you to try me ^____^ ")
            print()