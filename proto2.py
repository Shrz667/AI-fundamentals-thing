# import tkinter as tk
# import random
# import heapq

# # Etat final du jeu
# objectif = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# # Etat de depart
# jeu = list(objectif)
# coups = 0
# en_cours = False

# # Creer la fenetre
# fenetre = tk.Tk()
# fenetre.title("Jeu de Taquin avec A*")
# fenetre.geometry("400x550")
# fenetre.resizable(False, False)

# # Titre
# titre = tk.Label(
#     fenetre,
#     text="JEU DE TAQUIN",
#     font=("Arial", 20, "bold")
# )
# titre.pack(pady=10)

# # Compteur de coups
# info = tk.Label(fenetre, text="Coups : 0",
#                 font=("Arial", 12))
# info.pack()

# # Plateau
# plateau = tk.Frame(fenetre)
# plateau.pack(pady=10)

# # Message
# message = tk.Label(fenetre, text="Melange le jeu !",
#                    font=("Arial", 11))
# message.pack(pady=5)

# # Liste des boutons
# boutons = []


# # Calculer la distance de Manhattan
# def heuristique(etat):
#     distance = 0

#     for i in range(9):
#         nombre = etat[i]

#         if nombre != 0:
#             position_finale = nombre - 1

#             ligne = i // 3
#             colonne = i % 3

#             ligne_finale = position_finale // 3
#             colonne_finale = position_finale % 3

#             distance = distance + abs(ligne - ligne_finale)
#             distance = distance + abs(colonne - colonne_finale)

#     return distance


# # Trouver les etats voisins
# def voisins(etat):
#     resultat = []

#     vide = etat.index(0)

#     positions = []

#     if vide % 3 > 0:
#         positions.append(vide - 1)

#     if vide % 3 < 2:
#         positions.append(vide + 1)

#     if vide // 3 > 0:
#         positions.append(vide - 3)

#     if vide // 3 < 2:
#         positions.append(vide + 3)

#     for position in positions:
#         nouveau = list(etat)

#         nouveau[vide] = nouveau[position]
#         nouveau[position] = 0

#         resultat.append(tuple(nouveau))

#     return resultat


# # Algorithme A*
# def a_etoile(depart):

#     liste_ouverte = []
#     heapq.heappush(
#         liste_ouverte,
#         (heuristique(depart), 0, depart)
#     )

#     parents = {}
#     couts = {depart: 0}

#     while liste_ouverte:

#         f, g, courant = heapq.heappop(liste_ouverte)

#         if g != couts[courant]:
#             continue

#         # Si on trouve la solution
#         if courant == objectif:

#             chemin = [courant]

#             while courant in parents:
#                 courant = parents[courant]
#                 chemin.append(courant)

#             chemin.reverse()
#             return chemin

#         # Examiner les voisins
#         for voisin in voisins(courant):

#             nouveau_cout = g + 1

#             if voisin not in couts or nouveau_cout < couts[voisin]:

#                 couts[voisin] = nouveau_cout
#                 parents[voisin] = courant

#                 f = nouveau_cout + heuristique(voisin)

#                 heapq.heappush(
#                     liste_ouverte,
#                     (f, nouveau_cout, voisin)
#                 )

#     return []


# # Afficher le plateau
# def afficher():
#     for i in range(9):

#         if jeu[i] == 0:
#             boutons[i].config(
#                 text="",
#                 bg="white"
#             )
#         else:
#             boutons[i].config(
#                 text=str(jeu[i]),
#                 bg="lightblue"
#             )


# # Deplacer une case
# def deplacer(position):

#     global coups

#     if en_cours:
#         return

#     vide = jeu.index(0)

#     if (position // 3 == vide // 3
#             and abs(position - vide) == 1) or abs(position - vide) == 3:

#         jeu[vide] = jeu[position]
#         jeu[position] = 0

#         coups = coups + 1
#         info.config(text="Coups : " + str(coups))

#         afficher()

#         if tuple(jeu) == objectif:
#             message.config(text="Bravo ! Tu as gagne !")


# # Melanger le jeu
# def melanger():

#     global coups

#     if en_cours:
#         return

#     jeu[:] = objectif

#     # Faire 20 deplacements aleatoires
#     for i in range(20):

#         vide = jeu.index(0)
#         liste = voisins(tuple(jeu))
#         choix = random.choice(liste)

#         jeu[:] = choix

#     coups = 0
#     info.config(text="Coups : 0")
#     message.config(text="Trouve la solution !")

#     afficher()

# #resoudre le jeu 

# def resoudre():

#     global en_cours, coups

#     if en_cours:
#         return

#     en_cours = True

#     boutons_melanger.config(state="disabled")
#     bouton_a.config(state="disabled")

#     message.config(text="Recherche de la solution...")
#     fenetre.update()

#     depart = tuple(jeu)

#     chemin = a_etoile(depart)

#     if chemin:
#         jeu[:] = chemin[-1]

#         coups = len(chemin) - 1

#         info.config(text="Coups : " + str(coups))

#         afficher()

#         message.config(text="Solution trouvee avec A* !")

#     else:
#         message.config(text="Aucune solution trouvee !")

#     en_cours = False

#     boutons_melanger.config(state="normal")
#     bouton_a.config(state="normal")


# # Creer les 9 boutons
# for i in range(9):

#     bouton = tk.Button(
#         plateau,
#         text=str(jeu[i]),
#         font=("Arial", 20, "bold"),
#         width=4,
#         height=2,
#         command=lambda i=i: deplacer(i)
#     )

#     bouton.grid(
#         row=i // 3,
#         column=i % 3,
#         padx=3,
#         pady=3
#     )

#     boutons.append(bouton)


# # Bouton melanger
# boutons_melanger = tk.Button(
#     fenetre,
#     text="Melanger",
#     font=("Arial", 11),
#     command=melanger
# )
# boutons_melanger.pack(pady=5)

# # Bouton A*
# bouton_a = tk.Button(
#     fenetre,
#     text="Resoudre avec A*",
#     font=("Arial", 11, "bold"),
#     command=resoudre
# )
# bouton_a.pack(pady=5)

# # Afficher le jeu et lancer la fenetre
# afficher()
# fenetre.mainloop()