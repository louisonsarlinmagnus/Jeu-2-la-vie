from classes.grille import Grille
import time


def main():
    vie = Grille(25, 10)
    vie.remplir_alea(55)
    vie.affecte_voisins()
    while True:
        print("\u001B[H\u001B[J") #On met un caractère d'échapement
        print(vie) #On affiche la grille
        print("\n") #On saute une ligne pour bien voir la différence avec la pahse d'avant
        time.sleep(0.5)
        vie.jeu()
        vie.actualise()


main()