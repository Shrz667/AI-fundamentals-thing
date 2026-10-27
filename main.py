from tkinter import Tk, Label, Button,scrolledtext
import tkinter as tk

fenetre = Tk()
fenetre.title("je suis la") 
fenetre.geometry("800x450")
fenetre.configure(bg="#34495e")
shema=[
    [1, 2, 3],
    [8, None, 4],
    [7, 6, 5],
]

x= tk.Frame(fenetre)
# x.pack(side="right")

                                          

console = scrolledtext(x, width=40, height=20,       
                       bg="black", fg="green",        
                       insertbackground="lime",      
                       font=("Consolas", 11),        
                       state="disabled")             
console.pack(fill="both", expand=True)   

x.pack(side="right", fill="both", expand=True, padx=10, pady=10)





x3= tk.Frame(fenetre)

c= tk.Button(x3, text="RESET", width=25, height=2)
c.grid(row=3, column=0, padx=30, pady=5)            
a = tk.Button(x3, text="ALGO A*", width=25, height=2)
a.grid(row=3, column=3, padx=30, pady=5) 
x3.configure(bg="#34495e") 

x3.pack(side="bottom")



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


x2.configure(bg="#34495e")
x2.pack(side="left")


fenetre.mainloop()                        