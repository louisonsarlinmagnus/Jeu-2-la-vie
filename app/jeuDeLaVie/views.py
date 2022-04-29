from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from jeuDeLaVie.classes.grille import Grille
import os

vie = Grille(25, 25)
vie.remplir_alea(25)
vie.affecte_voisins()

def index(request):
    # vie = Grille(25, 10)
    # vie.remplir_alea(5)
    # vie.affecte_voisins()
    # while True:
    #     print("\u001B[H\u001B[J") #On met un caractère d'échapement
    #     print(vie) #On affiche la grille
    #     print("\n") #On saute une ligne pour bien voir la différence avec la pahse d'avant
    #     time.sleep(0.5)
    vie.jeu()
    vie.actualise()

    context = {
        'vie' : vie.matrice,
        'range_largeur' : range(int(vie.largeur)),
        'range_hauteur' : range(int(vie.hauteur)),
        'intervalle': 1000,
    }
    
    return render(request, 'jeuDeLaVie/index.html', context)