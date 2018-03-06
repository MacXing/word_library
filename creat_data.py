import numpy as np
import os
import pandas as pd
import pypinyin
from itertools import chain

def open_dirs(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            read_xlsx(os.path.join(root, name),name)
        # for name in dirs:
        #     print(os.path.join(root, name))


def read_xlsx(filename,name):
    a = pd.read_excel(filename)
    a['process_cat']=0
    name = name.split('.')[0]
    a['resource']=name
    a['word_pinyin']=''
    # print(a['resource'])
    for d in range(len(a)):
        if pd.notnull(a.loc[d,'Id']):
            a.loc[d:,'process_cat']=a.loc[d,'Id']
        if pd.notnull(a.loc[d,'同义词']):
            a.loc[d,'word_pinyin'] =','.join(chinese_pinyin(a.loc[d,'同义词']))
        elif pd.notnull(a.loc[d,'词类名']):
            a.loc[d,'word_pinyin'] =','.join(chinese_pinyin(a.loc[d,'词类名']))

    # print(a['process_cat'])
    save_csv(a,name)

def save_csv(a,name):
    #
    a.to_csv("C:\\Users\\User\\Desktop\\"+name+'.csv', index=False)

def chinese_pinyin(content):
    result=pypinyin.pinyin(content)
    result=list(chain(*result))
    return(result)


if __name__ == '__main__':
    open_dirs('C:\\Users\\User\\Desktop\\贵阳项目词库')
    # read_xlsx()
    # print(chinese_pinyin('贵阳项目词库'))