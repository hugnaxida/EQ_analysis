import cantools
from cantools.database import Message
import getdbc
from tqdm import tqdm
import time
#from logutil import Logs
#__author__ = 'ChengDH'
dbcflog=[]
class DbcAnalize():
    def __init__(self, dbc_path):
        # 加载dbc文件
        try:
            dbs = cantools.database.load_file(dbc_path)
        except Exception as e:
            print('%s: %s' % (e.__class__.__name__, e))
            return False
        self.dbs = dbs
        self.messages = self.dbs.messages

    def get_msg_info_all(self):
        message_dict = {}
        message_dict_list=[]
        message_list = []
        for msg in self.messages:
            msg_name = msg.name
            msg_id = msg.frame_id
            msg_id = '0x%X' % msg_id
            msg_len = msg.length
            msg_cycle = msg.cycle_time
            msg_sender = msg.senders
            #message_list.append(msg_id)
            message_list.append(msg_len)
            message_list.append(msg_cycle)
            message_list.append(msg_sender)
            message_dict[msg_name] = message_list
            message_dict_list.append([msg_name,msg_id,message_list])
            message_list = []
        return message_dict_list

    def get_sig_info_all(self, filtmessage):
        signal_dict = {}
        signal_dict_list=[]
        signal_list = []
        for msg in self.messages:
            if msg.name == str(filtmessage):
                for item in msg.signals:

                    sig_name = item.name
                    sig_start = item.start
                    sig_len = item.length
                    sig_byte_order = item.byte_order
                    sig_signed = item.is_signed
                    factor = item.scale
                    offset = item.offset
                    s_min = item.minimum
                    s_max = item.maximum
                    unit = item.unit

                    signal_list.append(sig_start)
                    signal_list.append(sig_len)
                    signal_list.append(sig_byte_order)
                    signal_list.append(sig_signed)
                    signal_list.append(factor)
                    signal_list.append(offset)
                    signal_list.append(s_min)
                    signal_list.append(s_max)
                    signal_list.append(unit)

                    signal_dict[sig_name] = signal_list
                    signal_dict_list.append([sig_name,signal_list])
                    signal_list = []
        return signal_dict_list
all_msg_name_find=[]
all_msg_name=[]
def readdbc_():
    global all_msg_name_find,all_msg_name
#all_msg_name_find[i][0]代表所需要查找的名字，协议名称
#all_msg_name_find[i][1]代表服务号，用于匹配
#all_msg_name[i][0][0]单个分析项的名称
#all_msg_name[i][0][1][1]单个分析项的长度
#all_msg_name[i][0][1][4]单个分析项的乘法运算
#all_msg_name[i][0][1][5]单个分析项的加法运算
    print("开始进行数据库数据的读入:---------------")
    for i in tqdm(range(len(getdbc.dbc_files_input))):
        if getdbc.dbc_files_input[i]=="Core_Objects_protocol.dbc" or getdbc.dbc_files_input[i]=="Core_DRSD_protocol.dbc":
            print("特定数据库跳过读入，不影响结果计算------------------")
            continue
        else:
            print(getdbc.dbc_files_input[i])
            time.sleep(0.5)
            test = DbcAnalize(getdbc.dbc_files_input[i])
            testa = test.get_msg_info_all()
            for j in range(len(testa)):
                time.sleep(0.5)
                all_msg_name.append(test.get_sig_info_all(testa[j][0]))
                all_msg_name_find.append(testa[j])

    #至此所有数据均已读完
    print("\n")
    print("数据库读入over-----------------------")