'''
Created on Dec 21, 2013
 __          __  _
 \ \        / / | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \
    \  /\  /  __/ | (_| (_) | | | | | |  __/
  ___\/__\/ \___|_|\___\___/|_| |_| |_|\___|
 |__   __|
    | | ___
    | |/ _ \
    | | (_) |
   _|_|\___/                    _ _
  / ____|                      | | |
 | |  __  ___   ___   ___ _   _| | |
 | | |_ |/ _ \ / _ \ / _ \ | | | | |
 | |__| | (_) | (_) |  __/ |_| |_|_|
  \_____|\___/ \___/ \___|\__, (_|_)
                           __/ |
                          |___/

@author: Chris
'''

from gooey.python_bindings.gooey_decorator import Gooey
from gooey.python_bindings.gooey_parser import GooeyParser


@Gooey(
    program_name='Advanced Layout Groups',
    sidebar_title="Your Custom Title",
    show_sidebar=False,
    dump_build_config=True,
    # body_bg_color='#ffffff'

)
def main():
    message = (
        'Hi there!\n\n' 
        'Welcome to Gooey! \nThis is a demo of the flexible layouts and overall' 
        'customization you can achieve by using argument groups and '
        'the new gooey_options feature.')



    import sys
    print(sys.argv)
    desc = "Example application to show Gooey's various widgets"
    file_help_msg = "Name of the file you want to process"
    my_cool_parser = GooeyParser(description=desc, add_help=False)

    description_area = my_cool_parser.add_argument_group(
        "About",
        gooey_options={
            'show_border': True,
            'show_underline': False,
        }
    )

    description_area.add_argument(
        'thing',
        default=message,
        widget='Textarea',
        help="asdfsadfasdfa sdfadf ad",
        gooey_options={
            'height': 100,
            'show_help': False,
            'show_label': False,
            'readonly': True
        }
    )

    categories = my_cool_parser.add_argument_group(
        'Categories',
        gooey_options={
            'show_border': True,
            'columns': 2,
            # 'margin_top': 20
        }
    )

    categories.add_argument(
        '--parent-category',
        metavar='Parent Category',
        help='This is a very, very, very long help text '
                             'to explain a very, very, very important input value. '
                             'Unfortunately, the end of this long message is cropped. ',
        choices=['a', 'b', 'c'],
        required=True,
        gooey_options={
            'label_color': '#FF9900',
            # 'help_color': '#ff00ff',
            # 'help_bg_color': '#ff0000'
        })

    categories.add_argument(
        '--subcategory',
        metavar='Subcategory',
        help='Select Subcategory',
        choices=['a', 'b', 'c'],
        required=True,
        gooey_options={
            'label_color': '#FF9900',
            'validator': {
                'type': 'local',
                'test': 'user_input > 10',
                'message': 'this is a super long error message wtih multiple ideas and suggestions on how to go about resolving the error '
            }
            # 'help_color': '#ff00ff',
            # 'help_bg_color': '#ff0000'
        })


    search_options = my_cool_parser.add_argument_group(
        'Search Options',
        'Customize the search options',
        gooey_options={
            'show_border': True,
            'columns': 2
        }
    )

    search_options.add_argument('--query', help='base search string'
                                    , gooey_options={'full_width': True}
                                    )

    search_flags = search_options.add_argument_group('Flags',
                                                     gooey_options={'show_border': True}
                                                     )
    search_flags.add_argument('--buy-it-now',
                              metavar='Buy it Now',
                              help="Will immediately purchase if possible",
                              action='store_true',
                              widget='BlockCheckbox')
    search_flags.add_argument('--auction',
                              metavar='Auction',
                              help="Place bids up to PRICE_MAX",
                              action='store_true',
                              widget='BlockCheckbox',
                              gooey_options={
                                  'label_color': '#ff00fe',
                                  'checkbox_label': 'Enable'
                              }
    )

    price_range = search_options.add_argument_group('Price_Range',
                                                    gooey_options={'show_border': True}
                                                    )

    price_range.add_argument('--price-min',
                             help=
                             'This'
                             # 'is a very, very, very long help text '
                             # 'to explain a very, very, very important input value. '
                             )
    price_range.add_argument('--price-max', help='max price')

    my_cool_parser.print_help()
    args = my_cool_parser.parse_args()
    print(args)
    print("Hiya!")
    for i in range(20):
        import time
        print('Howdy', i)
        time.sleep(.3)
    # print(args.listboxie)


def here_is_smore():
    pass


if __name__ == '__main__':
    main()
