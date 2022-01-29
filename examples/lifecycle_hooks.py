"""
Demos the usage of Gooey's lifecycle hooks
"""
from gooey import Events, Gooey, GooeyParser
from gooey import types as t

def between_zero_and_ten(value: str):
    try:
        integer = int(value)
        if 0 <= integer <= 10:
            return integer
        else:
            raise Exception("Hey! What did I tell you!!?")
    except ValueError:
        # upgrading the default error message.
        raise ValueError('Hey! I said enter a number!')


def handle_success(args, state: t.PublicGooeyState):
    field = state['active_form'][0]
    field['value'] = 'Good job, now try this one: ' + str(args.number + 1)
    return {**state, 'active_form': [field]}


def handle_error(args, state: t.PublicGooeyState):
    field = state['active_form'][0]
    field['value'] = 'You see what you did!?'
    return {**state, 'active_form': [field]}


@Gooey(use_events=[Events.ON_ERROR, Events.ON_SUCCESS, Events.VALIDATE_FORM])
def main():
    parser = GooeyParser(on_success=handle_success, on_error=handle_error)
    parser.add_argument('number', type=between_zero_and_ten, help="Enter any value between 0 and 10. No funny business.")
    args = parser.parse_args()
    if args.number == 10:
        raise Exception('I have decided 10 is not allowed either!')
    print('All done! Here is what you entered: ', args)
    print('Now go back to the edit screen. Your input has been magically updated!')


if __name__ == '__main__':
    main()

