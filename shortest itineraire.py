import math
import random 
import csv


class Ville:
    def __init__(self, nom, x, y):
        self.nom = nom
        self.x = x
        self.y = y

villes = []
with open("algeria_20_cities_import.csv", encoding="utf-8") as f:
    for ligne in csv.DictReader(f):
        villes.append(Ville(ligne["city"], float(ligne["x_km"]), float(ligne["y_km"])))


depart = next(v for v in villes if v.nom == "Algiers")
print ("Ville de départ :", depart.nom, depart.x, depart.y)
print ( len(villes))


def distance(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)


def cout(tournee):
    total = 0
    for i in range(len(tournee)):
        suivante = tournee[(i + 1) % len(tournee)]   # la dernière revient à la première
        total += distance(tournee[i], suivante)
    return total

def afficher_trajet(tournee):
    cumul = 0
    print(f"{tournee[0].nom:<20} cumul = 0.0 km")
    for i in range(1, len(tournee)):
        d = distance(tournee[i - 1], tournee[i])
        cumul += d
        print(f"{tournee[i].nom:<20}   cumul = {cumul:8.1f} km" f" (+{d:7.1f} km)")
    d = distance(tournee[-1], tournee[0])
    cumul += d
    print(f"{tournee[0].nom:<20} cumul = {cumul:8.1f} km  (retour)")


def tournee():
    autres = [v for v in villes if v is not depart]
    random.shuffle(autres)
    return [depart] + autres





def recherche_aleatoire(): 
  meilleure = tournee()
  meilleur_cout = cout(meilleure)
  for _ in range(10):
        t = tournee()
        c = cout(t)
        if c < meilleur_cout:
            meilleure, meilleur_cout = t, c
            return meilleure, meilleur_cout

#pour voir si ca maeche  
t,c= recherche_aleatoire()
afficher_trajet(t)



def recherche_local():
 pass 


def hill_climbing():
    pass 

def recui_simule():
   pass

def atbu_surch ():
   pass

def genetic ():
   pass

