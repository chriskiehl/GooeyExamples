# -*- coding: utf-8 -*-

'''
Created on Dec 21, 2013

@author: Chris
'''

from gooey import Gooey
from gooey import GooeyParser
import message

welcome_message = \
    r'''
 __          __  _
 \ \        / / | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \
    \  /\  /  __/ | (_| (_) | | | | | |  __/
  ___\/__\/ \___|_|\___\___/|_| |_| |_|\___|
 |__   __|
    | | ___
    | |/ _ \
    | | (_) |
   _|_|\___/                    _ _
  / ____|                      | | |
 | |  __  ___   ___   ___ _   _| | |
 | | |_ |/ _ \ / _ \ / _ \ | | | | |
 | |__| | (_) | (_) |  __/ |_| |_|_|
  \_____|\___/ \___/ \___|\__, (_|_)
                           __/ |
                          |___/
'''


@Gooey(language='japanese', program_name=u'プログラム例')
def arbitrary_function():
    desc = u"コマンドライン引数を入力してください"
    file_help_msg = u"処理したいファイルの名前"
    my_cool_parser = GooeyParser(description=desc)
    my_cool_parser.add_argument('foo', metavar=u"ファイルブラウザ",
                                help=file_help_msg, widget="FileChooser")   # positional

    my_cool_parser.add_argument(
        '-d',
        metavar=u'--デュレーション',
        default=2,
        type=int,
        help=u'プログラム出力の期間（秒）'
    )

    my_cool_parser.add_argument(
        '-s',
        metavar=u'--スケジュール',
        help=u'日時プログラムを開始すべき',
        widget='DateChooser'
    )
    my_cool_parser.add_argument(
        "-c",
        metavar=u"--ショータイム",
        action="store_true",
        help=u"カウントダウンタイマーを表示します"
    )
    my_cool_parser.add_argument(
        "-p",
        metavar=u"--ポーズ",
        action="store_true",
        help=u"一時停止の実行"
    )

    args = my_cool_parser.parse_args()
    main(args)


def main(args):
    message()


def here_is_more():
    pass


if __name__ == '__main__':
    arbitrary_function()
