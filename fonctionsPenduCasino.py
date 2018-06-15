"""Fonctions automatisant l'ajout des scores dans le ficher binaire"""

"""with open(nom_fichier,"wb") as fich:  # Il est conseillé d'utiliser with

   pickle.dump(objet, fich)              # objet est enregistré dans fichier

   objet = pickle.load(fich)             # on récupère l'objet suivant de fichier """

import os
import pickle
from time import sleep
from random import randrange


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
        #print('scores chargés :', score,'\n')
        return score

def ajoutS(new_score) :
    with open('donnees', 'wb') as fichier :
        pickle.dump(new_score, fichier)

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
        print("salut Pouya ! Merci de corriger mon Pendu 3.0 haha, bisous à vous 2 \n"
              "Tu entre en mode GodeMode : your intelligence up to 23, you guess and \n"
              "you feel every words asked in pendu !")
        print("CheatCode ON :", mot)



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
