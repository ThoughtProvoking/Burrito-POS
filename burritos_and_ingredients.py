from enum import Enum


class Burritos(Enum):
    BURRITO_BOWL = 1
    TWO_INGREDIENT = 2
    THREE_INGREDIENT = 3
    A_LA_CART = 4

all_ingredients = {
    'base': {
        'tortilla': 0.00,
        'rice': 0.00
    },
    'meat': {
        'chicken': 0.50,
        'steak': 0.50
    },
    'salsa': {
        'red salsa': 0.50,
        'green salsa': 0.50,
        'queso': 1.50
    },
    'toppings': {
        'grated cheese': 0.33,
        'sour cream': 0.33,
        'guac': 1.25
    },
    'misc': {
        'soft drink': 1.25,
        'brownie': 1.50,
        'chips': 2.00
    }
}

ingredients_with_fee = [
    'queso',
    'guac'
]
