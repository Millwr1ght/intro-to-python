"""
W09/10 Prove : Shopping Cart
a program that stores a list of products in a shopping cart along with their prices.
The user has the ability to add items to the list, remove them, and see the total price of the cart

"""
from collections import deque


class Cart:
    """ the shopping cart class
    variables: 
     -  list of items in cart: {'item': 'price'} 
     -  total price of items: int 
    methods: 
     -  prompt for/add new item, 
     -  display contents of cart,
     -  display total price,
     -  remove an item
    """

    def __init__(self):
        """ set up instance and variables """
        self.contents = deque()
        self.prices = deque()
        self.total_price = 0.00

    def add(self):
        """ prompt for and add an item to the Cart """
        new_item = input('\nWhat item would you like to add to your cart? ')

        new_item_price = input('How much does it cost? ')
        self.contents.append(new_item)
        self.prices.append(new_item_price)
        self.total_price += new_item_price
        print(f'"{new_item}" worth ${new_item_price:.2f} was added to your cart!')

    def remove(self):
        """ prompt for and remove an item from the Cart """
        if self.not_empty():
            item = input('Which item would you like to remove? ')
            try: # is input integer?
                item = int(item)
                if item - 1 >= 0 and item - 1 < len(self.contents):
                    self.total_price -= self.prices[item - 1]
                    del self.contents[item - 1]
                    del self.prices[item - 1]
                    print(f'\nItem #{item} was removed.')
                else:
                    print(f'\nItem #{item} was not found in your cart.')
            except: # input is string
                if item in self.contents:
                    index = self.contents.index(item)
                    self.total_price -= self.prices[index]
                    self.contents.remove(item)
                    del self.prices[index]
                    print(f'\n"{item}" was removed.')
                else:
                    print(f'\n"{item}" was not found in your cart.')

    def display(self):
        """ display all of the contents of the cart """
        if self.not_empty():
            print('\nHere\'s what is in your cart so far:')
            i = 0
            for item, price in zip(self.contents, self.prices):
                i += 1
                print(f'{i:2}. {item} - ${price:.2f}')

    def total(self):
        """ total the cart price and output it """
        print(f'\nYour current total is ${self.total_price:.2f}.')

    def not_empty(self):
        """ check if the cart is empty or not, if empty, suggest filling it """
        if len(self.contents) > 0:
            return True
        else:
            print('Your cart is empty, let\'s fix that!')


def main():
    """ the main menu for the shopping cart program """
    choice = ''
    user_cart = Cart()
    print('Welcome to Aperture Shopping Centre!')
    while choice.lower() != 'quit' and choice.lower() != '5':
        print('\n1. Add to cart\n2. Remove item\n3. View cart\n4. Subtotal\n5. Quit')
        choice = input('Please select an action: ')
        if choice.lower() == 'add' or choice.lower() == 'add to cart' or choice.lower() == '1':
            user_cart.add()
        elif choice.lower() == 'remove' or choice.lower() == 'remove item' or choice.lower() == '2':
            user_cart.remove()
        elif choice.lower() == 'view' or choice.lower() == 'view cart' or choice.lower() == '3':
            user_cart.display()
        elif choice.lower() == 'subtotal' or choice.lower() == 'total' or choice.lower() == '4':
            user_cart.total()
    print('Thank you for shopping with us!')


if __name__ == '__main__':
    main()
