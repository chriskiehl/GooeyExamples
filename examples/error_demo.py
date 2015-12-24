'''
An example script to demonstrate Gooey's recovery from Client errors.

(It fails because it's supposed to)

'''

import time
from gooey import Gooey
from gooey import GooeyParser

# ascii art credit:
# http://www.chris.com/ascii/index.php?art=objects/explosives
NO_BOOM = r"""
          ,--.!,
       __/   -*-
     ,d08b.  '|`
     0088MM
     `9MMP'
  hjm
"""

BOOM = r"""
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____
       KAA-BOOOOOOM
"""



@Gooey(monospace_display=True)
def main():
  my_cool_parser = GooeyParser(description='This Demo will raise an error!')
  my_cool_parser.add_argument(
    "explode",
    metavar='Should I explode?',
    help="Determines whether or not to raise the error",
    choices=['Yes', 'No'],
    default='Yes')

  args = my_cool_parser.parse_args()
  if 'yes' in args.explode.lower():
    print 'Will throw error in'
    for i in range(5, 0, -1):
      print i
      time.sleep(.7)
    raise Exception(BOOM)

  print NO_BOOM
  print 'No taste for danger, eh?'

if __name__ == '__main__':
  main()
