import os
import pymongo
import threading
import random
import time
from parse import x_parse

#读文件夹内文件
#path 不设置时，默认在代码的当前路径读文件
def readFiles(path="",kind=["txt"]):
    if path == "":
        file_dir = os.getcwd()
    else:
        file_dir = path
    print("即将在{}下读取文件".format(file_dir))
    mfiles = []
    for root,dirs,files in os.walk(file_dir):
#        print(root)
        #忽略old文件夹内的文件
        if root == file_dir + "\\old":
            continue
        for i in files:
            for k in kind:
                #筛选文件类型，有待改进
                if i[-3:] == k[-3:]:
                    t = "%s\%s"%(root,i)
                    mfiles.append(t)
    print(mfiles)
    return mfiles
    
def writeInMongo(dbname,colname,res):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[dbname]
    mycol = mydb[colname]
    x = mycol.insert_many((res))
    try:
        x = mycol.insert_many(eval(str(al)))
    except:
        pass
    print("success! %s messages have been inserted"%x)
    
threadLock = threading.Lock()
class myThread(threading.Thread):
    global threadLock
    def __init__(self,x):
        threading.Thread.__init__(self)
        self.x = x

    def run(self):
        #print("开启线程："+self.name)
        threadLock.acquire()
        x_parse(self.x)
        threadLock.release()
        
class Item(object):
    def __init__(self,mark1="",mark2="",mark3="",mark4="",mark5="",mark6="",mark7="",mark8="",mark9="",mark10="",time="",msg="",orimsg=""):
        super(Item,self).__init__()
        self.mark1 = mark1
        self.mark2 = mark2 
        self.mark2 = mark2 
        self.mark3 = mark3 
        self.mark4 = mark4 
        self.mark5 = mark5 
        self.mark6 = mark6 
        self.mark7 = mark7 
        self.mark8 = mark8 
        self.mark9 = mark9 
        self.mark10 = mark10
        self.time = time
        self.msg = msg
        self.orimsg = orimsg
        #拼成id 随机生成时分秒
        self._id = time+str(random.randint(0,59))+str(random.randint(0,59))+str(random.randint(0,99))
    def setid(self,id):
        self._id = id
    def setmark1(self,mark):
        self.mark1 = mark
    def setmark2(self,mark):
        self.mark2 = mark
    def setmark3(self,mark):
        self.mark3 = mark
    def setmark4(self,mark):
        self.mar4 = mark
    def setmark5(self,mark):
        self.mark5 = mark
    def setmark6(self,mark):
        self.mark6 = mark
    def setmark7(self,mark):
        self.mark7 = mark
    def setmark8(self,mark):
        self.mark8 = mark
    def setmark9(self,mark):
        self.mark9 = mark
    def setmark10(self,mark):
        self.mark10 = mark
    def settime(self,time):
        self.time = time
    def setmsg(self,msg):
        self.msg = msg
    def setorimsg(self,msg):
        self.orimsg = msg
    def getjson(self):
        return '{"_id":"%s","time":"%s","mark1":"%s","mark2":"%s","mark3":"%s","mark4":"%s","mark5":"%s","mark6":"%s","mark7":"%s","mark8":"%s","mark9":"%s","mark10":"%s","msg":"%s","orimsg":"%s"}'%(self._id,self.time,self.mark1,self.mark2,self.mark3,self.mark4,self.mark5,self.mark6,self.mark7,self.mark8,self.mark9,self.mark10,self.msg,self.orimsg)

