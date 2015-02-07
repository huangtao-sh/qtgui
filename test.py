#!/usr/bin/python3

from qtgui import MainWindow
from PyQt5.QtWidgets import *
class Test(MainWindow):
#    ui_file='a.txt'
    ui_text='''
mainwindow
    widget
        hbox
            scrollarea
                treewidget
                    labels="姓名 账户"
                    columnwidths=[100,60]
                    var twdata=data
            form
                tablewidget name=tw label=[label1]
                    rowcount=5
                    hlabels="账户 户名"
                    columnwidths=[100,80]
                    var tab2=data
                    signal itemclicked=tb1click
                scrollarea
                    textbrowser label=[label3] name=edt1
                        var ab=text
                button text=[click]  label=[label2]
                    signal clicked=edt1.copy
                    slot setenabled=edt1.copyavailable
'''
    def init(self):
        super().init()
        self['ab']='hello world'
        self['tab']=[['sf','sfd'],['sdfawe','sdfafasd']]
        self['tab2']=[['huangtao','Youku'],
                      ['zhangsan','fsdljl'],]
    def click(self,item):
        d=[{'text':'fads sfd'.split(),'icon':'up.png',
            'childs':[
            {'text':'halo fsd'.split(),},
            {'text':'youku dfs'.split()} ]},
           {'text':'sfda sfda'.split(),}]
        self['twdata']=d

    def tb1click(self,item):
        s=item.tableWidget().item(item.row(),0).text()
        self.showinfo(s)

if __name__=='__main__':
    Test.run()
