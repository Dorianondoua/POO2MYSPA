class Bibliothèque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, livre):
        self.livres.remove(livre)

    def rechercher_livre(self, mot_cle):
        return [livre for livre in self.livres if mot_cle.lower() in livre.titre.lower() or mot_cle.lower() in livre.auteur.lower()]

    def trier_livres(self, critere='titre'):
        if critere == 'titre':
            self.livres.sort(key=lambda livre: livre.titre)
        elif critere == 'auteur':
            self.livres.sort(key=lambda livre: livre.auteur)
        elif critere == 'annee':
            self.livres.sort(key=lambda livre: livre.annee)
        elif critere == 'genre':
            self.livres.sort(key=lambda livre: livre.genre)

    def lister_livres(self):
        return self.livres
