'''
Created on Dec 21, 2013

@author: Chris
'''

import sys
import hashlib
from time import time as _time
from time import sleep as _sleep

from gooey import Gooey
from gooey import GooeyParser
from gooey.examples import display_message


@Gooey(language='russian', program_name=u'\u041f\u0440\u0438\u043c\u0435\u0440 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b')
def arbitrary_function():
  desc = u"\u041f\u0440\u0438\u043c\u0435\u0440 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u002c \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u044c "
  file_help_msg = u"\u0418\u043c\u044f \u0444\u0430\u0439\u043b\u0430\u002c \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c"

  my_cool_parser = GooeyParser(description=desc)

  my_cool_parser.add_argument(
    'foo',
    metavar=u"\u0432\u044b\u0431\u043e\u0440\u0430\u0444\u0430\u0439\u043b\u043e\u0432",
    help=file_help_msg,
    widget="FileChooser")

  my_cool_parser.add_argument(
    'bar',
    metavar=u"\u041d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0444\u0430\u0439\u043b\u043e\u0432 \u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c",
    help=file_help_msg,
    widget="MultiFileChooser")

  my_cool_parser.add_argument(
    '-d',
    metavar=u'--\u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c',
    default=2,
    type=int,
    help=u'\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0028 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445 \u0029 \u043d\u0430 \u0432\u044b\u0445\u043e\u0434\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b')

  my_cool_parser.add_argument(
    '-s',
    metavar=u'--\u043a\u0440\u043e\u043d \u002d \u0433\u0440\u0430\u0444\u0438\u043a',
    help=u'\u0414\u0430\u0442\u0430',
    widget='DateChooser')

  args = my_cool_parser.parse_args()
  main(args)


def main(args):
  display_message()

def here_is_smore():
  pass


if __name__ == '__main__':
  arbitrary_function()
