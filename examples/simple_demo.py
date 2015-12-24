'''
A simple Gooey example. One required field, one optional.
'''


import argparse
from gooey import Gooey, GooeyParser

@Gooey()
def main():
  parser = GooeyParser(description='Process some integers.')

  parser.add_argument(
    'required_field',
    metavar='Some Field',
    help='Enter some text!')

  parser.add_argument(
    '-f', '--foo',
    metavar='Some Flag',
    action='store_true',
    help='I turn things on and off')

  args = parser.parse_args()
  print 'Hooray!'

if __name__ == '__main__':
  main()
