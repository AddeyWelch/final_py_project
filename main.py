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
    if trans == 'rent':
        options = input(
            'Select one of the following:\nHOUSES\nCastle Bouncer (7)\tSports Bouncer (4)\tDisney Princess Bouncer (3)\nWATER SLIDES\n16’ Wave Pool Slide (4)\tDolphin Slide (5)\tGiant Slip and Dip (2)\nCOMBOS\nElephant Bouncer (6)\tJurassic Adventure Course (2)\tYRP Slide and Pool Combo (5)\n').lower(
            ).strip()
        how_many = input('Quantity:').strip()
        how_long = input(
            'How long are you wanting to rent this item for?').strip()


def purchase_item(trans):
    """ str, int -> float
    Display the items available to purchase from. Allows the customer to select
    the item of their choice and the quantity of that item.
    """
    if trans == 'purchase':
        options = input(
            'Select one of the following:\nHOUSES\nCastle Bouncer (7)\tSports Bouncer (4)\tDisney Princess Bouncer (3)\nWATER SLIDES\n16’ Wave Pool Slide (4)\tDolphin Slide (5)\tGiant Slip and Dip (2)\nCOMBOS\nElephant Bouncer (6)\tJurassic Adventure Course (2)\tYRP Slide and Pool Combo (5)\n').lower(
            ).strip()
        how_many = input('Quantity:').strip()

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
# def test_total_sales_cost():
#     """ str -> float
#     Returns the price (including the tax, 7%) calculated of the items selected.
#     """
#
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
    # if who == 'customer':
    #     print('Welcome to Bounce Into Fun!')
    #     trans = input(
    #         'Which transaction would you like to complete? (Enter RENT, RETURN, PURCHASE, or REPLACE)').strip(
    #         ).lower()
    #     if trans == 'rent':
    #         options = input(
    #             'Select one of the following:\nHOUSES\t\tWATER SLIDES\t\tCOMBOS\n').lower(
    #             ).strip()
    #         # display = # category options (3 of them w/ stock num) and price
    #         choice = input('Which one would you like?').strip().lower()
    #         how_many = input('Quantity:').strip()
    #         how_long = input(
    #             'How long are you wanting to rent this item for?').strip()
    #             if how_long >= 1:
    #                 '*********\nBOUNCE INTO FUN\nThank you for shopping with us\n*********'
    #
    #                 continue
    #             elif how_many >= 5:
    #                 return 'Max number of days to rent this item is 5 days, please re-enter a valid number to complete your process.'
