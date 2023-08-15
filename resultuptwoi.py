import os
#__author__ = 'ChengDH'
import mespdata
import resultup
import pandas as pd
import getdbc

def end(arg3):
    for j in range(len(mespdata.ID_SPI)):
        # 文件夹路径
        folder_path = f"{arg3}\\result\\{mespdata.ID_SPI[j]}"
        # 获取文件夹下的所有CSV文件
        csv_files = sorted([file for file in os.listdir(folder_path) if file.endswith('.csv')])
        # 创建一个空的DataFrame列表
        merged_data_list = []
        # 遍历每个CSV文件并逐行合并
        for i, file in enumerate(csv_files):
            # 构造完整的文件路径
            file_path = os.path.join(folder_path, file)
            # 读取CSV文件内容
            with open(file_path, 'r', encoding='gbk') as f:
                lines = f.readlines()
            # 提取每一行的数据
            if i == 0:
                # 读入第一个CSV文件的全部内容（包括表头）
                column_data1 = [line.strip().split(',')[0] for line in lines]
                merged_data_list.append(column_data1)
                column_data = [line.strip().split(',')[1] for line in lines]
            else:
                # 仅读取第二列数据
                column_data = [line.strip().split(',')[1] for line in lines]
            # 将数据添加到合并的DataFrame列表中
            merged_data_list.append(column_data)
        # 合并所有的行到一个DataFrame中
        merged_data = pd.DataFrame(merged_data_list).T
        # 将除表头行外的所有数据尝试转换为数字，无法解析为数字的值保留为字符串
        merged_data.iloc[1:] = merged_data.iloc[1:].apply(pd.to_numeric, errors='ignore')
        # 如果文件夹下没有CSV文件，则生成指定名称的xlsx文件
        if len(csv_files) == 0:
            merged_data = pd.DataFrame({'No Data': ['No Data']})
        # 写入到Excel文件中
        file_name = f'{arg3}\\各项合并结果\\{mespdata.Index_ALL[j]}.xlsx'
        merged_data.to_excel(file_name, index=False)