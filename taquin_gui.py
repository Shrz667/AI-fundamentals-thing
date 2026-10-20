# import tkinter as tk
# from tkinter import ttk, messagebox

# # 0 = case vide
# ETAT_INITIAL = [
#     [1, 2, 3],
#     [8, 0, 4],
#     [7, 6, 5],
# ]


# class Damier(tk.Frame):
#     """Un damier 3x3. Si cliquable=True, l'utilisateur glisse les jetons vers la case vide."""

#     def __init__(self, parent, etat, cliquable=False):
#         super().__init__(parent, bg="#34495e", padx=4, pady=4)
#         self.etat_depart = [ligne[:] for ligne in etat]
#         self.etat = [ligne[:] for ligne in etat]
#         self.cliquable = cliquable
#         self.boutons = [[None] * 3 for _ in range(3)]

#         for r in range(3):
#             for c in range(3):
#                 b = tk.Button(
#                     self, width=4, height=2, font=("Arial", 24, "bold"),
#                     relief="flat", command=lambda r=r, c=c: self.clic(r, c),
#                 )
#                 b.grid(row=r, column=c, padx=2, pady=2)
#                 self.boutons[r][c] = b
#         self.dessiner()

#     def dessiner(self):
#         for r in range(3):
#             for c in range(3):
#                 v = self.etat[r][c]
#                 b = self.boutons[r][c]
#                 if v == 0:
#                     b.config(text="", bg="#bdc3c7", state="disabled")
#                 else:
#                     b.config(text=str(v), bg="#ecf0f1",
#                              state="normal" if self.cliquable else "disabled",
#                              disabledforeground="black")

#     def position_vide(self):
#         for r in range(3):
#             for c in range(3):
#                 if self.etat[r][c] == 0:
#                     return r, c

#     def clic(self, r, c):
#         if not self.cliquable:
#             return
#         vr, vc = self.position_vide()
#         # le jeton doit etre voisin de la case vide
#         if abs(vr - r) + abs(vc - c) == 1:
#             self.etat[vr][vc], self.etat[r][c] = self.etat[r][c], 0
#             self.dessiner()

#     def reinitialiser(self):
#         self.etat = [ligne[:] for ligne in self.etat_depart]
#         self.dessiner()

#     def get_etat(self):
#         return [ligne[:] for ligne in self.etat]

#     def set_etat(self, etat):
#         self.etat = [ligne[:] for ligne in etat]
#         self.dessiner()


# class Application(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Projet 1 : Espace d'états - Jeu du Taquin")
#         self.resizable(False, False)

#         ttk.Label(self, text="Jeu du Taquin (3x3)",
#                   font=("Arial", 18, "bold")).pack(pady=(10, 0))
#         ttk.Label(self, text="Glissez les jetons vers la case vide pour créer la configuration finale"
#                   ).pack(pady=(0, 10))

#         # --- zone des deux damiers ---
#         zone = ttk.Frame(self, padding=10)
#         zone.pack()

#         gauche = ttk.Frame(zone)
#         gauche.grid(row=0, column=0, padx=20)
#         ttk.Label(gauche, text="État initial", font=("Arial", 12, "bold")).pack(pady=5)
#         self.damier_initial = Damier(gauche, ETAT_INITIAL, cliquable=False)
#         self.damier_initial.pack()

#         droite = ttk.Frame(zone)
#         droite.grid(row=0, column=1, padx=20)
#         ttk.Label(droite, text="État final (à créer)", font=("Arial", 12, "bold")).pack(pady=5)
#         self.damier_final = Damier(droite, ETAT_INITIAL, cliquable=True)
#         self.damier_final.pack()

#         # --- boutons ---
#         barre = ttk.Frame(self, padding=5)
#         barre.pack()
#         ttk.Button(barre, text="Réinitialiser",
#                    command=self.damier_final.reinitialiser).grid(row=0, column=0, padx=5)
#         ttk.Button(barre, text="Lancer l'algorithme A",
#                    command=self.lancer).grid(row=0, column=1, padx=5)
#         ttk.Button(barre, text="Effacer le journal",
#                    command=self.effacer_journal).grid(row=0, column=2, padx=5)

#         # --- journal : etapes intermediaires ---
#         ttk.Label(self, text="Étapes intermédiaires (scores et état du damier)",
#                   font=("Arial", 10, "bold")).pack(anchor="w", padx=15, pady=(10, 0))
#         cadre = ttk.Frame(self)
#         cadre.pack(padx=15, pady=(0, 15), fill="both", expand=True)
#         self.journal = tk.Text(cadre, width=60, height=12, font=("Consolas", 10))
#         defil = ttk.Scrollbar(cadre, command=self.journal.yview)
#         self.journal.config(yscrollcommand=defil.set)
#         self.journal.pack(side="left", fill="both", expand=True)
#         defil.pack(side="right", fill="y")

#     # ---------- utilitaires pour l'affichage ----------
#     def etat_en_texte(self, etat):
#         return "\n".join(" ".join(str(v) if v else "_" for v in ligne) for ligne in etat)

#     def afficher_etape(self, numero, etat, g, h):
#         """A appeler depuis l'algorithme A a chaque exploration."""
#         f = g + h
#         self.journal.insert("end", f"--- Étape {numero} --- g={g}  h={h}  f={f}\n")
#         self.journal.insert("end", self.etat_en_texte(etat) + "\n\n")
#         self.journal.see("end")

#     def effacer_journal(self):
#         self.journal.delete("1.0", "end")

#     # ---------- bouton Lancer ----------
#     def lancer(self):
#         initial = self.damier_initial.get_etat()
#         final = self.damier_final.get_etat()
#         if initial == final:
#             messagebox.showinfo("Info", "L'état final est identique à l'état initial.")
#             return
#         self.journal.insert("end", "État initial :\n" + self.etat_en_texte(initial) + "\n\n")
#         self.journal.insert("end", "État final :\n" + self.etat_en_texte(final) + "\n\n")
#         self.journal.insert("end", "TODO : appliquer l'algorithme A ici.\n\n")
#         self.journal.see("end")


# if __name__ == "__main__":
#     Application().mainloop()


import tkinter as tk
import random
import heapq

# Etat final du jeu
objectif = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Etat de depart
jeu = list(objectif)
coups = 0
en_cours = False

# Creer la fenetre
fenetre = tk.Tk()
fenetre.title("Jeu de Taquin avec A*")
fenetre.geometry("400x550")
fenetre.resizable(False, False)

# Titre
titre = tk.Label(
    fenetre,
    text="JEU DE TAQUIN",
    font=("Arial", 20, "bold")
)
titre.pack(pady=10)

# Compteur de coups
info = tk.Label(fenetre, text="Coups : 0",
                font=("Arial", 12))
info.pack()

# Plateau
plateau = tk.Frame(fenetre)
plateau.pack(pady=10)

# Message
message = tk.Label(fenetre, text="Melange le jeu !",
                   font=("Arial", 11))
message.pack(pady=5)

# Liste des boutons
boutons = []


# Calculer la distance de Manhattan
def heuristique(etat):
    distance = 0

    for i in range(9):
        nombre = etat[i]

        if nombre != 0:
            position_finale = nombre - 1

            ligne = i // 3
            colonne = i % 3

            ligne_finale = position_finale // 3
            colonne_finale = position_finale % 3

            distance = distance + abs(ligne - ligne_finale)
            distance = distance + abs(colonne - colonne_finale)

    return distance


# Trouver les etats voisins
def voisins(etat):
    resultat = []

    vide = etat.index(0)

    positions = []

    if vide % 3 > 0:
        positions.append(vide - 1)

    if vide % 3 < 2:
        positions.append(vide + 1)

    if vide // 3 > 0:
        positions.append(vide - 3)

    if vide // 3 < 2:
        positions.append(vide + 3)

    for position in positions:
        nouveau = list(etat)

        nouveau[vide] = nouveau[position]
        nouveau[position] = 0

        resultat.append(tuple(nouveau))

    return resultat


# Algorithme A*
def a_etoile(depart):

    liste_ouverte = []
    heapq.heappush(
        liste_ouverte,
        (heuristique(depart), 0, depart)
    )

    parents = {}
    couts = {depart: 0}

    while liste_ouverte:

        f, g, courant = heapq.heappop(liste_ouverte)

        if g != couts[courant]:
            continue

        # Si on trouve la solution
        if courant == objectif:

            chemin = [courant]

            while courant in parents:
                courant = parents[courant]
                chemin.append(courant)

            chemin.reverse()
            return chemin

        # Examiner les voisins
        for voisin in voisins(courant):

            nouveau_cout = g + 1

            if voisin not in couts or nouveau_cout < couts[voisin]:

                couts[voisin] = nouveau_cout
                parents[voisin] = courant

                f = nouveau_cout + heuristique(voisin)

                heapq.heappush(
                    liste_ouverte,
                    (f, nouveau_cout, voisin)
                )

    return []


# Afficher le plateau
def afficher():
    for i in range(9):

        if jeu[i] == 0:
            boutons[i].config(
                text="",
                bg="white"
            )
        else:
            boutons[i].config(
                text=str(jeu[i]),
                bg="lightblue"
            )


# Deplacer une case
def deplacer(position):

    global coups

    if en_cours:
        return

    vide = jeu.index(0)

    if (position // 3 == vide // 3
            and abs(position - vide) == 1) or abs(position - vide) == 3:

        jeu[vide] = jeu[position]
        jeu[position] = 0

        coups = coups + 1
        info.config(text="Coups : " + str(coups))

        afficher()

        if tuple(jeu) == objectif:
            message.config(text="Bravo ! Tu as gagne !")


# Melanger le jeu
def melanger():

    global coups

    if en_cours:
        return

    jeu[:] = objectif

    # Faire 20 deplacements aleatoires
    for i in range(20):

        vide = jeu.index(0)
        liste = voisins(tuple(jeu))
        choix = random.choice(liste)

        jeu[:] = choix

    coups = 0
    info.config(text="Coups : 0")
    message.config(text="Trouve la solution !")

    afficher()

#resoudre le jeu 

def resoudre():

    global en_cours, coups

    if en_cours:
        return

    en_cours = True

    boutons_melanger.config(state="disabled")
    bouton_a.config(state="disabled")

    message.config(text="Recherche de la solution...")
    fenetre.update()

    depart = tuple(jeu)

    chemin = a_etoile(depart)

    if chemin:
        jeu[:] = chemin[-1]

        coups = len(chemin) - 1

        info.config(text="Coups : " + str(coups))

        afficher()

        message.config(text="Solution trouvee avec A* !")

    else:
        message.config(text="Aucune solution trouvee !")

    en_cours = False

    boutons_melanger.config(state="normal")
    bouton_a.config(state="normal")


# Creer les 9 boutons
for i in range(9):

    bouton = tk.Button(
        plateau,
        text=str(jeu[i]),
        font=("Arial", 20, "bold"),
        width=4,
        height=2,
        command=lambda i=i: deplacer(i)
    )

    bouton.grid(
        row=i // 3,
        column=i % 3,
        padx=3,
        pady=3
    )

    boutons.append(bouton)


# Bouton melanger
boutons_melanger = tk.Button(
    fenetre,
    text="Melanger",
    font=("Arial", 11),
    command=melanger
)
boutons_melanger.pack(pady=5)

# Bouton A*
bouton_a = tk.Button(
    fenetre,
    text="Resoudre avec A*",
    font=("Arial", 11, "bold"),
    command=resoudre
)
bouton_a.pack(pady=5)

# Afficher le jeu et lancer la fenetre
afficher()
fenetre.mainloop()