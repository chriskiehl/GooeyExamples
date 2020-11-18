'''
Combining Gooey and PySimpleGUI
'''

import sys
from time import sleep
from gooey import Gooey, GooeyParser
if sys.version_info[0] >= 3: import PySimpleGUI as sg  
else:                        import PySimpleGUI27 as sg  


@Gooey(auto_start=True)
def main():
    _ = GooeyParser().parse_args(sys.argv[1:])

    print('Demo starting')
    
    window=sg.Window('interactive demo',
                     [ [sg.Text('Please pick source file')],
                       [sg.InputText(key='InputFilename'), sg.FileBrowse()],
                       [sg.Submit(), sg.Cancel()]])
    event, values = window.Read()
    window.Close()
    
    if event == 'Submit':
        print('Pretending to process file '+values['InputFilename'])
        sleep(4)
    print('Done')
    
if __name__ == '__main__':
    main()
