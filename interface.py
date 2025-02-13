import tkinter as tk
from tkinter import messagebox, filedialog
import json

class Livre:
    def __init__(self, titre, auteur, annee, genre):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion de La Bibliothèque")
        self.geometry("600x400")
        self.configure(bg="beige")  # couleur de fond
        
         # Ajout d'un label pour le titre de l'application
        self.titre_label = tk.Label(self, text="GESTION DE LA BIBLIOTHEQUE", font=("Arial", 16), bg="beige")
        self.titre_label.pack(pady=10)
        
        self.livres = []
        
        self.create_menu()
        self.create_widgets()
        
    def create_menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)
        
        fichier_menu = tk.Menu(menu)
        menu.add_cascade(label="Fichier", menu=fichier_menu)
        fichier_menu.add_command(label="Sauvegarder", command=self.sauvegarder)
        fichier_menu.add_command(label="Charger", command=self.charger)
        fichier_menu.add_separator()
        fichier_menu.add_command(label="Quitter", command=self.quit)
        
    def create_widgets(self):
        self.form_frame = tk.Frame(self)
        self.form_frame.pack(pady=10)
        
        tk.Label(self.form_frame, text="Titre").grid(row=0, column=0)
        self.titre_entry = tk.Entry(self.form_frame)
        self.titre_entry.grid(row=0, column=1)
        
        tk.Label(self.form_frame, text="Auteur").grid(row=1, column=0)
        self.auteur_entry = tk.Entry(self.form_frame)
        self.auteur_entry.grid(row=1, column=1)
        
        tk.Label(self.form_frame, text="Année").grid(row=2, column=0)
        self.annee_entry = tk.Entry(self.form_frame)
        self.annee_entry.grid(row=2, column=1)
        
        tk.Label(self.form_frame, text="Genre").grid(row=3, column=0)
        self.genre_entry = tk.Entry(self.form_frame)
        self.genre_entry.grid(row=3, column=1)
        
        self.ajouter_button = tk.Button(self.form_frame, text="Ajouter Livre", command=self.ajouter_livre)
        self.ajouter_button.grid(row=4, columnspan=2)
        
        self.liste_frame = tk.Frame(self)
        self.liste_frame.pack(pady=10)
        
        self.liste_box = tk.Listbox(self.liste_frame, width=50)
        self.liste_box.pack(side=tk.LEFT)
        
        self.supprimer_button = tk.Button(self.liste_frame, text="Supprimer Livre", command=self.supprimer_livre)
        self.supprimer_button.pack(side=tk.RIGHT)
        
         # Champ de recherche
        tk.Label(self, text="Recherche").pack(pady=5)
        self.recherche_entry = tk.Entry(self)
        self.recherche_entry.pack(pady=5)
    
        self.rechercher_button = tk.Button(self, text="Rechercher", command=self.rechercher_livre)
        self.rechercher_button.pack(pady=5)

    def rechercher_livre(self):
        recherche = self.recherche_entry.get().lower()
        self.liste_box.delete(0, tk.END)  # Effacer la liste actuelle

        livres_trouves = [livre for livre in self.livres if recherche in livre.titre.lower() or recherche in livre.auteur.lower()]

        if not livres_trouves:
           messagebox.showinfo("Information", "Aucun livre trouvé.")
        else:
            for livre in livres_trouves:
                self.liste_box.insert(tk.END, f"{livre.titre} - {livre.auteur} ({livre.annee}) - {livre.genre}")
    
    def ajouter_livre(self):
        titre = self.titre_entry.get()
        auteur = self.auteur_entry.get()
        annee = self.annee_entry.get()
        genre = self.genre_entry.get()
        
        if not titre or not auteur or not annee or not genre:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return
        
        try:
            annee = int(annee)
        except ValueError:
            messagebox.showerror("Erreur", "L'année doit être un nombre.")
            return
        
        livre = Livre(titre, auteur, annee, genre)
        self.livres.append(livre)
        self.liste_box.insert(tk.END, f"{livre.titre} - {livre.auteur} ({livre.annee}) - {livre.genre}")
        
        self.titre_entry.delete(0, tk.END)
        self.auteur_entry.delete(0, tk.END)
        self.annee_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        
    def supprimer_livre(self):
        try:
            index = self.liste_box.curselection()[0]
            del self.livres[index]
            self.liste_box.delete(index)
        except IndexError:
            messagebox.showerror("Erreur", "Veuillez sélectionner un livre à supprimer.")
        
    def sauvegarder(self):
        fichier = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Fichiers JSON", "*.json")])
        if fichier:
            with open(fichier, 'w') as f:
                json.dump([livre.__dict__ for livre in self.livres], f)
                
    def charger(self):
        fichier = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
        if fichier:
            with open(fichier, 'r') as f:
                self.livres = [Livre(**data) for data in json.load(f)]
                self.liste_box.delete(0, tk.END)
                for livre in self.livres:
                    self.liste_box.insert(tk.END, f"{livre.titre} - {livre.auteur} ({livre.annee}) - {livre.genre}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
