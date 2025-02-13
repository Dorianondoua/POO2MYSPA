from document import Document
class Livre(Document):
   def __init__(self, titre, auteur, annee, genre):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre


   def __str__(self):
        return f"{self.titre} par {self.auteur} ({self.annee})"