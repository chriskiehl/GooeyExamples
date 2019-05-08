'''
Combining Gooey and formlayout
'''

import sys
from gooey import Gooey, GooeyParser
from formlayout import fedit



@Gooey(auto_start=True)
def main():
    _ = GooeyParser().parse_args(sys.argv[1:])

    print('Demo starting')
    R=fedit(title='Interactive data input example',
            data=[ ('What is your name', ''),
                   ('Are you married?',[2, 'Yes', 'No', 'It\'s complicated']) ],
            comment='Please fill the following information with care.')
            
    if R:
        print('Welcome {}'. format(R[0]))
        print('Your marital status is: '. format(R[1]))

if __name__ == '__main__':
    main()
