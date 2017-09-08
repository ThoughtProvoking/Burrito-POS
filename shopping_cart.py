class ShoppingCart:

    def __init__(self):
        self._shopping_cart = []
        self._total_cost = 0.0


    def calculate_total_cost(self):
        for item in self._shopping_cart:
            self._total_cost += item.calculate_total()


    def print_receipt(self):
        print('Here is your receipt:', end='\n')
        for item in self._shopping_cart:
            item.print_receipt()

        print(f'Total:                   ${self._total_cost:3.2f}')


    def add_product(self, product):
        self._shopping_cart.append(product)
