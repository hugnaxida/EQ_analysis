import mespdata
import os
import shutil
#__author__ = 'ChengDH'
def resultup(arg3):
    result_folder = os.path.join(arg3, 'result')
    if os.path.exists(result_folder):
        shutil.rmtree(result_folder)
    os.mkdir(result_folder)

    for i in range(len(mespdata.ID_SPI)):
        sub_folder = os.path.join(result_folder, mespdata.ID_SPI[i])
        if  os.path.exists(sub_folder):
            shutil.rmtree(sub_folder)
        os.mkdir(sub_folder)

    merge_folder = os.path.join(arg3, '各项合并结果')
    if os.path.exists(merge_folder):
        shutil.rmtree(merge_folder)
    os.mkdir(merge_folder)
    merge_folder = os.path.join(arg3, '报文详细分析')
    if os.path.exists(merge_folder):
        shutil.rmtree(merge_folder)
    os.mkdir(merge_folder)
    merge_folder = os.path.join(arg3, '数据最终合并文件')
    if os.path.exists(merge_folder):
        shutil.rmtree(merge_folder)
    os.mkdir(merge_folder)
    print("\n")
    print("文件夹生成完成")
def resultlast(arg3):
    result_folder = os.path.join(arg3, 'result')
    if os.path.exists(result_folder):
        shutil.rmtree(result_folder)
