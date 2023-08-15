import csv
import os
import pandas as pd
import testdbc
import mespdata
import readdbc_alldata
import basicf
import resultup
#__author__ = 'ChengDH'
#[[[index],[massages id spi]],[[name],[size]],[[name],[size]]......]  首先匹配massages id 然后得到一个下标，找到对应的index 跳到index对应的子列表 利用下标跳转 然后数据拆分，在使用的时候可以先建一个
#存储列表  比如 匹配的d3在massage下标为5，则找到大列表中下标为5+1的子列表lista[namesize]],这个时候外部会传入一个list，新建lisdata=[0for i in range(len(lista)] 然后替换值  加入number计算目前list的动态位置，利用listdata。appen
def analysis_data(a,b,index_of,arg3,arg4):#一共41个#b是正文开始的字节 a是服务号
    if arg4=="0":
        if len(a)>0 and a[0] in mespdata.ID_SPI and mespdata.ID_SPI.index(a[0])<len(mespdata.Index_ALL) :
            str1=mespdata.ID_SPI.index(a[0])
            alldata=[[],[],[],[]]#Name Resolution Offset Size
            for i in range(len(readdbc_alldata.all_msg_name[str1])):
                alldata[0].append(readdbc_alldata.all_msg_name[str1][i][0])
                alldata[1].append(readdbc_alldata.all_msg_name[str1][i][1][4])
                alldata[2].append(readdbc_alldata.all_msg_name[str1][i][1][5])
                alldata[3].append(readdbc_alldata.all_msg_name[str1][i][1][1])
            niubinumber=0
            newdata=basicf.turn0x(b)
            Namelist=alldata[0]
            Resolutionlist=alldata[1]
            Offsetlist=alldata[2]
            Sizelist=alldata[3]
            jiexis=[]
            for i in range(len(Sizelist)):
                jiexi=[]
                jiexi.append(Namelist[i])
                jiexi.append(basicf.jiexif(niubinumber,Resolutionlist[i],Offsetlist[i],Sizelist[i],newdata))
                niubinumber+=Sizelist[i]
                jiexis.append(jiexi)
            row_count = len(jiexis)
            # 打开CSV文件，使用newline=''参数以避免空行被自动插入
            with open(f'{arg3}\\result\\{a[0]}\\{index_of}.csv', 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                row_data = ["Signal Name：", "Analysis Result："]
                csvwriter.writerow(row_data)
                # 遍历每一行并写入CSV文件
                for j in range(row_count):
                    # 构造要写入CSV文件的数据

                    row_data = [f"{jiexis[j][0]}", float(f"{jiexis[j][1]}")]
                    # 写入一行数据到CSV文件
                    csvwriter.writerow(row_data)
    else:
        if len(a) > 0 and a[0] in mespdata.ID_SPI and mespdata.ID_SPI.index(a[0]) < len(mespdata.Index_ALL):
            str1 = mespdata.ID_SPI.index(a[0])
            alldata = [[], [], [], []]  # Name Resolution Offset Size
            for i in range(len(testdbc.all_msg_name1[str1])):
                alldata[0].append(testdbc.all_msg_name1[str1][i][0])
                alldata[1].append(testdbc.all_msg_name1[str1][i][1][4])
                alldata[2].append(testdbc.all_msg_name1[str1][i][1][5])
                alldata[3].append(testdbc.all_msg_name1[str1][i][1][1])
            niubinumber = 0
            newdata = basicf.turn0x(b)
            Namelist = alldata[0]
            Resolutionlist = alldata[1]
            Offsetlist = alldata[2]
            Sizelist = alldata[3]
            jiexis = []
            for i in range(len(Sizelist)):
                jiexi = []
                jiexi.append(Namelist[i])
                jiexi.append(basicf.jiexif(niubinumber, Resolutionlist[i], Offsetlist[i], Sizelist[i], newdata))
                niubinumber += Sizelist[i]
                jiexis.append(jiexi)
            row_count = len(jiexis)
            # 打开CSV文件，使用newline=''参数以避免空行被自动插入
            with open(f'{arg3}\\result\\{a[0]}\\{index_of}.csv', 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                row_data = ["Signal Name：", "Analysis Result："]
                csvwriter.writerow(row_data)
                # 遍历每一行并写入CSV文件
                for j in range(row_count):
                    # 构造要写入CSV文件的数据

                    row_data = [f"{jiexis[j][0]}", float(f"{jiexis[j][1]}")]
                    # 写入一行数据到CSV文件
                    csvwriter.writerow(row_data)