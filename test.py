#!/usr/bin/python3

from qtgui import MainWindow
from PyQt5.QtWidgets import *
class Test(MainWindow):
#    ui_file='a.txt'
    ui_text='''
mainwindow
    tabwidget
        widget label=[describ]
            vbox
                textbrowser
                hbox
                    stretch
                    button text=[hello]
                        signal clicked=click
        widget label=[search]
            vbox
                edit
                edit
                hbox
                    stretch
                    button text=[info]
                        signal clicked=click
       
'''
    def init(self):
        super().init()

    def click(self,item):
        self.showinfo("Hello world")


if __name__=='__main__':
    Test.run()
