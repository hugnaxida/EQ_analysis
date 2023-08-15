import readdbc_alldata
import testdbc
#__author__ = 'ChengDH'
Index_L=[]
modified_list=[]
ID_SPI=[]
Index_ALL=[]
def mespdata(arg4):
    global ID_SPI,Index_ALL,Index_L,modified_list
    if arg4=="0":
        for i in range(len(readdbc_alldata.all_msg_name_find)):
            modified_list.append(readdbc_alldata.all_msg_name_find[i][1])
            Index_L.append(readdbc_alldata.all_msg_name_find[i][0])
        ID_SPI = [item.replace('0x', '',) for item in modified_list]
        Index_ALL=[i for i in Index_L]
    else:
        for i in range(len(testdbc.all_msg_name_find1)):
            modified_list.append(testdbc.all_msg_name_find1[i][1])
            Index_L.append(testdbc.all_msg_name_find1[i][0])
        ID_SPI = [item.replace('0x', '',) for item in modified_list]
        Index_ALL=[i for i in Index_L]
