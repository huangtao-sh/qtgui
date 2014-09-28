#!/usr/bin/python3

from qtgui import MainWindow
class Test(MainWindow):
    ui_file='a.txt'
    ui_text=None
    '''
mainwindow
    widget
        form
            edit label=[int a]
                var a=text.int
            edit label=[int b]
                var b=text.int
            edit label=[sum]
                var c=text.int
            button text=[click]
                connect clicked=click
'''
    def click(self):
        self['c']=sum(self['a,b'])
    def hello(self):
        self['c']=sum(self['a,b'])
    
if __name__=='__main__':
    Test.run()
