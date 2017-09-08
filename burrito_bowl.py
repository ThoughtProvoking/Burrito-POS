from burritos_and_ingredients import all_ingredients, ingredients_with_fee

from operator import itemgetter


class BurritoBowl:
    
    def __init__(self, name='Burrito in a Bowl', base_price=3.99):
        self._name = name
        self._base_price = base_price
        self._total_price = base_price
        self._ingredients = {}
        self._other = {}


    def start_order(self):
        for category, ingredient_list in all_ingredients.items():
            if category == 'toppings': # no toppings
                continue

            for ingredient, price in ingredient_list.items():
                if ingredient == 'tortilla': # no tortilla
                    continue

                print(f'Add {ingredient}? y/n:')
                add = input()

                while add != 'y' and add != 'n':
                    print('Invalid input.', end=' ')
                    add = input('y/n: ')

                if add == 'y':
                    if category != 'misc':
                        self._ingredients[ingredient] = price
                        break # break inner for loop

                    else:
                        self._ask_for_extra(ingredient, price, True)


    def calculate_total(self, is_a_la_cart=False):
        if is_a_la_cart:
            ingredients_sorted = sorted([(item, price) for item, price in self._ingredients.items()], key=itemgetter(1))
            for ingredient, price in ingredients_sorted[:-3]:
                # charge for all ingredients except most expensive three
                self._total_price += price

        else:
            for ingredient, price in self._ingredients.items():
                if ingredient in ingredients_with_fee:
                    self._total_price += price

        for item, price in self._other.items():
            self._total_price += price

        return self._total_price


    def print_receipt(self):
        print(f'{self._name:25} ${self._base_price}')
        for ingredient, price in self._ingredients.items():
            if ingredient in ingredients_with_fee:
                print(f'  {ingredient:23} ${price:.2f}')

            else:
                print(f'  {ingredient}')

        for item, price in self._other.items():
            print(f'{item:25} ${price:2.2f}')


    def _ask_for_extra(self, item, price, is_misc=False):
        
        if not is_misc: # item is a burrito ingredient
            print(f'Would you like extra {item}? y/n:', end=' ')
            extra = input()

            while extra != 'y' and extra != 'n':
                print('Invalid input.', end=' ')
                extra = input('y/n: ')

            if extra == 'y':
                self._ingredients[f'extra {item}'] = price

        else: # item is NOT a burrito ingredient
            print(f'How many {item} do you want?', end=' ')
            servings = input()

            while not servings.isnumeric():
                print('Invalid input. Numbers only:', end=' ')
                servings = input()

            self._other[f'{item} x{int(servings)}'] = int(servings) * price
