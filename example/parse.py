import sys
sys.path.append(r"mylib文件夹路径")
import mylib
import random

def x_parse(path):
    #读取文件数据
    pass
    #解析文件数据
    pass
    #存储文件数据
    pass
    
def main():
    #读取文件 制定你要分析的文件类型
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