#!/usr/bin/python3

from qtgui import MainWindow
from PyQt5.QtWidgets import *
from qtgui.textparser import element,sub_element
class Test(MainWindow):
#    ui_file='a.txt'
    ui_text='''
mainwindow
    tabwidget
        groupbox args=["world"] layout=vbox
            treewidget
                labels="columna|columnB"
                var data=data
            hbox
                stretch
                button args=["hello"]
                    signal clicked=click
        groupbox args=["new view"] layout=vbox
            hbox
                radio args=["Hello"] 
                radio args=["world"] 
'''
    def init(self):
        super().init()
        root=element('root')
        sub_element(root,'list1',{'text':'sfad sdfa'.split()})
        b=sub_element(root,'list2')
        sub_element(b,'huangao')
        sub_element(b,'listi')
        self['data']=root

    def click(self,item):
        print(self.bg)

if __name__=='__main__':
    Test.run()
