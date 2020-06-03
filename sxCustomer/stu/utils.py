import pandas as pd
import numpy as np
from configparser import ConfigParser as conf


def check_phone(cc):
    file_columns = {}
    for i in cc:
        if not len(i.split(':')) > 1: continue
        k = i.split(':')[0].__str__().strip()
        v = i.split(':')[1].__str__().strip()
        file_columns[k] = v

    if not 'phone' in file_columns.keys():
        print('转换字段import_file_column中没有配置phone字段，无法导入。正在退出导入，3秒')
        return
    return file_columns

def get_params():
    cc = conf.get('sales_file_import', 'file_colnums').__str__().split(',')
    db_columns = {}
    params = {}
    for i in cc:
        if not len(i.split(':')) > 1: continue
        k = i.split(':')[0].__str__().strip()
        v = i.split(':')[1].__str__().strip()
        db_columns[k] = v
        params[k] = v

    return params,db_columns

def get_df(file_path,s=0):
    try:
        try:
            df = pd.read_excel(file_path, encoding='utf-8',sheet_name=s)
        except Exception as e:

            df = pd.read_excel(file_path, encoding='gbk',sheet_name=s)
    except:
        try:
            df = pd.read_csv(file_path, encoding='utf-8',sheet_name=None)
        except:
            df = pd.read_csv(file_path, encoding='gbk')
    df.replace(np.nan, '', inplace=True)

    return df

def for_update(datas,file_path,params,file_columns,db_columns,func,source,new_name):

    for index, row in datas.iterrows():
        # 清空参数
        for k, v in params.items():
            params[k] = None
        for colnum in row.index:
            value = row[colnum]
            db_col = ''
            # 必须在文件import_file_column 列表中才能导入
            for k, v in file_columns.items():
                if colnum.strip() == v.strip():
                    db_col = k.strip()
                    break
            # 必须在文件db_columns 列表中才能导入
            if not db_col in db_columns.keys():
                continue
            params[k] = value

        params['phone'] = str(params['phone'])
        if params['phone'] and len(str(params['phone'])) == 11:
             params['source'] = source
             params['jianli'] = new_name
             func(params,index+1,file_path)


