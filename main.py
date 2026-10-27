from tkinter import Tk, Label, Button
import heapq
from tkinter.scrolledtext import ScrolledText 
import tkinter as tk

fenetre = Tk()
fenetre.title("je suis la") 
fenetre.geometry("800x450")
fenetre.configure(bg="#000000")
shema=[
    [1, 2, 3],
    [8, None, 4],
    [7, 6, 5],
]

x= tk.Frame(fenetre)
# bar= tk.Scrollbar(x)
# bar.pack(side="right", fill="y")

console = ScrolledText(x, width=40, height=20,       
                       bg="black", fg="green",        
                       insertbackground="green",      
                       font=("Consolas", 11),        
                       state="disabled")             
console.pack(fill="both", expand=True)   



def ecrire(message):                           
    console.config(state="normal")             
    console.insert("end", message + "\n")      
    console.see("end")                        
    console.config(state="disabled")


def etat_actuel():                             
    liste = []                                 
    for i in range(3):                         
        for j in range(3):                     
            b = boutons[i][j]                  
            liste.append(0 if b is None else int(b.cget("text"))) 
    return tuple(liste)


def afficher(etat, titre):                    
    ecrire(titre)                              
    for i in range(0, 9, 3):                  
        ligne = ["_" if v == 0 else str(v) for v in etat[i:i+3]]  
        ecrire("[" + ", ".join(ligne) + "]")   # Ex : [8, _, 4]
    ecrire("") 

but = tuple(0 if v is None else v      
            for ligne in shema         
            for v in ligne)            
                                       


def heuristique(etat):                         
    total = 0                                 
    for pos, v in enumerate(etat):           
        if v != 0:                             
            p = but.index(v)                  
            total += abs(pos // 3 - p // 3) + abs(pos % 3 - p % 3) 
    return total



def voisins(etat):                             
    v = etat.index(0)                          
    l, c = divmod(v, 3)                        
    resultat = []                            
    for dl, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):   
        nl, nc = l + dl, c + dc               
        if 0 <= nl < 3 and 0 <= nc < 3:       
            n = nl * 3 + nc                    
            liste = list(etat)                 
            liste[v], liste[n] = liste[n], liste[v]   
            resultat.append(tuple(liste))      
    return resultat

def astar(depart):                            
    file = [(heuristique(depart), 0, depart)]  
    parent = {depart: None}                  
    cout = {depart: 0}                         
    while file:                                
        f, g, etat = heapq.heappop(file)      
        if etat == but:                       
            chemin = []                        
            while etat is not None:
                chemin.append(etat)
                etat = parent[etat]
            return chemin[::-1]               
        if g > cout[etat]:                     
            continue
        for v in voisins(etat):                
            if v not in cout or g + 1 < cout[v]:  
                cout[v] = g + 1               
                parent[v] = etat               
                heapq.heappush(file, (g + 1 + heuristique(v), g + 1, v))  # f = g + h
    return None       


def lancer_astar():                           
    chemin = astar(etat_actuel())              
    if chemin is None:                         
        ecrire("Aucune solution")
        return
    afficher(chemin[0], "État initial (mélangé)")      
    for i, etat in enumerate(chemin[1:], start=1):    
        afficher(etat, "Coup " + str(i))
    ecrire("Terminé en " + str(len(chemin) - 1) + " coups")
 


x.pack(side="right", fill="both", expand=True)

# /////////////////////////////////////////////////////////////////////////

x3= tk.Frame(fenetre)

def reset():                                       
    console.config(state="normal")                 
    console.delete("1.0", "end")                   
    console.config(state="disabled")              

    tous = []                                      
    for ligne in boutons:                          
        for b in ligne:                            
            if b is not None:                     
                tous.append(b)                     

    for i in range(3):                             
        for j in range(3):                        
            boutons[i][j] = None                   

    for b in tous:                                 
        numero = int(b.cget("text"))               
        for i in range(3):                         
            for j in range(3):
                if shema[i][j] == numero:          
                    b.grid(row=i, column=j)        
                    boutons[i][j] = b   


c= tk.Button(x3, text="RESET", width=25, height=2,command = reset)
c.grid(row=3, column=0, padx=30, pady=5)       
c.configure(bg="green")     
a = tk.Button(x3, text="ALGO A*", width=25, height=2, command=lancer_astar)
a.configure(bg="green")
a.grid(row=3, column=3, padx=30, pady=5) 
x3.configure(bg="#000000") 

x3.pack(side="bottom")

# //////////////////////////////////////////////////////////////////////////////

x2= tk.Frame(fenetre)

boutons = [[None] * 3 for _ in range(3)] 
# trv btn sur grille 
def position(bouton):                
    for i in range(3):                  
        for j in range(3):               
            if boutons[i][j] is bouton:   
                return i, j  

         
# si voisin vide
def case_vide():                          
    for i in range(3):
        for j in range(3):
            if boutons[i][j] is None:     
                return i, j

def cliquer(bouton):                     
    l, c = position(bouton)           
    lv, cv = case_vide()                  
    if abs(l - lv) + abs(c - cv) == 1:    
        bouton.grid(row=lv, column=cv)  
        boutons[lv][cv] = bouton         
        boutons[l][c] = None             

for l in range(3):                       
    for c in range(3):                    
        valeur = shema[l][c]             
        if valeur is None:                
            continue                      
        b = Button(x2, text=str(valeur), width=10, height=5)   
        b.config(command=lambda b=b: cliquer(b))               
        b.grid(row=l, column=c)           
        boutons[l][c] = b    


x2.configure(bg="#000000")
x2.pack(side="left")


fenetre.mainloop()                        