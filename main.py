import csv

rental_fees = {'castle_bouncer': [7, 100, 400],
               'sports_bouncer': [4, 100, 400],
               'disney_princess_bouncer': [3, 100, 400],
               '16"_wave_pool_slide': [4, 175, 550],
               'dolphin_slide': [5, 175, 550],
               'giant_slip_and_dip': [2, 175, 500],
               'elephant_bouncer': [6, 225, 625],
               'jurassic_adventure_course': [2, 225, 625],
               'yellow_slide_and_pool_combo': [5, 225, 625]}


def main():
    """ str -> None
    Contains some of the program's branching and all the functions parameters
    ('inputs')
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
                # elephant_bouncer --> Elephant Bouncer
                print('{0} - {1} - ${2}'.format(key, value[0], value[1]))
                # Format of the dict --> Castle Bouncer - 7 - $400
            options = input().strip().lower().replace(' ', '_')
            # Castle Bouncer --> castle_bouncer
            while True:
                try:
                    how_many = int(input('Quantity:').strip())
                    break
                except:
                    print("That's not an integer..")
                    continue
            for num in str(how_many):
                if num > str(rental_fees[options][0]):
                    return 'This input is invalid, please try again!'
                else:
                    how_long = int(input(
                        'How long are you wanting to rent this item for?').strip(
                        ))
                    return rent_item(options, how_many, how_long)
        elif trans == 'purchase':
            print('Please select one of the following:')
            for key, value in rental_fees.items():
                key = key.replace('_', ' ').title()
                # elephant_bouncer --> Elephant Bouncer
                print('{0} - {1} - ${2}'.format(key, value[0], value[2]))
                # Format of the dict --> Castle Bouncer - 7 - $400
            options = input().strip().lower().replace(' ', '_')
            # Castle Bouncer --> castle_bouncer
            while True:
                try:
                    how_many = int(input('Quantity:').strip())
                    break
                except:
                    print("That's not an integer..")
                    continue
            for num in str(how_many):
                if num > str(rental_fees[options][0]):
                    return 'This input is invalid, please try again!'
                else:
                    return purchase_item(options, how_many)
        elif trans == 'return':
            for key, value in rental_fees.items():
                key = key.replace('_', ' ').title()
                # elephant_bouncer --> Elephant Bouncer
                print('{0}'.format(key))
                # Format of the dict --> Castle Bouncer
            which_one = input('Which item are you returning?\n').strip().lower(
            ).replace(' ', '_')
            # Castle Bouncer --> castle_bouncer
            while True:
                try:
                    how_many = int(input('Quantity:').strip())
                    break
                except:
                    print("That's not an integer..")
                    continue
            for num in str(how_many):
                if num > str(rental_fees[which_one][0]):
                    return 'Please enter the correct number of items.'
                else:
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
        # [['Houses', 'Castle Bouncer (7)', 'Sports Bouncer (4)',
        #     'Disney Princess Bouncer (3)'],
        # ['Water Slides', '16" Wave Pool Slide (4)', 'Dolphin Slide (5)',
        #     'Giant Slip and Dip (2)'],
        # ['Combo', 'Elephant Bouncer (6)', 'Jurassic Adventure Course (2)',
        #   'Yellow Slide and Pool Combo (5)']]
        return list_info


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
        'Rented -- ' + str(how_long) + '\n'
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

# def total_sales_cost():
#     """ str -> float
#     Returns the price (including the tax, 7%) calculated of the items
#     selected.
#     """
#


def update_inventory():
    """ str -> None
    Update the file every time a new transaction is processed and will write it
    to a .csv file.
    """


if __name__ == '__main__':
    print(main())
