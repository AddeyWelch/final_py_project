import main


def test_show_inventory():
    assert main.show_inventory() == [[
        'Houses', 'Castle Bouncer (7)', 'Sports Bouncer (4)',
        'Disney Princess Bouncer (3)'
    ], ['Water Slides', '16" Wave Pool Slide (4)', 'Dolphin Slide (5)',
        'Giant Slip and Dip (2)'], ['Combo', 'Elephant Bouncer (6)',
                                    'Jurassic Adventure Course (2)',
                                    'Yellow Slide and Pool Combo (5)']]
# def test_rent_item():
#     assert main.rent_item('Disney Princess Bouncer', 1) == 107.0
#     assert main.rent_item('Jurassic Adventure Course', 1) == 240.75
#
#
# def test_purchase_item():
#     assert main.purchase_item('YRP Bounce Slide and Pool Combo', 1) == 668.75
#     assert main.purchase_item('Dolphin Slide', 2) == 1177.0
#
#
# def test_return_item():
#     assert main.return_item('Sports Bouncer', 1) == 10.7
#     assert main.return_item('16’ Wave Pool Slide', 3) == 56.2
#
#
# def test_total_sales_cost(rented_item):
#     assert main.test_total_sales_cost('total') == 800.0
#     assert main.test_total_sales_cost('total') == 500.0