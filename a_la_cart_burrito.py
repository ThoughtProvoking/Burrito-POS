from burritos_and_ingredients import all_ingredients
from burrito_bowl import BurritoBowl

from operator import itemgetter


class ALaCartBurrito(BurritoBowl):
    
    def __init__(self):
        super().__init__('A La Cart Burrito', 5.99)


    def start_order(self):
        for category, ingredient_list in all_ingredients.items():
            # allow toppings
            for ingredient, price in ingredient_list.items():
                # allow free extra tortilla
                print(f'Add {ingredient}? y/n:')
                add = input()

                while add != 'y' and add != 'n':
                    print('Invalid input.', end=' ')
                    add = input('y/n: ')

                if add == 'y':
                    if category != 'misc':
                        self._ingredients[ingredient] = price
                        self._ask_for_extra(ingredient, price)

                    else:
                        super()._ask_for_extra(ingredient, price, True)


    def calculate_total(self):
        return super().calculate_total(True)


    def print_receipt(self):
        ingredients_sorted = sorted([(item, price) for item, price in self._ingredients.items()], key=itemgetter(1))
        print(f'{self._name:25} ${self._base_price}')

        for ingredient, price in ingredients_sorted[:-3]:
            # print the prices of charged ingredients
            print(f'  {ingredient:23} ${price:.2f}')

        for ingredient, price in ingredients_sorted[-3:]:
            print(f'  {ingredient}')

        for item, price in self._other.items():
            print(f'{item:25} ${price:2.2f}')
