#!/usr/bin/python3

from qtgui import MainWindow
from PyQt5.QtWidgets import *
from qtgui.textparser import element,sub_element
class Test(MainWindow):
#    ui_file='a.txt'
    ui_text='''
mainwindow
    tabwidget
        widget label=[describ]
            vbox
                treewidget
                    labels="columna|columnB"
                    var data=data
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
        root=element('root')
        sub_element(root,'list1',{'text':'sfad sdfa'.split()})
        b=sub_element(root,'list2')
        sub_element(b,'huangao')
        sub_element(b,'listi')
        self['data']=root

    def click(self,item):
        s=self.open_files("请选择一个文件夹",'C:\\users')
        print(s)

if __name__=='__main__':
    Test.run()
