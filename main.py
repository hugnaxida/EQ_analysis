import csv
import os
import test
import mespfunction
import analysis
import readdbc_alldata
import getdbc
import basicf
import mespdata
import resultup
import resultuptwoi
import sys
import testdbc
import testfor
import tkinter as tk
from tkinter import messagebox

def show_complete_message():
    root = tk.Tk()
    root.geometry("300x200")  # 设置弹窗的宽度和高度
    root.title("made--by--chengdenghe")  # 设置弹窗的标题
    #root.iconbitmap("icon.ico")  # 设置弹窗的图标（icon.ico是自定义的图标文件路径）
    label = tk.Label(root, text="程序已经分析完成", font=("Arial", 16))
    label.pack(pady=50)

    root.mainloop()
# 在适当的位置调用函数来展示提示弹窗

#__author__ = 'ChengDH'
class mesp:
    number=0
    index_of=''
    protocol=[]
    service=[]
    function=[]
    msgtag=[]
    datalists=[]
    spi_DR = []
    spi_RSP_NUM = []
    spi_CRC = []
    TP_head = []
    TP_single_size = []  # flog=0
    TP_single_appid = []  # flog=0
    TP_msgid = []  # flog=1
    TP_total = []  # flog=1
    TP_appid = []  # flog=1
    TP_msgids = []  # flog=2
    def __init__(self, datalist,a,b,c,d,e,f,g,h,i,j,k):#mesp类初始化函数
        self.index_of=k
        self.number=0
        self.protocol=[datalist[0]]
        self.service=[datalist[1]]
        self.function=[datalist[2]]
        self.msgtag=[datalist[3]]
        self.datalists=datalist[4:]
        self.spi_DR=a
        self.spi_RSP_NUM=b
        self.spi_CRC = c
        self.TP_head = d
        self.TP_single_size =e # flog=0
        self.TP_single_appid =f  # flog=0
        self.TP_msgid = g # flog=1
        self.TP_total =h  # flog=1
        self.TP_appid =i  # flog=1
        self.TP_msgids =j  # flog=2
class mecom:#mencom类
    index_of=''
    spi_DR = []
    comhead = []#00 单帧   #01   首帧  #02  多帧
    TP_single_size = []  # flog=0   单帧+长度
    TP_single_appid = []  # flog=0   状态符号 1个字节 data
    TP_msgid = []  # flog=1
    TP_total = []  # flog=1
    TP_appid = []  # flog=1
    TP_msgids = []  # flog=2
    datall=[]
    def __init__(self,a0,a,b,c,d,e,f,g,h,i):
        self.index_of=i
        self.spi_DR=a0
        self.comhead=a
        self.TP_single_size=b
        self.TP_single_appid=c
        self.TP_msgid=d
        self.TP_total=e
        self.TP_appid=f
        self.TP_msgids=g
        self.datall=h
    def adddatall(self,list_1):
        self.datall=list_1
    def appid(self):
        self.TP_appid=self.TP_single_appid
class spi:#spi类，实现最简单的分类分析
    flog=0#0代表单帧，1代表首帧，2代表多帧,3代表错误信息
    spi_DR=[]
    spi_RSP_NUM=[]
    spi_CRC=[]
    TP_head=[]
    TP_single_size=[]#flog=0
    TP_single_appid = []#flog=0
    TP_msgid=[]#flog=1
    TP_total = []#flog=1
    TP_appid=[]#flog=1
    TP_msgids = []#flog=2
    Mesp=[]
    Mecom=[]
    nmuber=0 #计算TP头部加spi头部在一起的长度，以此来推算出MESP/MECOM头部的信息
    datalists=[]#存储运输的数据
    def __init__(self,datalist):#spi类初始化函数
        if len(datalist) >=13:
            self.spi_DR=[datalist[0]]

            self.spi_RSP_NUM =[datalist[1]]+[datalist[2]]+[datalist[3]]
            self.spi_CRC = [datalist[4]]+[datalist[5]]
            if datalist[6]=='00':#单帧 按照单帧的格式进行分割
                self.flog=0
                self.TP_head = [datalist[6]]
                self.TP_single_size=[datalist[7]]
                self.TP_single_appid=[datalist[8]]
                self.number=9
            elif datalist[6]=='01':
                self.flog=1
                self.TP_head = [datalist[6]]
                self.TP_msgid = [datalist[7]]  # flog=1
                self.TP_total = [datalist[8]]+[datalist[9]]+[datalist[10]]+[datalist[11]] # flog=1
                self.TP_appid = [datalist[12]]  # flog=1
                self.number=12
            elif datalist[6] == '02':
                self.flog=2
                self.TP_head = [datalist[6]]
                self.TP_msgids = [datalist[7]]  # flog=2
                self.number=8
            else:
                flog=3
            if datalist[self.number]=='5E' and datalist[6]=='00':
                self.Mesp='5E'
            else:
                self.Mecom = [datalist[self.number]]
            self.number+=1
            for i in range(self.number,len(datalist)):
                self.datalists = self.datalists+[datalist[i]]

def analysis_mesp_06_function(listb,listc,listd,index_of,arg3,arg4):
    if listb==['01']:
        0
    elif listb==['02']:
        0
    elif listb==['03']:
        mespfunction.analysis_mesp_06_function_03(listc, listd,index_of,arg3,arg4)
    else:
        print("mesp解析出错,service-06-没有对应的功能号")
#分析mesp的service
def analysis_mesp_service(lista,listb,listc,listd,index_of,arg3,arg4):#lista代表service号，listb代表function号，listc代表rep/qep（大于等于80则是回复，小于80则是request，listd代表mesp的data
    if lista==['0C']:
        0
    elif lista==['06']:
        analysis_mesp_06_function(listb,listc,listd,index_of,arg3,arg4)
    else:
        print("mesp解析出错,没有对应的服务号")
arg1 = ''
arg2 = ''
arg3 = ''
arg4=''
def main():
    global arg1, arg2, arg3,arg4
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    arg4 = sys.argv[4]

    print(arg1,arg2,arg3,arg4)

    print("程序开始处理信息---------------")
    # 在这里添加其他的逻辑操作
#folder_path_input=input("请输入存放dbc文件的文件夹,dbc中含有状态信息：\n")
#file_input_path_data=input("请输入需要解析的文件的地址：--------比如：GSR_replace_file_EQ_spi.csv\n")
#file_path_data_wenjianjia = input("请输入需要生成的所有结果文件夹的地址：\n")

if __name__ == '__main__':
    main()
    print("\n")
    print("\n")
    print("-----------------made       by       chengdenghe -------------")
    print("\n")
    print("\n")
    print("程序开始处理信息---------------")
    datalist = []
    indexlist = []
    if arg4=="0":
        print("\n")
        print("dbc参数为0，重新读入数据库数据，如果你想读取序列化数据，请将参数4置为1-----------------")
        getdbc.getdbc(arg1)
        readdbc_alldata.readdbc_()
        testdbc.testdbcin(arg1)
    else:
        testdbc.testdbcout(arg1)
        print("\n")
        print("dbc数据为1，读取序列化数据，如果你想重新读取数据库数据，请将参数4置为0-------------")
    mespdata.mespdata(arg4)
    resultup.resultup(arg3)
    with open(arg2,'r') as file:  # 读原始数据  GSR_replace_file_EQ_spi.csv(EQ端     GSR_replcae_file_MCU_spi.csv mcu端
        reader = csv.reader(file)
        start_reading = False  # 用于标记是否开始读取
        for row in reader:
            if len(row) >= 5 and row[4] == '128 B':  # 检查第五个值是否为特定值
                start_reading = True

            if len(row) >= 7 and start_reading:
                datalist.append(row[7].split())  # 添加需要的数据
                indexlist.append(row[1])
    # 数据区域
    datalistlast = []  # 存放所有的数据emsp+emcom
    datalistmesp = []  # 存放emsp
    datalistmespanalysis = []  # 存放与datalistmesp对应的数据
    datalistmecom = []  # 存放emcom
    datalistmecom_08 = []  # 存放emcom
    for i in range(len(datalist)):  # 进行数据分组
        testi = spi(datalist[i])
        datalistlast.append(testi)
        if testi.Mesp == '5E':
            datalistmesp.append(
                mesp(['5E'] + testi.datalists, testi.spi_DR, testi.spi_RSP_NUM, testi.spi_CRC, testi.TP_head,
                     testi.TP_single_size, testi.TP_single_appid, testi.TP_msgid, testi.TP_total, testi.TP_appid,
                     testi.TP_msgids, indexlist[i]))
        else:
            datalistmecom.append(
                mecom(testi.spi_DR, testi.TP_head, testi.TP_single_size, testi.TP_single_appid, testi.TP_msgid,
                      testi.TP_total, testi.TP_appid, testi.TP_msgids, testi.Mecom + testi.datalists, indexlist[i]))
    for i in range(len(datalistmecom)):
        if datalistmecom[i].spi_DR == ['08']:
            datalistmecom_08.append(datalistmecom[i])
    # 首先将datalistlast中的所有数据放在一个二次列表中，然后利用这个列表进行输出
    datalists1 = [
        ["spiDR头", "spi_RSP_NUM", "spi-CRC较捡码", "帧的类型（0-单帧，1-首帧，2-多帧）", "TP_single_size", "TP_single_appid", "TP_msgid",
         "TP_total", "TP_appid", "TP_msgids", "Mesp", "Mecom", "报文内容"]]
    datalists1 += [
        [spi.spi_DR, spi.spi_RSP_NUM, spi.spi_CRC, spi.TP_head, spi.TP_single_size, spi.TP_single_appid, spi.TP_msgid,
         spi.TP_total, spi.TP_appid, spi.TP_msgids, spi.Mesp, spi.Mecom, spi.datalists] for spi in datalistlast]
    # 首先将datalistmesp中的所有数据放在一个二次列表中，然后利用这个列表进行输出
    datalist2 = [
        ["spiDR头", "spi_RSP_NUM", "spi-CRC较捡码", "帧的类型（0-单帧，1-首帧，2-多帧）", "TP_single_size", "TP_single_appid", "TP_msgid",
         "TP_total", "TP_appid", "TP_msgids", "mesp_protocol", "mesp_service", "mesp_function", "mesp_msg-tag", "报文内容"]]
    datalist2 += [
        [spi.spi_DR, spi.spi_RSP_NUM, spi.spi_CRC, spi.TP_head, spi.TP_single_size, spi.TP_single_appid, spi.TP_msgid,
         spi.TP_total, spi.TP_appid, spi.TP_msgids, spi.protocol, spi.service, spi.function, spi.msgtag, spi.datalists]
        for spi in datalistmesp]
    datalist3 = [
        ["spiDR头", "帧的类型（0-单帧，1-首帧，2-多帧）", "TP_single_size", "TP_single_appid", "TP_msgid", "TP_total", "TP_appid",
         "TP_msgids", "报文内容"]]
    datalist3 += [
        [spi.spi_DR, spi.comhead, spi.TP_single_size, spi.TP_single_appid, spi.TP_msgid, spi.TP_total, spi.TP_appid,
         spi.TP_msgids, spi.datall] for spi in datalistmecom_08]
    with open(f"{arg3}\\报文详细分析\\all.csv", 'w', newline='') as file:  # 输出all mesp+mecom
        writer = csv.writer(file)
        writer.writerows(datalists1)
    # file_path_mesp=input("请输入mesp文件所需要保存的地址(包含spi报头和TP报头)：---------------------------")
    with open(f"{arg3}\\报文详细分析\\mesp.csv", 'w', newline='') as file:  # 输出mesp
        writer = csv.writer(file)
        writer.writerows(datalist2)
    # file_path_mecom=input("请输入mecom文件所需要保存的地址：-------------------------")
    # 分析mesp的service
    print("\n")
    print("开始解析mecsp：--------------")
    for i in range(len(datalistmesp)):
        analysis_mesp_service(datalistmesp[i].service, datalistmesp[i].function, datalistmesp[i].msgtag,
                              datalistmesp[i].datalists, datalistmesp[i].index_of,arg3,arg4)
    listmecom = []  # [i][1]    [i][8]
    listflag = []
    flognum = datalistmecom_08[0]
    for i in range(len(datalistmecom_08)):
        if datalistmecom_08[i].comhead == ['00']:
            listflag = []
            listmecom.append(datalistmecom_08[i])
        elif datalistmecom_08[i].comhead == ['01']:
            flognum = datalistmecom_08[i]
            listflag = datalistmecom_08[i].datall
        else:
            if i < len(datalistmecom_08) - 1 and datalistmecom_08[i + 1].comhead != ['02']:
                listflag += datalistmecom_08[i].datall
                flognum.adddatall(listflag)
                #flognum.appid()
                listmecom.append(flognum)
            elif i == len(datalistmecom_08) - 1:
                listflag += datalistmecom_08[i].datall
                flognum.adddatall(listflag)
                #flognum.appid()
                listmecom.append(flognum)  # cd ./EQW-analysis.spec
            else:
                listflag += datalistmecom_08[i].datall
    # listmecom  mencome的结果
    datalist4 = [
        ["spiDR头", "帧的类型（0-单帧，1-首帧，2-多帧）", "TP_single_size", "TP_single_appid", "TP_msgid", "TP_total", "TP_appid",
         "TP_msgids", "报文内容"]]
    datalist4 += [
        [spi.spi_DR, spi.comhead, spi.TP_single_size, spi.TP_single_appid, spi.TP_msgid, spi.TP_total, spi.TP_appid,
         spi.TP_msgids, spi.datall] for spi in listmecom]
    # file_path_mecom_mecom=input("请输入mecom文件所需要保存的地址(不包含spi报头和TP报头)：---------------------------")
    with open(f"{arg3}\\报文详细分析\\mecom.csv", 'w', newline='') as file:  # 输出mecom
        writer = csv.writer(file)
        writer.writerows(datalist4)
    # print("test-------------------mecom")
    print("\n")
    print("开始解析mecom：--------------")
    for i in range(len(listmecom)):
        mespfunction.mencomanal(listmecom[i].TP_single_appid, listmecom[i].datall, listmecom[i].index_of,arg3,arg4)
    # 具体的代码逻辑
    print("\n")
    print("开始合并数据·~~~~~````请稍后...................................")
    resultuptwoi.end(arg3)
    # 程序执行完毕后，等待用户输入任意内容终止程序
    print("\n")
    print("删除文件夹result，运行正在进行中....开始横纵坐标倒转.....请稍后......")
    resultup.resultlast(arg3)
    test.lastturn(arg3)
    print("\n")
    print("正在检查文件顺序...............请稍后............................")

    testfor.process_files(arg3)
    print("\n")
    print("\n")
    print("\n")
    print("运行结束...succeessful......运行成功！...........运行结束..........\n")
    show_complete_message()

datalistmespanalysis