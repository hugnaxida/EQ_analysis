import basicf

import analysis
#__author__ = 'ChengDH'

def analysis_mesp_06_function_03(listc, listd,index_of,arg3,arg4):
    number = 0  # 当前解析到的坐标
    number_02=0
    if basicf.getint0x(listc[0]) >= 80:  # 最高位为1，则进行的是回复操作，进行回复的解析
        if listc[0]!='80':
            ret = listd[0:4]
            number += 4
            ct_type = [listd[number]]
            number += 1
            ct_vision = [listd[number]]
            number += 1
            ct_stage = [listd[number]]
            number += 1
            Reserved6 = [listd[number]]
            number += 1
            ct_params_num = listd[number:number + 2]
            params_long = ''
            for params_longs in range(len(ct_params_num)):
                params_long += ct_params_num[params_longs]
            basicf.get_number_of_params(params_long)  # 计算参数的个数
            number += 2
            Reserved7 = listd[number:number + 2]
            number += 2
            ct_crc = listd[number:number + 4]
            number += 4
            number += 20  # 跳过热server-5
            params = listd[number:]
            params_max = ''
            for i_p in range(4):
                params_max += params[i_p]
            basicf.get_long_of_params(params_max,number_02)  # 计算参数字段的大小
            paramss = listd[number + 4:]
            analysis.analysis_data(ct_stage, paramss,index_of,arg3,arg4)  # 解析函数，mesp和mecom都可以使用

    else:  # 进行的是请求操作，进行请求的解析
        ct_type = [listd[number]]
        number += 1
        ct_vision = [listd[number]]
        number += 1
        ct_stage = [listd[number]]
        number += 1
        Reserved6 = [listd[number]]
        number += 1
        ct_params_num = listd[number:number + 2]
        params_long = ''
        ct_params_num.reverse()
        for params_longs in range(len(ct_params_num)):
            params_long += ct_params_num[params_longs]
        basicf.get_number_of_params(params_long)  # 计算参数的个数
        number += 2
        Reserved7 = listd[number:number + 2]
        number += 2
        ct_crc = listd[number:number + 4]
        number += 4
        number += 20  # 跳过热server-5
        params = listd[number:]
        params_max = ''
        size=params[0:4]
        size.reverse()
        for i_p in range(4):
            params_max += size[i_p]
        basicf.get_long_of_params(params_max,number_02)  # 计算参数字段的大小
        paramss=listd[number+4:]
        analysis.analysis_data(ct_stage,paramss,index_of,arg3,arg4)#解析函数，mesp和mecom都可以使用


def mencomanal(ct_stage,paramss,index_of,arg3,arg4):
    analysis.analysis_data(ct_stage, paramss,index_of,arg3,arg4)