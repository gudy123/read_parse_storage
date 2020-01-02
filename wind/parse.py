import sys
sys.path.append(r"E:\和信\导入信息\mylib")
import mylib
import random

def x_parse(path):
    data = []
    with open(path,"r",encoding="utf-8") as f:
        lines = f.read().split("\n")
    xtime = lines[0][-12:-1]
    for line in lines:
        if len(line) > 0 and line[0] == '◆':
            data.append(line)
    res = []
    for x in data:
        item = mylib.Item()
        item.setmsg(x)
        item.settime(xtime)
        item.setid(xtime.replace("年","").replace("月","").replace("日","")+str(random.randint(0,59))+str(random.randint(0,59))+str(random.randint(0,99)))
        
        res.append(eval(item.getjson()))
    #print(res)
    mylib.writeInMongo("wind","instruction",res)
    
    
def main():
    #读取文件
    mfiles = mylib.readFiles(kind="txt")
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