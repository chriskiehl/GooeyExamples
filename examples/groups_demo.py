'''
A simple Gooey example. One required field, one optional.
'''

from gooey import Gooey, GooeyParser


@Gooey()
def main():
    parser = GooeyParser(description='Log into webservice.')
    userIDGroup = parser.add_argument_group("UserID")

    userIDGroup.add_argument(
        '--login',
        metavar='Username',
        type=str,
        help='Enter you email address.')

    userIDGroup.add_argument(
        '--pwd',
        metavar='Password',
        type=str,
        help='Enter your password',
        widget="PasswordField")

    advSettingsGroup = parser.add_argument_group(
        "Advanced Settings",
        gooey_options={"collapsible": True})

    advSettingsGroup.add_argument(
        "--serviceUrl",
        metavar="Web service URL",
        type=str,
        help="Enter the url of the webservice you want to connect to.")

    args = parser.parse_args()
    print('Connected!')


if __name__ == '__main__':
    main()
