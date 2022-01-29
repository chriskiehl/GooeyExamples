"""
This is the
"""
import csv
import zipfile
from gooey import Gooey, GooeyParser

import os
from io import TextIOWrapper

path = os.path.join(os.path.dirname(__file__), 'sample_data', 'worldcities.zip')

with zipfile.ZipFile(path) as zf:
    with zf.open('worldcities.csv', 'r') as f:
        reader = csv.reader(TextIOWrapper(f, 'utf-8'))
        locations = ['{} - {}'.format(x[4], x[1]) for x in reader][1:][:1000]


@Gooey(program_name='Square BnB v8.0')
def version8():
    parser = GooeyParser(
        description='Welcome to SquareBnb travel. Wherever you go, we have a place for you')

    location = parser.add_argument_group('Find a place to stay', gooey_options={
        'show_border': True
    })
    location.add_argument(
        'location',
        metavar='Location',
        choices=locations,
        help='Where are you going?',
        widget='FilterableDropdown',
        gooey_options={
            'full_width': True
        })
    location.add_argument(
        'guests',
        metavar='Guests',
        help='Add Guests',
        type=int,
        choices=range(11),
        gooey_options={'full_width': True})
    location.add_argument(
        'check-in',
        metavar='Check in',
        widget='DateChooser',
        help='Add Dates')
    location.add_argument(
        'check-out',
        metavar='Check out',
        widget='DateChooser',
        help='Add Dates')

    pricing = parser.add_argument_group('Pricing', gooey_options={
        'show_border': True
    })
    pricing.add_argument(
        '--min-price',
        help='Minimum Price',
        gooey_options={'show_help': False, 'label_color': '#2e2424'})
    pricing.add_argument(
        '--max-price',
        help='Maximum Price',
        gooey_options={'show_help': False, 'label_color': '#2e2424'})

    # FILTERS
    filters = parser.add_argument_group('Popular Filters', gooey_options={
        'show_border': True,
    })
    filters.add_argument('--ignore-me', gooey_options={'visible': False})
    housing = filters.add_argument_group('Rooms and Beds', gooey_options={
        'show_border': True,
        'columns': 1
    })
    housing.add_argument(
        '--rooms',
        metavar='Rooms',
        type=int,
        choices=range(11), help='How many rooms do you need?')
    housing.add_argument(
        '--beds',
        metavar='Beds',
        type=int,
        choices=range(11), help='How many beds do you need?')
    housing.add_argument(
        '--bathrooms',
        metavar='Bathrooms',
        type=int,
        choices=range(11), help='How many bathrooms do you need?')

    ammenities = filters.add_argument_group('Amenities', gooey_options={
        'show_border': True,
        'columns': 2
    })
    ammenities.add_argument(
        '--entire-place',
        metavar='Entire Place',
        action='store_true',
        help='Have the whole place to yourself')
    ammenities.add_argument(
        '--house',
        metavar='House',
        action='store_true', help='No apartments, plz')
    ammenities.add_argument(
        '--wifi',
        metavar='WIFI',
        action='store_true', help='Internet is a must!')
    ammenities.add_argument(
        '--kitchen',
        metavar='Kitchen',
        action='store_true', help='A place to cook')

    args = parser.parse_args()
    print(args)
    # ... rest of program



if __name__ == '__main__':
    version8()