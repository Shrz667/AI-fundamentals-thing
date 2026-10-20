import tkinter as tk
from tkinter import ttk, messagebox

# 0 = case vide
ETAT_INITIAL = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5],
]


class Damier(tk.Frame):
    """Un damier 3x3. Si cliquable=True, l'utilisateur glisse les jetons vers la case vide."""

    def __init__(self, parent, etat, cliquable=False):
        super().__init__(parent, bg="#34495e", padx=4, pady=4)
        self.etat_depart = [ligne[:] for ligne in etat]
        self.etat = [ligne[:] for ligne in etat]
        self.cliquable = cliquable
        self.boutons = [[None] * 3 for _ in range(3)]

        for r in range(3):
            for c in range(3):
                b = tk.Button(
                    self, width=4, height=2, font=("Arial", 24, "bold"),
                    relief="flat", command=lambda r=r, c=c: self.clic(r, c),
                )
                b.grid(row=r, column=c, padx=2, pady=2)
                self.boutons[r][c] = b
        self.dessiner()

    def dessiner(self):
        for r in range(3):
            for c in range(3):
                v = self.etat[r][c]
                b = self.boutons[r][c]
                if v == 0:
                    b.config(text="", bg="#bdc3c7", state="disabled")
                else:
                    b.config(text=str(v), bg="#ecf0f1",
                             state="normal" if self.cliquable else "disabled",
                             disabledforeground="black")

    def position_vide(self):
        for r in range(3):
            for c in range(3):
                if self.etat[r][c] == 0:
                    return r, c

    def clic(self, r, c):
        if not self.cliquable:
            return
        vr, vc = self.position_vide()
        # le jeton doit etre voisin de la case vide
        if abs(vr - r) + abs(vc - c) == 1:
            self.etat[vr][vc], self.etat[r][c] = self.etat[r][c], 0
            self.dessiner()

    def reinitialiser(self):
        self.etat = [ligne[:] for ligne in self.etat_depart]
        self.dessiner()

    def get_etat(self):
        return [ligne[:] for ligne in self.etat]

    def set_etat(self, etat):
        self.etat = [ligne[:] for ligne in etat]
        self.dessiner()


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Projet 1 : Espace d'états - Jeu du Taquin")
        self.resizable(False, False)

        ttk.Label(self, text="Jeu du Taquin (3x3)",
                  font=("Arial", 18, "bold")).pack(pady=(10, 0))
        ttk.Label(self, text="Glissez les jetons vers la case vide pour créer la configuration finale"
                  ).pack(pady=(0, 10))

        # --- zone des deux damiers ---
        zone = ttk.Frame(self, padding=10)
        zone.pack()

        gauche = ttk.Frame(zone)
        gauche.grid(row=0, column=0, padx=20)
        ttk.Label(gauche, text="État initial", font=("Arial", 12, "bold")).pack(pady=5)
        self.damier_initial = Damier(gauche, ETAT_INITIAL, cliquable=False)
        self.damier_initial.pack()

        droite = ttk.Frame(zone)
        droite.grid(row=0, column=1, padx=20)
        ttk.Label(droite, text="État final (à créer)", font=("Arial", 12, "bold")).pack(pady=5)
        self.damier_final = Damier(droite, ETAT_INITIAL, cliquable=True)
        self.damier_final.pack()

        # --- boutons ---
        barre = ttk.Frame(self, padding=5)
        barre.pack()
        ttk.Button(barre, text="Réinitialiser",
                   command=self.damier_final.reinitialiser).grid(row=0, column=0, padx=5)
        ttk.Button(barre, text="Lancer l'algorithme A",
                   command=self.lancer).grid(row=0, column=1, padx=5)
        ttk.Button(barre, text="Effacer le journal",
                   command=self.effacer_journal).grid(row=0, column=2, padx=5)

        # --- journal : etapes intermediaires ---
        ttk.Label(self, text="Étapes intermédiaires (scores et état du damier)",
                  font=("Arial", 10, "bold")).pack(anchor="w", padx=15, pady=(10, 0))
        cadre = ttk.Frame(self)
        cadre.pack(padx=15, pady=(0, 15), fill="both", expand=True)
        self.journal = tk.Text(cadre, width=60, height=12, font=("Consolas", 10))
        defil = ttk.Scrollbar(cadre, command=self.journal.yview)
        self.journal.config(yscrollcommand=defil.set)
        self.journal.pack(side="left", fill="both", expand=True)
        defil.pack(side="right", fill="y")

    # ---------- utilitaires pour l'affichage ----------
    def etat_en_texte(self, etat):
        return "\n".join(" ".join(str(v) if v else "_" for v in ligne) for ligne in etat)

    def afficher_etape(self, numero, etat, g, h):
        """A appeler depuis l'algorithme A a chaque exploration."""
        f = g + h
        self.journal.insert("end", f"--- Étape {numero} --- g={g}  h={h}  f={f}\n")
        self.journal.insert("end", self.etat_en_texte(etat) + "\n\n")
        self.journal.see("end")

    def effacer_journal(self):
        self.journal.delete("1.0", "end")

    # ---------- bouton Lancer ----------
    def lancer(self):
        initial = self.damier_initial.get_etat()
        final = self.damier_final.get_etat()
        if initial == final:
            messagebox.showinfo("Info", "L'état final est identique à l'état initial.")
            return
        self.journal.insert("end", "État initial :\n" + self.etat_en_texte(initial) + "\n\n")
        self.journal.insert("end", "État final :\n" + self.etat_en_texte(final) + "\n\n")
        self.journal.insert("end", "TODO : appliquer l'algorithme A ici.\n\n")
        self.journal.see("end")


if __name__ == "__main__":
    Application().mainloop()