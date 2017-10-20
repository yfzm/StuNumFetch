# -*- coding:utf-8 -*-
from Tkinter import *
import pinyin
import csv


class StuNumFetch:
    def __init__(self):
        print "正在读取并初始化数据，请稍后..."
        self.data = []
        self.readData()
        self.getPinyin()
        print "数据读取完毕！"
        self.root = Tk()
        self.root.title(u"学号-姓名匹配")
        self.root.geometry("470x300")
        self.root.resizable(0, 0)
        self.drawAll()

        self.root.mainloop()

    def readData(self):
        with open('StudNum.csv', 'rb') as myFile:
            lines = csv.reader(myFile)
            for line in lines:
                self.data.append(line)

    def getPinyin(self):
        apinyin = pinyin.PinYin()
        apinyin.load_word()

        for everyone in self.data:
            #print everyone[2]
            name_py = apinyin.hanzi2pinyin(string=everyone[2])
            ss = ""
            for item in name_py:
                ss += item
            name_sp = apinyin.hanzi2shoupin(string=everyone[2])
            everyone.append(ss)
            everyone.append(name_sp)
            #print type(everyone[1])
            #print name_sp

        #for everyone in self.data:
            #print everyone[4]

    def drawAll(self):
        self.enquiry = Entry(self.root, font=(None, 20), width=30)
        self.result = Listbox(self.root, font=(None, 12), width=53)
        self.result.insert(END, u"请在上方输入学号或姓名的拼音（或首拼）来检索")
        self.result.insert(END, "")
        self.result.insert(END, u"注意：请将输入法切换至英文状态，否则本程序将不可用！")

        self.enquiry.place(x=20, y=20, anchor="nw")
        self.result.place(x=20, y=70, anchor="nw")

        self.enquiry.focus_set()

        self.enquiry.bind('<KeyPress>', self.fetch)

    def fetch(self, t):
        if len(str(t.keysym)) > 1:
            return

        self.result.delete(0, END)
        enq = str(self.enquiry.get()) + str(t.keysym)
        for everyone in self.data:
            if enq in everyone[1] or enq in everyone[4] or enq in everyone[5]:
                ss = ""
                for item in everyone[:-2]:
                    ss += str(item) + " "
                self.result.insert(END, ss)

if __name__ == "__main__":
    snf = StuNumFetch()
