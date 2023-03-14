
class Pizza:
    nom = ""
    ingredients = ""
    prix = 0.0
    vegetarienne = False
    
    def __init__(self, nom, ingredients, prix, vegetarienne): #on a pas besoin de mettre ** car la class pizza n'hérite pas des éléments de Kivy. C'est juste une class qui nous permet de gérer nos données. On appelle pas non plus super car cette class n'hérite de personne.
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix
        self.vegetarienne = vegetarienne