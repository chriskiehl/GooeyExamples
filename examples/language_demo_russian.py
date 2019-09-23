# -*- coding: utf-8 -*-

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
import message


@Gooey(language='russian', program_name=u'Пример программы')
def arbitrary_function():
    desc = u"Пример приложения , чтобы показать "
    file_help_msg = u"Имя файла, который вы хотите обработать"

    my_cool_parser = GooeyParser(description=desc)

    my_cool_parser.add_argument(
        'foo',
        metavar=u"выборафайлов",
        help=file_help_msg,
        widget="FileChooser")

    my_cool_parser.add_argument(
        'bar',
        metavar=u"Несколько файлов Сохранить",
        help=file_help_msg,
        widget="MultiFileChooser")

    my_cool_parser.add_argument(
        '-d',
        metavar=u'--продолжительность',
        default=2,
        type=int,
        help=u'Продолжительность ( в секундах ) на выходе программы')

    my_cool_parser.add_argument(
        '-s',
        metavar=u'--крон - график',
        help=u'Дата',
        widget='DateChooser')

    args = my_cool_parser.parse_args()
    main(args)


def main(args):
    message()


def here_is_more():
    pass


if __name__ == '__main__':
    arbitrary_function()
