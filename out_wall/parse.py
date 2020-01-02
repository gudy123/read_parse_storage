#!/usr/bin/python
# coding:utf-8
from bs4 import BeautifulSoup
import bs4
import sys
sys.path.append(r"E:\和信\导入信息\mylib")
import mylib
import mylib
import random
import re

def x_parse(path):
    data = []
    with open(path,"r",encoding = 'utf-8') as f:
        text = f.read()
    soup = BeautifulSoup(text,features="lxml")

    q = (soup.body.get_text().replace("\n","").replace("\xa0",""))
    q = q.split("#@#")[1:]
    res = []
    for i in q:
        item = mylib.Item()
        i = re.split('[【】]',i)
        item.settime(i[0])
        item.setid(i[0]+str(random.randint(0,59))+str(random.randint(0,59))+str(random.randint(0,99)))
        item.setmsg(i[-1])
        l = len(i)
        if l > 2:
            item.setmark1(i[1])
        if l > 3:
            item.setmark2(i[2])
        if l > 4:
            item.setmark1(i[3])
        if l > 5:
            item.setmark2(i[4])
        if l > 6:
            item.setmark1(i[5])
        if l > 7:
            item.setmark2(i[6])
        if l > 8:
            item.setmark1(i[7])
        if l > 9:
            item.setmark2(i[8])
        if l > 10:
            item.setmark1(i[9])
        if l > 11:
            item.setmark2(i[10])
        res.append(eval(item.getjson()))
    mylib.writeInMongo("other","instruction",res)
    
def main():
    mfiles = mylib.readFiles(kind = "html")
    threads = []
    for filename in mfiles:
        threadt = mylib.myThread(filename)
        threadt.start()
        threads.append(threadt)
    for t in threads:
        t.join()

    
if __name__ == "__main__":
    main()
