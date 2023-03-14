from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from models import Pizza

class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza("4 fromages", "Sauce tomate, Mozzarella, Gorgonzola, Parmigiano Reggiano, Provolone, Origan", 13.50, True),
            Pizza("Vegetarienne", "Sauce tomate, Mozzarella, Aubergine, Poivrons, Artichaut, Courgette, Olives", 12.50, True),
            Pizza("Salami", "Sauce tomate, Mozzarella, Salami, Parmigiano Reggiano", 14.00, False),
            Pizza("Tonno", "Sauce tomate, Mozzarella, Tonno, Oignons, Olives", 14.00, True)
        ]

class PizzaApp(App):
    pass


PizzaApp().run()