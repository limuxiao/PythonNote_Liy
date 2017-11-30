# -*- coding:utf-8 -*-
class SweetPatato:
    def __init__(self):
        self.cooked_string = '生的'
        self.cooked_level = 0
        self.comps = []
        pass

    def cook(self, cooked_level):
        self.cooked_level += cooked_level
        if 0 <= self.cooked_level < 3:
            self.cooked_string = '生的'
        elif 3 <= self.cooked_level < 5:
            self.cooked_string = '半生不熟'
        elif 5 <= self.cooked_level < 8:
            self.cooked_string = '熟的'
        elif self.cooked_level >= 8:
            self.cooked_string = '烤糊了'

    def addComp(self, comp):
        self.comps.append(comp)

    def __str__(self):
        return '烤了%d分钟，现在是%s'%(self.cooked_level,self.cooked_string) + ',加了:' + str(self.comps)