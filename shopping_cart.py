"""
W09/10 Prove : Shopping Cart
a program that stores a list of products in a shopping cart along with their prices.
The user has the ability to add items to the list, remove them, and see the total price of the cart

"""


class Item:
    """ the Item class 
    variables:
     -  name: str
     -  price: float
     -  quantity: int
    methods:
     - prompt for name, price: void
     - get price: float
    """

    def __init__(self, item_name: str = 'Unnamed', item_price: float = float(0), item_quantity: int = int(1)):
        """ initialize setup """
        self.name = item_name
        self.price = item_price
        self.quantity = item_quantity

    def prompt(self):
        """ get name, price, and quantity input from user """
        self.name = input('\nWhat item would you like to add to your cart? ')
        self.price = float(input('How much does it cost? '))
        self.quantity = int(
            input(f'How many "{self.name}"s will you be purchasing? '))

    def total_price(self):
        """ return total price of Item, i.e. quantity * price """
        return self.price * self.quantity


class Cart:
    """ the shopping cart class
    variables: 
     -  list of Items in cart: []
     -  total price of items: int 
    methods: 
     -  add new Item: void
     -  display items in cart: str
     -  display total price: str
     -  remove an item: void
    """

    def __init__(self):
        """ set up instance and variables """
        self.items = []

    def add_item(self):
        """ prompt for and add an item to the Cart """
        new_item = Item()
        new_item.prompt()
        self.items.append(new_item)

        print(
            f'"{new_item.name}" x({new_item.quantity}) worth ${new_item.price:.2f} each was added to the cart!')

    def remove_item(self):
        """ prompt for and remove an item from the Cart """
        if self.not_empty():
            item = input('Which item would you like to remove? ')

            try:  # is input integer?
                item = int(item)
                if item - 1 >= 0 and item - 1 < len(self.items):
                    del self.items[item - 1]
                    print(f'\nItem #{item} was removed.')
                else:
                    print(f'\nItem #{item} was not found in your cart.')

            except:  # input is string
                found = False
                i = 0
                for product in self.items:
                    if item == product.name and not found:
                        self.items.remove(product)
                        print(f'\n"{item}" was removed.')
                        found = True
                    i += 1
                if not found:
                    print(f'\n"{item}" was not found in your cart.')

    def get_total(self):
        """ get the total price of all Items in Cart """
        total = 0
        for item in self.items:
            total += item.total_price()

        return total

    def display_items(self):
        """ display all of the items in the cart """
        if self.not_empty():
            print('\nHere\'s what is in your cart so far:')
            i = 0
            for item in self.items:
                i += 1
                print(
                    f'{i:2}. {item.name} ({item.quantity}) - ${item.total_price():.2f}')

    def display_total(self):
        """ total the cart price and output it """

        print(f'\nYour current total is ${self.get_total():.2f}.')

    def not_empty(self):
        """ check if the cart is empty or not, if empty, suggest filling it """
        if len(self.items) > 0:
            return True
        else:
            print('Your cart is empty, let\'s fix that!')


def main():
    """ the main menu for the shopping cart program """
    choice = ''
    user_cart = Cart()
    print('Welcome to Aperture Shopping Centre!')

    # menu loop
    while choice.lower() != 'quit' and choice.lower() != '5':
        print('\n1. Add to cart\n2. Remove item\n3. View cart\n4. Subtotal\n5. Quit')
        choice = input('Please select an action: ')

        # choice 1: Add an Item
        if choice.lower() == 'add' or choice.lower() == 'add to cart' or choice.lower() == '1':
            user_cart.add_item()

        # choice 2: Remove an Item
        elif choice.lower() == 'remove' or choice.lower() == 'remove item' or choice.lower() == '2':
            user_cart.remove_item()

        # choice 3: View cart/Display items in cart
        elif choice.lower() == 'view' or choice.lower() == 'view cart' or choice.lower() == '3':
            user_cart.display_items()

        # choice 4: View total price of items in cart
        elif choice.lower() == 'subtotal' or choice.lower() == 'total' or choice.lower() == '4':
            user_cart.display_total()

        # choice Invalid: not 1-5, try again
        elif choice.lower() != 'quit' and choice.lower() != '5':
            print('\nPlease make a valid selection.')

    print('Thank you for shopping with us!')


# begin!
if __name__ == '__main__':
    main()
