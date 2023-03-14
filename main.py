from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from models import Pizza
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty

class PizzaWidget(BoxLayout):
    nom = StringProperty() #permet de pouvoir passer le nom au PizzaWidget
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()

class MainWidget(BoxLayout):
    recycleView = ObjectProperty(None) # On crée cette ObjectProperty afin de pouvoir utiliser le recycleView (initialiser à none)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza("4 fromages", "Sauce tomate, Mozzarella, Gorgonzola, Parmigiano Reggiano, Provolone, Origan", 13.50, True),
            Pizza("Vegetarienne", "Sauce tomate, Mozzarella, Aubergine, Poivrons, Artichaut, Courgette, Champignons, Olives", 12.50, True),
            Pizza("Salami", "Sauce tomate, Mozzarella, Salami, Parmigiano Reggiano", 14.00, False),
            Pizza("Tonno", "Sauce tomate, Mozzarella, Tonno, Oignons, Olives", 14.00, True)
        ]

    def on_parent(self, widget, parent): #on_parent on affiche les datas quand le widget a été rajouté au layout parent (si il n'est pas chargé, cela ne fonctionnera pas. C'est pour cela qu'on utilise on_parent)
        # self.recycleView.data = [
        #     {"nom": "4 fromages",
        #      "ingredients": "Champignons"},
        #     {"nom": "Salami",
        #      "ingredients": "Champignons"}
        # ] # nous permet d'envoyer les datas au recycleView
        self.recycleView.data = [pizza.get_dictionnary() for pizza in self.pizzas]
        
class PizzaApp(App):
    pass


PizzaApp().run()