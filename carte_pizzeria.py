class CartePizzeriaException(Exception):
    pass

class CartePizzeria:
    def __init__(self):
        self.pizzas = []

    def is_empty(self):
        return len(self.pizzas) == 0

    def nb_pizzas(self):
        return len(self.pizzas)

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        pizza_found = None
        for pizza in self.pizzas:
            if pizza.name == name:
                pizza_found = pizza
                break

        if not pizza_found:
            raise CartePizzeriaException(f"Pizza '{name}' non trouvée.")
        else:
            self.pizzas.remove(pizza_found)