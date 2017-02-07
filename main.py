def show_inventory():
    """ list of strings -> str
    Allows the user to view what inventory is in stock.
    """
    with open('inventory.txt', 'r') as file:
        new_list = file.read().splitlines()
        # ['Houses - Castle Bouncer (7) - Sports Bouncer (4) - Disney Princess Bouncer (3)']

        list_info = list(map(lambda s: s.split(' - '), new_list))
        # get info in usable format
    return list_info


def rent_item(trans):
    """ str, int -> str
    Display the items available to rent from. Allows the customer to select the
    item of their choice and the quantity of that item.
    """
    rental_fees = {'castle_bouncer': 100,
                   'sports_bouncer': 100,
                   'disney_princess_bouncer': 100,
                   '16"_wave_pool_slide': 175,
                   'dolphin_slide': 175,
                   'giant_slip_and_dip': 175,
                   'elephant_bouncer': 225,
                   'jurassic_adventure_course': 225,
                   'yellow_slide_and_pool_combo': 225}
    purchase_fees = {'castle_bouncer': 400,
                     'sports_bouncer': 400,
                     'disney_princess_bouncer': 400,
                     '16"_wave_pool_slide': 550,
                     'dolphin_slide': 550,
                     'giant_slip_and_dip': 550,
                     'elephant_bouncer': 625,
                     'jurassic_adventure_course': 625,
                     'yellow_slide_and_pool_combo': 625}
    tax = 1.07
    if trans == 'rent':
        print('Please select one of the following:')
        for key, value in rental_fees.items():
            key = key.replace('_', ' ').title()
            print('{0} - ${1}'.format(key, value))
        options = input().strip().lower().replace(' ', '_')
        how_many = int(input('Quantity:').strip())
        how_long = int(input(
            'How long are you wanting to rent this item for?').strip())
        total = (rental_fees[options] * how_long + purchase_fees[options] / 10
                 ) * how_many * tax
        receipt = (
            '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
            '\n' + str(how_many) + '\t' + options + '\n'
            'Rent -- ' + str(how_long) + '\n'
            '\t\tTotal: ${0:.2f}'.format(total))
        return receipt


def purchase_item(trans):
    """ str, int -> float
    Display the items available to purchase from. Allows the customer to select
    the item of their choice and the quantity of that item.
    """
    rental_fees = {'castle_bouncer': 100,
                   'sports_bouncer': 100,
                   'disney_princess_bouncer': 100,
                   '16"_wave_pool_slide': 175,
                   'dolphin_slide': 175,
                   'giant_slip_and_dip': 175,
                   'elephant_bouncer': 225,
                   'jurassic_adventure_course': 225,
                   'yellow_slide_and_pool_combo': 225}
    purchase_fees = {'castle_bouncer': 400,
                     'sports_bouncer': 400,
                     'disney_princess_bouncer': 400,
                     '16"_wave_pool_slide': 550,
                     'dolphin_slide': 550,
                     'giant_slip_and_dip': 550,
                     'elephant_bouncer': 625,
                     'jurassic_adventure_course': 625,
                     'yellow_slide_and_pool_combo': 625}
    tax = 1.07
    if trans == 'purchase':
        print('Please select one of the following:')
        for key, value in purchase_fees.items():
            key = key.replace('_', ' ').title()
            print('{0} - ${1}'.format(key, value))
        options = input().strip().lower().replace(' ', '_')
        how_many = int(input('Quantity:').strip())
        total = purchase_fees[options] * how_many * tax
        receipt = (
            '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
            '\n' + str(how_many) + '\t' + options + '\n'
            'Purchased -- ' + str(how_many) + '\n'
            '\t\tTotal: ${0:.2f}'.format(total))
        return receipt

#
# def return_item():
#     """ str, int -> None
#     Allows the customer to return the item(s) they rented.
#     """
#
#
# def replace_item():
#     """ str, int -> None
#     User inputs whether it's damaged or not. After, the item is replaced, it
#     will calculate the total amount owed and prints it out to the customer.
#     """
#
#
# def total_sales_cost():
#     """ str -> float
#     Returns the price (including the tax, 7%) calculated of the items selected.
#     """
#
# def update_inventory():
#     """ str -> None
#     Update the file every time a new transaction is processed and will write it to a .csv file.
#     """

if __name__ == '__main__':
    print('Welcome to Bounce Into Fun!')
    who = input('Are you administration or customer?').lower().strip()
    if who == 'administration':
        print(show_inventory())
    else:
        trans = input(
            'Which transaction would you like to complete? (Enter RENT, RETURN, PURCHASE, or REPLACE)\n').strip(
            ).lower()
        print(rent_item(trans))
        print(purchase_item(trans))
