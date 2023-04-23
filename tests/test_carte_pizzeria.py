import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from unittest.mock import Mock
from carte_pizzeria import CartePizzeria, CartePizzeriaException

def test_is_empty():
    carte = CartePizzeria()
    assert carte.is_empty()

def test_nb_pizzas():
    carte = CartePizzeria()
    pizza = Mock()
    carte.add_pizza(pizza)
    assert carte.nb_pizzas() == 1

def test_add_pizza():
    carte = CartePizzeria()
    pizza = Mock()
    carte.add_pizza(pizza)
    assert not carte.is_empty()
    assert carte.nb_pizzas() == 1

def test_remove_pizza():
    carte = CartePizzeria()
    pizza = Mock()
    pizza.name = "Margherita"
    carte.add_pizza(pizza)
    carte.remove_pizza("Margherita")
    assert carte.is_empty()

def test_remove_pizza_not_found():
    carte = CartePizzeria()
    pizza = Mock()
    pizza.name = "Margherita"
    carte.add_pizza(pizza)
    with pytest.raises(CartePizzeriaException):
        carte.remove_pizza("Quattro Formaggi")