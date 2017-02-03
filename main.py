def show_inventory():
    """ list of strings -> str
    Allows the user to view what inventory is in stock.
    """
    with open('inventory.txt', 'r') as file:
        new_list = file.read().split(' - ').strip()
    print(new_list)
