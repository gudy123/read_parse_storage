#!/usr/bin/python
# coding:utf-8
import sys
sys.path.append(r"E:\和信\导入信息\mylib")
import mylib
from bs4 import BeautifulSoup
import bs4
import random
import re
from abstract import compress

def x_parse(path):
    with open("compress_example.html","r",encoding='utf-8') as f:
        text = f.read()
    soup = BeautifulSoup(text,features="lxml")

    q = (soup.body.get_text().replace("\n","").replace("\xa0",""))
    q = q.split("#@#")[1:]
    res = []
    for i in q:
        item = mylib.Item()
        i = re.split('[【】]',i)
        item.settime(i[0])
        text, kp = compress(i[-1])
        item.setorimsg(i[-1])
        item.setmsg(text)
        l0 = len(kp)
        if l0 > 0:
            item.setmark10(kp[0])
        if l0 > 1:
            item.setmark9(kp[1])
        if l0 > 2:
            item.setmark8(kp[2])
        item.setid(i[0]+str(random.randint(0,59))+str(random.randint(0,59))+str(random.randint(0,99)))
        l = len(i)
        if l > 2:
            item.setmark1(i[1])
        if l > 3:
            item.setmark2(i[2])
        if l > 4:
            item.setmark3(i[3])
        if l > 5:
            item.setmark4(i[4])
        if l > 6:
            item.setmark5(i[5])
        if l > 7:
            item.setmark6(i[6])
        if l > 8:
            item.setmark7(i[7])
        if l > 9:
            item.setmark8(i[8])
        if l > 10:
            item.setmark9(i[9])
        if l > 11:
            item.setmark10(i[10])
        res.append(eval(item.getjson()))
    mylib.writeInMongo("other","compress_instruction",res)
    
def main():
    #读取文件
    mfiles = mylib.readFiles(kind=["html"])
    threads = []
    for filename in mfiles:
        threadt = mylib.myThread(filename)
        #启动线程
        threadt.start()
        threads.append(threadt)
    for t in threads:
        t.join()
    #对每个文件建一个线程：处理获取文字，解析，写入数据库
    
if __name__ == "__main__":
    main()
