'''
Combining Gooey and PySimpleGUI
'''

import sys
from time import sleep
from gooey import Gooey, GooeyParser
import PySimpleGUI as sg

@Gooey(auto_start=True)
def main():
    _ = GooeyParser().parse_args(sys.argv[1:])

    print('Demo starting')

    window=sg.Window('interactive demo',
                     [ [sg.Text('Please pick source file')],
                       [sg.InputText(key='InputFilename'), sg.FileBrowse()],
                       [sg.Submit(), sg.Cancel()]])
    event, values = window.Read()
    window.close()

    if event == 'Submit':
        print(f'Pretending to process file {values["InputFilename"]}')
        sleep(4)
    print('Done')

if __name__ == '__main__':
    main()
