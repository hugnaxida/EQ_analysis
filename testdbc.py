import pickle
import os
import readdbc_alldata
# 假设你有一个包含字符数组和小数组的大数组
all_msg_name_find1=[]
all_msg_name1=[]
def testdbcin(arg1):
    # 序列化并保存到文件
    list1=readdbc_alldata.all_msg_name_find[:]
    list2=readdbc_alldata.all_msg_name[:]
    with open(f"{arg1}\\all_msg_name_find.pkl", "wb") as file:
        pickle.dump(list1, file)
    with open(f"{arg1}\\all_msg_name.pkl", "wb") as file:
        pickle.dump(list2, file)
    # 检查文件是否存在以及是否包含数据
def testdbcout(arg1):
    global all_msg_name1,all_msg_name_find1
    if os.path.isfile(f"{arg1}\\all_msg_name_find.pkl"):
        # 反序列化并加载数据
        with open(f"{arg1}\\all_msg_name_find.pkl", "rb") as file:
            all_msg_name_find1 = pickle.load(file)
    else:
        # 如果文件不存在或者没有数据，则创建新的数组
        print("您这是第一次读入数据，请将参数4置为0，读取数据库")
    if os.path.isfile(f"{arg1}\\all_msg_name.pkl"):
        # 反序列化并加载数据
        with open(f"{arg1}\\all_msg_name.pkl", "rb") as file:
            all_msg_name1 = pickle.load(file)
    else:
        # 如果文件不存在或者没有数据，则创建新的数组
        print("您这是第一次读入数据，请将参数4置为0，读取数据库")