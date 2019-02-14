'''
A Gooey example showing use of richtext display in the console pannel.
'''

from gooey import Gooey, GooeyParser
from colored import stylize, attr, fg

@Gooey(richtext_controls=True, auto_start=True)
def main():
    parser = GooeyParser(description='Just display the console')

    args = parser.parse_args()
    print(stylize("This is bold.", attr("bold")))
    print(stylize("This is underlined.", attr("underlined")))
    print(stylize("This is green.", fg("green")))
    print(stylize("This is red.", fg("red")))
    print(stylize("This is blue and bold.", fg("blue") + attr("bold")))


if __name__ == '__main__':
    main()
