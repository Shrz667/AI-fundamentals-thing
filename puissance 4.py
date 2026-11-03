from tkinter import Tk, Label, Button
import tkinter as tk





window = Tk()
window.title("Puissance 4")
window.geometry("900x600")
window.configure(bg="#172B40")

grille = [[None for _ in range(7)] for _ in range(6)]
def lancerhxh():
    x.pack_forget()
    afficher_plateau()


def lancerhvb():
    x.pack_forget()
    afficher_plateau()
joueur = 1
cercles = [[None for _ in range(7)] for _ in range(6)]


def jouer(event):
    global joueur
    j = event.x // 90                      
    for i in range(5, -1, -1):           
        if grille[i][j] is None:          
            grille[i][j] = joueur
            if joueur == 1:
                canvas.itemconfig(cercles[i][j], fill="#C96F72")  
                joueur = 2
            else:
                canvas.itemconfig(cercles[i][j], fill="#E8C878")   
                joueur = 1
            break                          


def afficher_plateau():
    global canvas
    canvas = tk.Canvas(window, width=630, height=540, bg="#365E7D", highlightthickness=0)
    canvas.pack(expand=True)
    for i in range(6):
        for j in range(7):
            cercles[i][j] = canvas.create_oval(j*90 + 8, i*90 + 8,
                                               (j+1)*90 - 8, (i+1)*90 - 8,
                                               fill="#172B40", outline="#75A8C9", width=2)
    canvas.bind("<Button-1>", jouer)


def gagnant():
    # horizontal : 6 lignes, la 1re case va de la colonne 0 à 3
    for i in range(6):
        for j in range(4):
            if grille[i][j] is not None and grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3]:
                return grille[i][j]

    # vertical : la 1re case va de la ligne 0 à 2
    for i in range(3):
        for j in range(7):
            if grille[i][j] is not None and grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j]:
                return grille[i][j]

    # diagonale vers le bas à droite
    for i in range(3):
        for j in range(4):
            if grille[i][j] is not None and grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3]:
                return grille[i][j]

    # diagonale vers le bas à gauche
    for i in range(3):
        for j in range(3, 7):
            if grille[i][j] is not None and grille[i][j] == grille[i+1][j-1] == grille[i+2][j-2] == grille[i+3][j-3]:
                return grille[i][j]

    return None


def jouer(event):
    global joueur
    j = event.x // 90
    for i in range(5, -1, -1):
        if grille[i][j] is None:
            if joueur == 1:
                lettre = "Rouge"
                couleur = "#C96F72"
            else:
                lettre = "Jaune"
                couleur = "#E8C878"

            grille[i][j] = lettre
            canvas.itemconfig(cercles[i][j], fill=couleur)

            if gagnant() is not None:
                canvas.unbind("<Button-1>")
                canvas.create_text(315, 270, text=lettre + " gagne !",
                                   fill="#FFFFFF", font=("Goldman", 40))
            else:
                joueur = 2 if joueur == 1 else 1
            break     
                                          
x=tk.Frame(window)
txt=tk.Label(x,text = "Puissance 4 ",bg="#E8C878",fg="#C96F72",font =("Goldman",30))
txt2=tk.Label(x,text = "Choisissez le mode de jeu",bg="#E8C878",fg="#C96F72",font =("Goldman",20))
txt.pack(padx=10,pady=10)
txt2.pack(padx=10,pady=10)

hh=tk.Button(x,text = "Human VS Human",bg="#75A8C9",font =("Goldman",10),command=lancerhxh)
hh.pack(padx=100,pady=50)
hb=tk.Button(x,text = "Human VS Bot",bg="#75A8C9",font =("Goldman",10),command=lancerhvb)
hb.pack(padx=100,pady=50)
x.configure(bg="#365E7D")
x.configure(width=350,height=250)



x.pack(side ="top",expand=True)

window.mainloop()
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
