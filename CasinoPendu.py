# -*-coding:utf-8 -*
#import os

from fonctionsPenduCasino import *

remember = False
game = True
pendu = False
casino = False

while not remember:
    Remember()
    remember = GetRemember()

while game:
    Menu()
    game = GetGame()
    casino = GetCasino()
    pendu = GetPendu()
    #DelPseudo('testos')

    while casino:
        Casino()
        game = GetGame()
        casino = GetCasino()

    while pendu:
        Pendu()
        game = GetGame()
        pendu = GetCasino()