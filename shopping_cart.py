shopping_cart = ['apple', 'banana', 'cherry', 'kiwi']

def disaply_shopping_cart():
    for index, fruit in enumerate(shopping_cart):
        print(f'Index {index}: {fruit}')

disaply_shopping_cart()

def add_to_cart(item):
    shopping_cart.append(item)
    print(f'{item} has been added to the shopping cart')

add_to_cart('grapes')
disaply_shopping_cart()

def remove_from_cart(index):
    if 0 <= index < len(shopping_cart):
        remove_item = shopping_cart.pop(index)
        print(f'Removed {remove_item} from the shopping cart')
    else:
        print('Invalid index, Item not removed')

remove_from_cart(1)
disaply_shopping_cart()

def delete_shopping_cart():
    shopping_cart.clear()
    print('Shopping cart has been deleted.')

delete_shopping_cart()
disaply_shopping_cart()