import pickle
# {Name of item: [how many is in stock, price for rent per day, full price]}
rental_fees = {'castle_bouncer': [7, 100, 400],
               'sports_bouncer': [4, 100, 400],
               'disney_princess_bouncer': [3, 100, 400],
               '16"_wave_pool_slide': [4, 175, 550],
               'dolphin_slide': [5, 175, 550],
               'giant_slip_and_dip': [2, 175, 500],
               'elephant_bouncer': [6, 225, 625],
               'jurassic_adventure_course': [2, 225, 625],
               'yellow_slide_and_pool_combo': [5, 225, 625]}

# made my dict a global dictionary so it didn't have to live in each function..
# (no repeating in each function)


def init_inventory():
    with open('inventory.p', 'wb') as fin:
        pickle.dump(rental_fees, fin)


def rent_item(options, how_many, how_long):
    """ None -> str
    Display the items available to rent from. Allows the customer to select the
    item of their choice and the quantity of that item and return the price.
    """
    tax = 1.07
    total = (rental_fees[options][1] * how_long + rental_fees[options][2] / 10
             ) * how_many * tax
    # total = (100 * 4 (days) + 400 / 10) * 2 * 1.07
    receipt = (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + str(how_many) + '\t' + options + '\n'
        'Rented -- ' + str(how_long) + 'days' + '\n'
        '\t\tTotal: ${0:.2f}'.format(total))
    return receipt


def purchase_item(options, how_many):
    """ None -> str
    Display the items available to purchase from. Allows the customer to select
    the item of their choice and the quantity of that item.
    """
    tax = 1.07
    total = rental_fees[options][2] * how_many * tax
    # total = 400 * 2 * 1.07
    receipt = (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + str(how_many) + '\t' + options + '\n'
        'Purchased -- ' + str(how_many) + '\n'
        '\t\tTotal: ${0:.2f}'.format(total))
    return receipt


def return_item(which_one, how_many, condition):
    """ None -> str
    Allows the customer to return the item(s) they rented with the receipt of
    the replacement value (10%) they paid to rent the item.
    """
    tax = 1.07
    if condition == 'y':
        total = rental_fees[which_one][2] * how_many * tax
        # total = 400 * 2 * 1.07
        receipt = (
            '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
            '\n' + str(how_many) + '\t' + which_one + '\n'
            'Returned Damaged -- ' + str(how_many) + '\n'
            '\t\tTotal: ${0:.2f}'.format(total))
        return receipt
    else:
        total = rental_fees[which_one][2] / 10
        # total = 400 / 10
        receipt = (
            '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
            '\n' + str(how_many) + '\t' + which_one + '\n'
            'Returned -- ' + str(how_many) + '\n'
            '\t\tRefund Total: ${0:.2f}'.format(total))
        return receipt


def update_inventory_remove(options, how_many):
    """ str -> None
    Update the file every time a new transaction is processed and will write it
    to a .p (pickle) file.
    """
    with open('inventory.p', 'rb') as fin:
        data = pickle.load(fin)
        update = int(data[options][0]) - how_many
    with open('inventory.p', 'wb') as fin:
        pickle.dump(update, fin)
    print(show_inventory())


def update_inventory_add(options, how_many):
    """
    """
    with open('inventory.p', 'rb') as fin:
        data = pickle.load(fin)
        update = int(data[options][0]) + how_many
    with open('inventory.p', 'wb') as fin:
        pickle.dump(update, fin)
    print(show_inventory())


def show_inventory():
    """ None -> list
    Allows the user to view what inventory is in stock.
    """
    with open('inventory.p', 'rb') as fin:
        data = pickle.load(fin)
        # {'jurassic_adventure_course': [2, 225, 625],
        #  'sports_bouncer': [4, 100, 400],
        #  '16"_wave_pool_slide': [4, 175, 550],
        #  'giant_slip_and_dip': [2, 175, 500],
        #  'castle_bouncer': [7, 100, 400],
        #  'disney_princess_bouncer': [3, 100, 400],
        #  'yellow_slide_and_pool_combo': [5, 225, 625],
        #  'dolphin_slide': [5, 175, 550],
        #  'elephant_bouncer': [6, 225, 625]}
        return data
