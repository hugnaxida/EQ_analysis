import os
#__author__ = 'ChengDH'
#folder_path_input=input("请输入存放dbc文件的文件夹,dbc中含有状态信息：\n")
#file_input_path_data=input("请输入需要解析的文件的地址：--------比如：GSR_replace_file_EQ_spi.csv\n")
#file_path_data_wenjianjia = input("请输入需要生成的所有结果文件夹的地址：\n")
dbc_files_input=[]
def getdbc(arg1):
    print("开始读入数据库")
    global dbc_files_input
    dbc_files_input = [file for file in os.listdir(arg1) if file.endswith('.dbc')]
    for i in range(len(dbc_files_input)):
        dbc_files_input[i]=arg1+'\\'+dbc_files_input[i]