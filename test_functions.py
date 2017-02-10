import main


def test_show_inventory():
    assert main.show_inventory() == {
        'jurassic_adventure_course': [2, 225, 625],
        'sports_bouncer': [4, 100, 400],
        '16"_wave_pool_slide': [4, 175, 550],
        'giant_slip_and_dip': [2, 175, 500],
        'castle_bouncer': [7, 100, 400],
        'disney_princess_bouncer': [3, 100, 400],
        'yellow_slide_and_pool_combo': [5, 225, 625],
        'dolphin_slide': [5, 175, 550],
        'elephant_bouncer': [6, 225, 625]
    }


def test_rent_item():
    assert main.rent_item('disney_princess_bouncer', 2, 2) == (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + '2' + '\t' + 'disney_princess_bouncer' + '\n'
        'Rented -- ' + '2' + '\n'
        '\t\tTotal: $513.60')
    assert main.rent_item('jurassic_adventure_course', 1, 4) == (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + '1' + '\t' + 'jurassic_adventure_course' + '\n'
        'Rented -- ' + '4' + '\n'
        '\t\tTotal: $1029.88')


def test_purchase_item():
    assert main.purchase_item('yellow_slide_and_pool_combo', 1) == (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + '1' + '\t' + 'yellow_slide_and_pool_combo' + '\n'
        'Purchased -- ' + '1' + '\n'
        '\t\tTotal: $668.75')
    assert main.purchase_item('dolphin_slide', 2) == (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + '2' + '\t' + 'dolphin_slide' + '\n'
        'Purchased -- ' + '2' + '\n'
        '\t\tTotal: $1177.00')


def test_return_item():
    assert main.return_item('sports_bouncer', 1, 'y') == (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + '1' + '\t' + 'sports_bouncer' + '\n'
        'Returned Damaged -- ' + '1' + '\n'
        '\t\tTotal: $428.00')
    assert main.return_item('16"_wave_pool_slide', 3, 'n') == (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + '3' + '\t' + '16"_wave_pool_slide' + '\n'
        'Returned -- ' + '3' + '\n'
        '\t\tRefund Total: $55.00')

# def test_update_inventory():
#     assert main.test_update_inventory() ==
#     assert main.test_update_inventory() ==
