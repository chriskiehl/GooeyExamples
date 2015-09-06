'''
A minimal Gooey example. One required field, one optional.

'''


import argparse
from gooey import Gooey

@Gooey(dump_build_config=True)
def main():
  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('integers', metavar='N', nargs='+',
                     help='an integer for the accumulator')
  parser.add_argument('--sum', dest='accumulate', action='store_const',
                     ### Notice that we store the function names as strings rather than the functions themselves
                     ### This is to allow serialization to JSON
                     const='sum', default='max',
                     help='sum the integers (default: find the max)')

  args = parser.parse_args()
  print getattr(__builtins__, args.accumulate)(map(int, args.integers[0].split()))


if __name__ == '__main__':
  main()
