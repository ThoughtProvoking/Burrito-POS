from burritos_and_ingredients import all_ingredients
from two_burrito import TwoIngredientBurrito


class ThreeIngredientBurrito(TwoIngredientBurrito):
    
    def __init__(self):
        super().__init__('Three Ingredient Burrito', 5.99)


    def start_order(self):
        for category, ingredient_list in all_ingredients.items():
            # allow toppings
            super().add_ingredients(category, ingredient_list)


    def calculate_total(self):
        return super().calculate_total()


    def print_receipt(self):
        super().print_receipt()
