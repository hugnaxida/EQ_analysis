import mespdata
import pandas as pd
#import pandas as pd
#f'{arg3}\\各项合并结果\\{mespdata.Index_ALL[j]}.xlsx'
# 读取Excel文件并转换为DataFrame
def lastturn(arg3):
    for j in range(len(mespdata.ID_SPI)):
        df = pd.read_excel(f'{arg3}\\各项合并结果\\{mespdata.Index_ALL[j]}.xlsx')
        # 创建一个新的DataFrame来保存转换后的数据
        new_df = pd.DataFrame()
        # 遍历原始DataFrame的每一行
        for index, row in df.iterrows():
            if not row.isnull().all():  # 判断是否该行全部为空
                # 将每一行的数据转置为一列
                transposed_row = pd.DataFrame(row.values.reshape(-1, 1))

                # 将转置后的数据添加到新DataFrame中
                new_df = pd.concat([new_df, transposed_row], axis=1)
        # 将转换后的数据保存为Excel文件
        new_df.to_excel(f'{arg3}\\各项合并结果\\{mespdata.Index_ALL[j]}.xlsx', index=False)

