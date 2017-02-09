import csv

rental_fees = {'castle_bouncer': [7, 100],
               'sports_bouncer': [4, 100],
               'disney_princess_bouncer': [3, 100],
               '16"_wave_pool_slide': [4, 175],
               'dolphin_slide': [5, 175],
               'giant_slip_and_dip': [2, 175],
               'elephant_bouncer': [6, 225],
               'jurassic_adventure_course': [2, 225],
               'yellow_slide_and_pool_combo': [5, 225]}
# purchase_fees = {'castle_bouncer': 400,
#                  'sports_bouncer': 400,
#                  'disney_princess_bouncer': 400,
#                  '16"_wave_pool_slide': 550,
#                  'dolphin_slide': 550,
#                  'giant_slip_and_dip': 550,
#                  'elephant_bouncer': 625,
#                  'jurassic_adventure_course': 625,
#                  'yellow_slide_and_pool_combo': 625}
purchase_fees = {'castle_bouncer': [7, 400],
                 'sports_bouncer': [4, 400],
                 'disney_princess_bouncer': [3, 400],
                 '16"_wave_pool_slide': [4, 550],
                 'dolphin_slide': [5, 550],
                 'giant_slip_and_dip': [2, 550],
                 'elephant_bouncer': [6, 625],
                 'jurassic_adventure_course': [2, 625],
                 'yellow_slide_and_pool_combo': [5, 625]}


def main():
    """ str -> None
    """
    print('Welcome to Bounce Into Fun!')
    who = input('Are you administration or customer?').lower().strip()
    if who == 'administration':
        return show_inventory()
    elif who == 'customer':
        trans = input(
            'Which transaction would you like to complete? (Enter RENT, PURCHASE, or RETURN)\n').strip(
            ).lower()
        if trans == 'rent':
            print('Please select one of the following:')
            for key, value in rental_fees.items():
                key = key.replace('_', ' ').title()
                print('{0} - {1} - ${2}'.format(key, value[0], value[1]))
            options = input().strip().lower().replace(' ', '_')
            how_many = int(input('Quantity:').strip())
            how_long = int(input(
                'How long are you wanting to rent this item for?').strip())
            return rent_item(options, how_many, how_long)
        elif trans == 'purchase':
            print('Please select one of the following:')
            for key, value in purchase_fees.items():
                key = key.replace('_', ' ').title()
                print('{0} - {1} - ${2}'.format(key, value[0], value[1]))
            options = input().strip().lower().replace(' ', '_')
            how_many = int(input('Quantity:').strip())
            return purchase_item(options, how_many)
        elif trans == 'return':
            for key, value in purchase_fees.items():
                key = key.replace('_', ' ').title()
                print('{0}'.format(key))
            which_one = input('Which item are you returning?\n').strip().lower(
            ).replace(' ', '_')
            how_many = int(input('Quantity:').strip())
            condition = input(
                'Is the item you are returning damaged? (y/n)\n').strip(
                ).lower()
            return return_item(which_one, how_many, condition)
        else:
            return "I'm sorry but this transaction can not be completed. Please try again."
    else:
        return 'This input is invalid!'


def show_inventory():
    """ None -> list
    Allows the user to view what inventory is in stock.
    """
    with open('inventory.csv') as file:
        new_list = csv.reader(file)
        # get info in usable format
        list_info = list(new_list)
        return list_info


def rent_item(options, how_many, how_long):
    """ None -> str
    Display the items available to rent from. Allows the customer to select the
    item of their choice and the quantity of that item and return the price.
    """
    tax = 1.07
    total = (
        rental_fees[options][1] * how_long + purchase_fees[options][1] / 10
    ) * how_many * tax
    receipt = (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + str(how_many) + '\t' + options + '\n'
        'Rented -- ' + str(how_long) + '\n'
        '\t\tTotal: ${0:.2f}'.format(total))
    return receipt


def purchase_item(options, how_many):
    """ None -> str
    Display the items available to purchase from. Allows the customer to select
    the item of their choice and the quantity of that item.
    """
    tax = 1.07
    total = purchase_fees[options][1] * how_many * tax
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
        total = purchase_fees[which_one][1] * how_many * tax
        receipt = (
            '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
            '\n' + str(how_many) + '\t' + which_one + '\n'
            'Returned Damaged -- ' + str(how_many) + '\n'
            '\t\tTotal: ${0:.2f}'.format(total))
        return receipt
    else:
        total = purchase_fees[which_one][1] / 10
        receipt = (
            '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
            '\n' + str(how_many) + '\t' + which_one + '\n'
            'Returned -- ' + str(how_many) + '\n'
            '\t\tRefund Total: ${0:.2f}'.format(total))
        return receipt

# def total_sales_cost():
#     """ str -> float
#     Returns the price (including the tax, 7%) calculated of the items
#     selected.
#     """
#

# def update_inventory():
#     """ str -> None
#     Update the file every time a new transaction is processed and will write it
#     to a .csv file.
#     """

if __name__ == '__main__':
    print(main())
