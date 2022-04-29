from __future__ import annotations
from typing import List

class Cellule:
    def __init__(self) -> None:
        self.actuel = False
        self.futur = False
        self.voisins = None
    
    def est_vivant(self: Cellule) -> bool:
            return self.actuel

    def set_voisins(self: Cellule, voisins: List[Cellule]) -> None:
        self.voisins = voisins

    def get_voisins(self: Cellule) -> List[Cellule]:

        return self.voisins

    def naitre(self: Cellule) -> None:
        self.futur = True

    def mourir(self: Cellule) -> None:
        self.futur = False

    def basculer(self: Cellule) -> None:
        self.actuel = self.futur

    def __str__(self: Cellule) -> str:
        # if self.actuel:
        #     chaine = ""
        # else:
        #     chaine = "-"
        return " "

    def calcule_etat_futur(self: Cellule) -> None:
        nbre_voisins_vivants = 0

        for voisin in self.voisins:
            if voisin.est_vivant():
                nbre_voisins_vivants += 1

        if (nbre_voisins_vivants != 2) and (nbre_voisins_vivants != 3) and (self.est_vivant()):
            self.mourir()
        elif (nbre_voisins_vivants == 3) and not (self.est_vivant()):
            self.naitre()
        else:
            self.futur = self.actuel