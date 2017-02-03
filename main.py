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


def rent_item():
    """ str, int -> str
    Display the items available to rent from. Allows the customer to select the
    item of their choice and the quantity of that item.
    """
    rent = [100, 175, 225]
    tax = 0.07  # (7%)

# def purchase_item():
#     """ str, int -> float
#     Display the items available to purchase from. Allows the customer to select
#     the item of their choice and the quantity of that item.
#     """
#
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
    who = input('Are you administration or customer?').lower().strip()
    print(show_inventory())
