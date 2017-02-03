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


if __name__ == '__main__':
    print(show_inventory())
