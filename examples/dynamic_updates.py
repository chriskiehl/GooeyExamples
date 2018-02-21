"""
Dynamic updates in Gooey

Simple example demonstrating feeding Gooey a dynamic list of file names at runtime
"""
import datetime
import json
import os
import sys

from gooey import Gooey, GooeyParser

directory_error = (
    'Unable to create a folder for your save files!\n'
    'Make sure you\re running in a directory where you have write permissions!'
)


@Gooey(
    program_name="Using Dynamic Values",
    poll_external_updates=True)
def main():
    mk_savedir()  # Make directory to store user's save files

    parser = GooeyParser(
        description='An example of polling for updates at runtime')
    g = parser.add_argument_group()
    stuff = g.add_mutually_exclusive_group(
        required=True,
        gooey_options={
            'initial_selection': 0
        }
    )
    stuff.add_argument(
        '--save',
        metavar='Save Progress',
        action='store_true',
        help='Take a snap shot of your current progress!'
    )
    stuff.add_argument(
        '--load',
        metavar='Load Previous Save',
        help='Load a Previous save file',
        dest='filename',
        widget='Dropdown',
        choices=list_savefiles(),
        gooey_options={
            'validator': {
                'test': 'user_input != "Select Option"',
                'message': 'Choose a save file from the list'
            }
        }
    )

    args = parser.parse_args()

    if args.save:
        save_file()
    else:
        read_file(os.path.join('saves', args.filename))
        print('Finished reading file!')


def read_file(path):
    with open(path, 'r') as f:
        print(f.read())


def list_savefiles():
    """ List all available files in the save directory """
    return list(sorted(os.listdir('saves'), reverse=True))


def show_error_modal(error_msg):
    """ Spawns a modal with error_msg"""
    # wx imported locally so as not to interfere with Gooey
    import wx
    app = wx.App()
    dlg = wx.MessageDialog(None, error_msg, 'Error', wx.ICON_ERROR)
    dlg.ShowModal()
    dlg.Destroy()


def save_file():
    """Save a plain ol' text file with some metadata in the title"""
    next_number = '{:04d}'.format(len(list_savefiles()) + 1)
    now = datetime.datetime.now().strftime('%b %d, %Y - %H.%M%p')
    filename = 'Save {} @ {}.save'.format(next_number, now)
    with open(os.path.join('saves', filename), 'w') as f:
        f.write("Hello World!")
    print('Saved {}!'.format(filename))


def mk_savedir():
    """
    Attempt to create a directory where we can store the user's save files
    """

    try:
        if sys.version_info[0] > 2:  # if Python 3
            os.makedirs('saves', exist_ok=True)

        elif sys.version_info[0] < 3:  # if Python 2
            try:
                os.makedirs('saves')

            except OSError:
                if not os.path.isdir('saves'):
                    raise

    except IOError as e:
        if not e.winerror == 183:  # already exists
            show_error_modal(directory_error)
            sys.exit(1)


if __name__ == '__main__':
    if 'gooey-seed-ui' in sys.argv:
        print(json.dumps({'--load': list_savefiles()}))
    else:
        main()
