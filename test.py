#!/usr/bin/python3

from qtgui import MainWindow
from PyQt5.QtWidgets import *
class Test(MainWindow):
#    ui_file='a.txt'
    ui_text='''
mainwindow
    widget
        hbox
            tablewidget
                hlabels="姓名 账户"
                columnwidths=[100,60]
                var tab=data
                signal itemclicked=tb1click
            form
                tablewidget name=tw
                    rowcount=5
                    hlabels="账户 户名"
                    columnwidths=[100,80]
                    var tab2=data
                    signal itemclicked=tb1click
                button text=[click]
                    connect clicked=click
'''
    def init(self):
        super().init()
        self['tab']=[['sf','sfd'],['sdfawe','sdfafasd']]
        self['tab2']=[['huangtao','Youku'],
                      ['zhangsan','fsdljl'],]
    def click(self,item):
        self['tab']=['asfd fsd'.split(),
                     'sfdafsd  sfda'.split(),
                     'sfdawe fsda'.split()]
        print(self['tab'])

    def tb1click(self,item):
        s=item.tableWidget().item(item.row(),0).text()
        self.showinfo(s)

if __name__=='__main__':
    Test.run()
