from core import (show_inventory, rent_item, purchase_item, return_item)

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
            if options in rental_fees:
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
            else:
                return 'The item you have entered is not available.'
        elif trans == 'purchase':
            print('Please select one of the following:')
            for key, value in rental_fees.items():
                key = key.replace('_', ' ').title()
                # elephant_bouncer --> Elephant Bouncer
                print('{0} - {1} - ${2}'.format(key, value[0], value[2]))
                # Format of the dict --> Castle Bouncer - 7 - $400
            options = input().strip().lower().replace(' ', '_')
            # Castle Bouncer --> castle_bouncer
            if options in rental_fees:
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
            else:
                return 'The item you have entered is not available.'
        elif trans == 'return':
            for key, value in rental_fees.items():
                key = key.replace('_', ' ').title()
                # elephant_bouncer --> Elephant Bouncer
                print('{0}'.format(key))
                # Format of the dict --> Castle Bouncer
            which_one = input('Which item are you returning?\n').strip().lower(
            ).replace(' ', '_')
            # Castle Bouncer --> castle_bouncer
            if which_one in rental_fees:
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
                        if condition == 'y':
                            return return_item(which_one, how_many, condition)
                        else:
                            return 'You must enter y or n.'
            else:
                return 'The item you have entered is not available.'
        else:
            return "I'm sorry but this transaction can not be completed. Please try again."
    else:
        return 'This input is invalid!'


if __name__ == '__main__':
    print(main())
