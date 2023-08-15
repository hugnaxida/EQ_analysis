import pandas as pd
import os


def process_files(arg3):
    folder_path = os.path.join(arg3, "各项合并结果")
    output_folder = os.path.join(arg3, "数据最终合并文件")

    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # 只处理后缀为xlsx或xls的文件
        if not (file_path.endswith(".xlsx") or file_path.endswith(".xls")):
            continue

        # 读取Excel文件
        df = pd.read_excel(file_path)

        # 确定包含ID的列名
        id_column = None
        for column in df.columns:
            if "ID" in str(df[column].iloc[0]):
                id_column = column
                break

        if id_column is None:
            continue

        # 将ID列数据类型转换为数值类型，保留不能转换为数值的字符串值
        df[id_column] = pd.to_numeric(df[id_column], errors='ignore')

        # 根据ID列的值进行判断
        is_ordered = True
        prev_value = None
        remove_indices = []
        for i, value in enumerate(df[id_column]):
            if isinstance(value, str):  # 检查值的类型
                continue  # 如果值是字符串，则跳过减法操作

            if prev_value is not None and value - prev_value != 1:
                is_ordered = False
                remove_indices.append(i)  # 记录需要删除的行索引
            prev_value = value

        # 删除不按顺序的行
        df = df.drop(remove_indices)

        # 将不按顺序的数据添加在最下面
        ordered_data = pd.DataFrame(
            data=[[value] for value in df[id_column] if value not in remove_indices],
            columns=[id_column]
        )
        df = pd.concat([df, ordered_data], ignore_index=True)

        # 保存修改后的文件
        modified_file_name = file_name
        modified_file_path = os.path.join(output_folder, modified_file_name)
        df.to_excel(modified_file_path, index=False)