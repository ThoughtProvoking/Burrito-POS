from burrito_bowl import BurritoBowl
from two_burrito import TwoIngredientBurrito
from three_burrito import ThreeIngredientBurrito
from a_la_cart_burrito import ALaCartBurrito
from burritos_and_ingredients import Burritos
from shopping_cart import ShoppingCart


def main():
    products = ShoppingCart()
    want_more_burritos = True

    while want_more_burritos:
        print('Welcome to BurritoMatic! What would you like to order?', end='\n')
        print('{:>50}'.format('Base price:'))
        print('    (1) Burrito-in-a-Bowl                 $3.99', end='\n')
        print('    (2) 2-ingredient Burrito              $4.99', end='\n')
        print('    (3) 3-ingredient Burrito              $5.99', end='\n')
        print('    (4) A-La-Cart Burrito                 $5.99', end='\n')
        print('Please enter the number of the burrito product you would like.', end='\n')
        burrito = input()

        while not burrito.isnumeric() or int(burrito) < 1 or int(burrito) > 4:
            print('Invalid input. Only numbers 1-4:', end=' ')
            burrito = input()

        choose_burrito(products, int(burrito))

        print('Would you like to buy another burrito? y/n:', end=' ')
        buy = input()

        while buy != 'y' and buy != 'n':
            print('Invalid input.', end=' ')
            buy = input('y/n: ')

        if buy == 'n':
            want_more_burritos = False

    products.calculate_total_cost()
    products.print_receipt()
    print('Thank you and have a nice day.', end='\n')


def choose_burrito(shopping_cart, burrito):
    if int(burrito) == Burritos.BURRITO_BOWL.value:
        burrito_bowl = BurritoBowl()
        burrito_bowl.start_order()
        shopping_cart.add_product(burrito_bowl)

    elif int(burrito) == Burritos.TWO_INGREDIENT.value:
        two_ingredient = TwoIngredientBurrito()
        two_ingredient.start_order()
        shopping_cart.add_product(two_ingredient)

    elif int(burrito) == Burritos.THREE_INGREDIENT.value:
        three_ingredient = ThreeIngredientBurrito()
        three_ingredient.start_order()
        shopping_cart.add_product(three_ingredient)

    elif int(burrito) == Burritos.A_LA_CART.value:
        a_la_cart = ALaCartBurrito()
        a_la_cart.start_order()
        shopping_cart.add_product(a_la_cart)

    else:
        print('Code should never go here.')


if __name__ == '__main__':
    main()
