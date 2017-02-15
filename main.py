from core import (show_inventory, rent_item, purchase_item, return_item,
                  update_inventory_add, update_inventory_remove, view_revenue)
import sys
import pickle

data = {'castle_bouncer': [7, 100, 400],
        'sports_bouncer': [4, 100, 400],
        'disney_princess_bouncer': [3, 100, 400],
        '16"_wave_pool_slide': [4, 175, 550],
        'dolphin_slide': [5, 175, 550],
        'giant_slip_and_dip': [2, 175, 500],
        'elephant_bouncer': [6, 225, 625],
        'jurassic_adventure_course': [2, 225, 625],
        'yellow_slide_and_pool_combo': [5, 225, 625]}

print('\n**Welcome to Bounce Into Fun!**\n')


def main():
    """ str -> None
    Contains some of the program's branching # and all the functions parameters
    """
    who = input(
        'Are you administration or customer?\n(Also, you can enter "q" to quit this program)\n').lower(
        ).strip()
    if who == 'administration':
        administration()
    elif who == 'customer':
        customer()
    elif who == 'q':
        quit_program(who)
    else:
        print('This input is invalid! Please try again')
        main()


def administration():
    """ None -> None
    Allows the user to view what is in inventory
    """
    show_inventory()
    view_revenue()


def customer():
    """ None -> None
    Allows the user to complete a transaction in the program
    """
    trans = input(
        'Which transaction would you like to complete? (Enter RENT, PURCHASE, or RETURN)\n').strip(
        ).lower()
    if trans == 'rent':
        rent(trans)
    elif trans == 'purchase':
        purchase(trans)
    elif trans == 'return':
        returns(trans)
    else:
        print(
            "I'm sorry but this transaction can not be completed. Please try again.")
        customer()


def input_one_of(choices):
    """
    Takes in a collection of strings
    Ask user for input, checks if input is in the collection of strings
    if not, prints invalid and restarts.
    """
    while True:
        choice = input(', '.join(choices) + ': ')
        if choice in choices:
            return choice
        else:
            print('Invalid input')


def rent(trans):
    """ str -> str
    Process if user selects customer & rent. Allows the customer to input
    what item they are renting along with quantity and how long they want to
    rent the item out for. Also, restriction for how long they can rent the
    item and how many items that can be rented.
    """
    print('Please select one of the following:')
    with open('inventory.p', 'rb') as fin:
        data = pickle.load(fin)
    for key, value in data.items():
        key = key.replace('_', ' ').title()
        # elephant_bouncer --> Elephant Bouncer
        print('{0} - {1} - ${2}'.format(key, value[0], value[1]))
        # Format of the dict --> Castle Bouncer - 7 - $400
    option_name = input().strip().lower().replace(' ', '_')
    # Castle Bouncer --> castle_bouncer
    if option_name in data:
        max_available = data[option_name][0]
        quantity_options = [str(n) for n in range(1, max_available + 1)]
        print('How many would you like to rent?')
        how_many = int(input_one_of(quantity_options))
        date_options = [str(x) for x in range(1, 5)]
        print('How long are you wanting to rent this item for?')
        how_long = int(input_one_of(date_options))
        print(rent_item(option_name, how_many, how_long) + '\n')
        print(update_inventory_remove(trans, option_name, how_many))
    else:
        print('The item you have entered is not available.')
        rent(trans)
    rerun_program()


def purchase(trans):
    """ str -> str
    Process if user selects customer & purchase. Allows the customer to input
    what item they are purchase along with quantity. Also, restriction for how
    many items can be purchased.
    """
    print('Please select one of the following:')
    with open('inventory.p', 'rb') as fin:
        data = pickle.load(fin)
    for key, value in data.items():
        key = key.replace('_', ' ').title()
        # elephant_bouncer --> Elephant Bouncer
        print('{0} - {1} - ${2}'.format(key, value[0], value[2]))
        # Format of the dict --> Castle Bouncer - 7 - $400
    option_name = input().strip().lower().replace(' ', '_')
    # Castle Bouncer --> castle_bouncer
    if option_name in data:
        max_available = data[option_name][0]
        quantity_options = [str(n) for n in range(1, max_available + 1)]
        print('How many would you like to purchase?')
        how_many = int(input_one_of(quantity_options))
        print(purchase_item(option_name, how_many, how_long) + '\n')
        print(update_inventory_remove(trans, option_name, how_many))
    else:
        print('The item you have entered is not available.')
        purchase(trans)
    rerun_program()


def returns(trans):
    """ str -> str
    Process if user selects customer & return. Allows the customer to input
    what item they are returning along with quantity. Also, this is where
    'replace' (damaged or not) takes place when the item is returned.
    """
    with open('inventory.p', 'rb') as fin:
        data = pickle.load(fin)
    for key, value in data.items():
        key = key.replace('_', ' ').title()
        # elephant_bouncer --> Elephant Bouncer
        print('{0}'.format(key))
        # Format of the dict --> Castle Bouncer
    which_one = input('Which item are you returning?\n').strip().lower(
    ).replace(' ', '_')
    print('Is the item you are returning damaged?')
    condition = input_one_of(['yes', 'no'])
    # Castle Bouncer --> castle_bouncer
    if which_one in data:
        max_available = data[which_one][0]
        quantity_options = [str(n) for n in range(1, max_available + 1)]
        print('How many items are you returning?')
        how_many = int(input_one_of(quantity_options))
        if condition == 'yes':
            print(return_item(which_one, how_many, condition) + '\n')
            print(update_inventory_remove(trans, which_one, how_many))
        else:
            print(return_item(which_one, how_many, condition) + '\n')
            print(update_inventory_add(trans, which_one, how_many))
    rerun_program()


def quit_program(who):
    """ str -> None
    Quits the program entirely
    """
    if who == "q":
        sys.exit(0)


def rerun_program():
    """ None -> str
    Continues the program if user inputs 'C' or quits the program if user
    inputs 'Q'
    """
    choice = input(
        'Would you like to continue the program or exist? (C or Q)\n').strip(
        ).lower()
    if choice == 'c':
        main()
    elif choice == 'q':
        quit_program(choice)
    else:
        print('You must enter C or Q')


if __name__ == '__main__':
    main()
