from burritos_and_ingredients import all_ingredients
from burrito_bowl import BurritoBowl


class TwoIngredientBurrito(BurritoBowl):
    
    def __init__(self, name='Two Ingredient Burrito', base_price=4.99):
        super().__init__(name, base_price)


    def start_order(self):
        for category, ingredient_list in all_ingredients.items():
            if category == 'toppings': # no toppings
                continue

            self.add_ingredients(category, ingredient_list)


    def add_ingredients(self, category, ingredient_list):
        for ingredient, price in ingredient_list.items():
            # allow tortilla
            print(f'Add {ingredient}? y/n:')
            add = input()

            while add != 'y' and add != 'n':
                print('Invalid input.', end=' ')
                add = input('y/n: ')

            if add == 'y':
                if category != 'misc':
                    if category == 'base':
                        self._ingredients[ingredient] = price
                        # allow tortilla and rice

                    else:
                        self._ingredients[ingredient] = price
                        break # break inner for loop

                else:
                    super()._ask_for_extra(ingredient, price, True)


    def calculate_total(self):
        return super().calculate_total()


    def print_receipt(self):
        super().print_receipt()
