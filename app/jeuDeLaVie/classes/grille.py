from __future__ import annotations
from jeuDeLaVie.classes.cellule import Cellule
from typing import List
from random import random


class Grille():
    def __init__(self: Grille, hauteur: int, largeur: int) -> None:
        self.hauteur = hauteur
        self.largeur = largeur
        self.matrice = self.set_matrice()

    def set_matrice(self: Grille) -> List[Cellule]:
        matrice = []
        for i in range(self.largeur):
            liste = []
            for j in range(self.hauteur):
                liste.append(Cellule())
            matrice.append(liste)
        return matrice

    def dans_grille(self: Grille, i: int, j: int) -> bool:
        return 0 <= i < self.largeur and 0 <= j < self.hauteur

    def setXY(self: Grille, i: int, j: int, cellule: Cellule) -> None:
        if self.dans_grille(i, j):
            self.matrice[i][j] = cellule
        else:
            raise IndexError(str(i, j))

    def getXY(self: Grille, i: int, j: int) -> Cellule:
        if self.dans_grille(i, j):
            return self.matrice[i][j]
        else:
            raise IndexError(str(i, j))

    def get_largeur(self: Grille) -> int:
        return self.largeur

    def get_hauteur(self: Grille) -> int:
        return self.hauteur

    @staticmethod
    def est_voisin(i: int, j: int, x: int, y: int) -> bool:
        return (abs(x - i) == 1) or (abs(y - j) == 1)

    def get_voisins(self: Grille, x: int, y: int) -> List[Cellule]:
        voisins = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.dans_grille(i, j) and Grille.est_voisin(x, y, i, j):
                    voisins.append(self.getXY(i, j))
        return voisins

    def affecte_voisins(self: Grille):
        for i in range(self.largeur):
            for j in range(self.hauteur):
                cellule = self.getXY(i, j)
                cellule.set_voisins(self.get_voisins(i, j))

    def __str__(self: Grille) -> str:
        chaine = ""
        for i in range(self.largeur):
            for j in range(self.hauteur):
                chaine += str(self.getXY(i, j))
            chaine += "<br>"#"\n"
        return chaine

    def remplir_alea(self, taux: int) -> None:
        for i in range(self.largeur):
            for j in range(self.hauteur):
                if random() <= (taux / 100):
                    cellule = self.getXY(i, j)
                    cellule.naitre()
                    cellule.basculer()
                    # print(cellule)

    def jeu(self: Grille) -> None:
        for i in range(self.largeur):
            for j in range(self.hauteur):
                cellule = self.getXY(i, j)
                cellule.calcule_etat_futur()

    def actualise(self: Grille) -> None:
        for i in range(self.largeur):
            for j in range(self.hauteur):
                cellule = self.getXY(i, j)
                cellule.basculer()

if __name__ == "__main__":
    grille = Grille(4, 5)
    #print(grille)