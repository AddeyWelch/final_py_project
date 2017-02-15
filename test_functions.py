import main


def test_rent_item():
    assert main.rent_item('disney_princess_bouncer', 2, 2) == (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + '2' + '\t' + 'disney_princess_bouncer' + '\n'
        'Rented -- ' + '2' + ' days' + '\n'
        '\t\tTotal: $513.60')
    assert main.rent_item('jurassic_adventure_course', 1, 4) == (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + '1' + '\t' + 'jurassic_adventure_course' + '\n'
        'Rented -- ' + '4' + ' days' + '\n'
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
    assert main.return_item('sports_bouncer', 1, 'yes') == (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + '1' + '\t' + 'sports_bouncer' + '\n'
        'Returned Damaged -- ' + '1' + '\n'
        '\t\tTotal: $428.00')
    assert main.return_item('16"_wave_pool_slide', 3, 'no') == (
        '******\nBOUNCE INTO FUN\nThank you for shopping with us!\n******'
        '\n' + '3' + '\t' + '16"_wave_pool_slide' + '\n'
        'Returned -- ' + '3' + '\n'
        '\t\tRefund Total: $55.00')
