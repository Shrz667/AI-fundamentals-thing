from tkinter import Tk, Label, Button
import tkinter as tk





window = Tk()
window.title("Puissance 4")
window.geometry("900x600")
window.configure(bg="#172B40")

grille = [[None for _ in range(7)] for _ in range(6)]
joueur = 1
cercles = [[None for _ in range(7)] for _ in range(6)]


             


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


def lancerhxh():
    global mode
    mode = "hxh"
    x.pack_forget()
    afficher_plateau()

def lancerhvb():
    global mode
    mode = "hvb"
    x.pack_forget()
    afficher_plateau()

def colonnes_libres():
     return [j for j in range(7) if grille[0][j] is None]    

def ligne_libre(j):
     for i in range(5, -1, -1):
         if grille[i][j] is None:
             return i
     return None   


def tester(j, lettre):
     # il pose f la case a joiuer mais without output just to see
     i = ligne_libre(j)
     grille[i][j] = lettre
     gagne = gagnant() is not None
     grille[i][j] = None
     return gagne
 
 



def choix_bot():
    ordre = [3, 2, 4, 1, 5, 0, 6]     # hna its thing abt the center thing               
    libres = colonnes_libres()

    # if its valid in one move je joue
    for j in ordre:
        if j in libres and tester(j, "J"):
            return j

   #si le h is at 1 move from winnig j abondone et le bloque priorite
    for j in ordre:
        if j in libres and tester(j, "R"):
            return j
        

# hna dans le cas diagonael plus bref quand y as 2 options de jeu je commence par gauche
    for j in ordre:
        if j in colonnes_libres():
            i = ligne_libre(j)
            grille[i][j] = "R"                     
            menaces = 0 #ida laeb hna sema mshi hadja
            for k in colonnes_libres():
                if tester(k, "R"):
                    menaces += 1     # mais la non faut bloquer coute que coute                
            grille[i][j] = None                  
            if menaces >= 2:
                return j          
            
    # je privilegie centyre sauf si blokani
    for j in ordre:
        if j in libres:
            i = ligne_libre(j)
            grille[i][j] = "J"                       
            danger = i > 0 and tester(j, "R")        
            grille[i][j] = None                   
            if not danger:
                return j

                                 

    return libres[0]  # hna je prend lwla vide ida lokhrin mamchawch


def gagnant():
    # horizontal 
    for i in range(6):
        for j in range(4):
            if grille[i][j] is not None and grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3]:
                return grille[i][j]

    # vertical 
    for i in range(3):
        for j in range(7):
            if grille[i][j] is not None and grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j]:
                return grille[i][j]

    # diagonale vers le bas et haut  à droite
    for i in range(3):
        for j in range(4):
            if grille[i][j] is not None and grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3]:
                return grille[i][j]

    # diagonale vers le bas et haut à gauche
    for i in range(3):
        for j in range(3, 7):
            if grille[i][j] is not None and grille[i][j] == grille[i+1][j-1] == grille[i+2][j-2] == grille[i+3][j-3]:
                return grille[i][j]

    return None

    

#laezem vicroire ida it seems obv
    #if not i have to create a beneficial menace
    #ida maqderch i place it fl pplassa lwwla win je peux creer une fenetre et tt ca en bloquant le rouge


def jouer(event):
    if mode == "hvb" and joueur == 2:
        return                                  
    poser(event.x // 90)


def poser(j):
    global joueur
    for i in range(5, -1, -1):
        if grille[i][j] is None:
            if joueur == 1:
                lettre = "R"
                player="Rouge"
                couleur = "#C96F72"
            else:
                lettre = "J"
                player="Jaune"
                couleur = "#E8C878"

            grille[i][j] = lettre
            canvas.itemconfig(cercles[i][j], fill=couleur)

            if gagnant() is not None:
                canvas.unbind("<Button-1>")
                canvas.create_text(315, 270, text=player + " gagne !",
                                   fill=couleur, font=("Goldman", 40))
            elif not colonnes_libres():
                canvas.unbind("<Button-1>")
                canvas.create_text(315, 270, text="Match nul",
                                   fill=couleur, font=("Goldman", 40))
            else:
                joueur = 2 if joueur == 1 else 1
                if mode == "hvb" and joueur == 2:
                    window.after(500, lambda: poser(choix_bot()))
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
