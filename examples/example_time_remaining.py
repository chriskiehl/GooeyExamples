from gooey import Gooey, GooeyParser
import os

@Gooey(optional_cols=2,
        program_name="Elapsed / Remaining Timer on Progress in Gooey",

        progress_regex=r"^progress: (?P<current>\d+)/(?P<total>\d+)$",
        progress_expr="current / total * 100",
        hide_progress_msg=True,

        timing_options={
            'show_time_remaining':True,
            'hide_time_remaining_on_complete':True
        }
        )
def parse_args():
    prog_descrip = 'Elapsed / Remaining Timer on Progress in Gooey'
    parser = GooeyParser(description=prog_descrip)

    sub_parsers = parser.add_subparsers(help='commands', dest='command')

    range_parser = sub_parsers.add_parser('range')

    range_parser.add_argument('--length',default=10)

    return parser.parse_args()

def compute_range(length):

    for i in range(length):
        # print("sometin")
        import time
        from random import randint
        time.sleep(randint(1,3))
        print(f"progress: {i}/{length}")

if __name__ == '__main__':
    conf = parse_args()
    if conf.command == 'range':
        compute_range(int(conf.length))
