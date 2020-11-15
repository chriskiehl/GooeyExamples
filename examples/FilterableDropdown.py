"""
Demo showing FilterableDropdown's capabilities when
backed by a large dataset.
"""
import os
import csv
import zipfile
from io import TextIOWrapper

from gooey import Gooey, GooeyParser, PrefixTokenizers

path = os.path.join(os.path.dirname(__file__), 'sample_data', 'worldcities.zip')

with zipfile.ZipFile(path) as zf:
    with zf.open('worldcities.csv', 'r') as f:
        reader = csv.reader(TextIOWrapper(f, 'utf-8'))
        data = ['{} - {}'.format(x[4], x[1]) for x in reader][1:]


@Gooey(program_name='FilterableDropdown Demo', poll_external_updates=True)
def main():
    parser = GooeyParser(description="Example of the Filterable Dropdown")
    parser.add_argument(
        "-a",
        "--myargument",
        metavar='Country',
        help='Search for a country',
        choices=data,
        widget='FilterableDropdown',
        gooey_options={
            'label_color': (255, 100, 100),
            'placeholder': 'Start typing to view suggestions',
            'search_strategy': {
                'type': 'PrefixFilter',
                'choice_tokenizer': PrefixTokenizers.WORDS,
                'input_tokenizer': PrefixTokenizers.REGEX('\s'),
                'ignore_case': True,
                'operator': 'AND',
                'index_suffix': False  # set to True to enable substring searching!
            }
        })
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    import sys
    import json
    if 'gooey-seed-ui' in sys.argv:
        print(json.dumps({'-b': data}))
    else:
        main()
