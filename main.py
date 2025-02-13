from abc import ABC, abstractmethod

# Classe abstraite Document
class Document(ABC):
    @abstractmethod
    def __str__(self):
        pass

# Classe Livre héritant de Document
class Livre(Document):
    def __init__(self, titre, auteur, annee, genre):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre

    def __str__(self):
        return f"{self.titre} par {self.auteur} ({self.annee})"

# Classe Bibliothèque pour gérer la collection de livres
class Bibliothèque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        """Ajoute un livre à la collection."""
        self.livres.append(livre)

    def supprimer_livre(self, livre):
        """Supprime un livre de la collection."""
        if livre in self.livres:
            self.livres.remove(livre)

    def rechercher_livre(self, mot_cle):
        """Recherche des livres par mot-clé dans le titre ou l'auteur."""
        return [livre for livre in self.livres if mot_cle.lower() in livre.titre.lower() or mot_cle.lower() in livre.auteur.lower()]

    def lister_livres(self):
        """Retourne la liste des livres dans la collection."""
        return self.livres
