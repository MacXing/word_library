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
            a.loc[d,'word_pinyin'] =''.join(chinese_pinyin(a.loc[d,'同义词']))
        elif pd.notnull(a.loc[d,'词类名']):
            a.loc[d,'word_pinyin'] =''.join(chinese_pinyin(a.loc[d,'词类名']))

    # print(a['process_cat'])
    save_csv(a,name)

def save_csv(a,name):
    #
    a.to_csv("C:\\Users\\User\\Desktop\\"+name+'.csv', index=False)

def chinese_pinyin(content):
    if '[' in content:
        content.replace('[','')
        content.replace(']','')
    result=number_pinyin(content)
    result=pypinyin.pinyin(result,style=pypinyin.NORMAL)
    result=list(chain(*result))
    result=','.join(result)
    if ',,' in result:
        result=result.replace(',,',',')
    result=result.upper()
    return(result)

def number_pinyin(pinyin_sentence):
    if('1' in pinyin_sentence):
      pinyin_sentence=pinyin_sentence.replace("1",",YI,")
    if('2' in pinyin_sentence):
      pinyin_sentence=pinyin_sentence.replace("2",",ER,")
    if('3' in pinyin_sentence):
      pinyin_sentence=pinyin_sentence.replace("3",",SAN,")
    if('4' in pinyin_sentence):
      pinyin_sentence=pinyin_sentence.replace("4",",SI,")
    if('5' in pinyin_sentence):
      pinyin_sentence=pinyin_sentence.replace("5",",WU,")
    if('6' in pinyin_sentence):
      pinyin_sentence=pinyin_sentence.replace("6",",LIU,")
    if('7' in pinyin_sentence):
      pinyin_sentence=pinyin_sentence.replace("7",",QI,")
    if('8' in pinyin_sentence):
      pinyin_sentence=pinyin_sentence.replace("8",",BA,")
    if('9' in pinyin_sentence):
      pinyin_sentence=pinyin_sentence.replace("9",",JIU,")
    if('0' in pinyin_sentence):
      pinyin_sentence=pinyin_sentence.replace("0",",LING,")

    pinyin_sentence=pinyin_sentence.replace(',,',',')
    if(pinyin_sentence[len(pinyin_sentence)-1]==','):
        pinyin_sentence=pinyin_sentence[0:len(pinyin_sentence)-1]
    if(pinyin_sentence[0]==','):
        pinyin_sentence=pinyin_sentence[1:len(pinyin_sentence)]

    return(pinyin_sentence)



# def number_pinyin(pinyin_sentence):
    # if ('1' == pinyin_sentence[len(pinyin_sentence)-1]):
    #     pinyin_sentence = pinyin_sentence.replace("1", ",YI")
    # if ('2' == pinyin_sentence[len(pinyin_sentence)-1]):
    #     pinyin_sentence = pinyin_sentence.replace("2", ",ER")
    # if ('3' == pinyin_sentence[len(pinyin_sentence)-1]):
    #     pinyin_sentence = pinyin_sentence.replace("3", ",SAN")
    # if ('4' == pinyin_sentence[len(pinyin_sentence)-1]):
    #     pinyin_sentence = pinyin_sentence.replace("4", ",SI")
    # if ('5' == pinyin_sentence[len(pinyin_sentence)-1]):
    #     pinyin_sentence = pinyin_sentence.replace("5", ",WU")
    # if ('6' == pinyin_sentence[len(pinyin_sentence)-1]):
    #     pinyin_sentence = pinyin_sentence.replace("6", ",LIU")
    # if ('7' == pinyin_sentence[len(pinyin_sentence)-1]):
    #     pinyin_sentence = pinyin_sentence.replace("7", ",QI")
    # if ('8' == pinyin_sentence[len(pinyin_sentence)-1]):
    #     pinyin_sentence = pinyin_sentence.replace("8", ",BA")
    # if ('9' == pinyin_sentence[len(pinyin_sentence)-1]):
    #     pinyin_sentence = pinyin_sentence.replace("9", "JIU")
    # if ('0' == pinyin_sentence[len(pinyin_sentence)-1]):
    #     pinyin_sentence = pinyin_sentence.replace("0", ",LING")

    # if('1' in pinyin_sentence):
    #   pinyin_sentence=pinyin_sentence.replace("1",",YI,")
    # if('2' in pinyin_sentence):
    #   pinyin_sentence=pinyin_sentence.replace("2",",ER,")
    # if('3' in pinyin_sentence):
    #   pinyin_sentence=pinyin_sentence.replace("3",",SAN,")
    # if('4' in pinyin_sentence):
    #   pinyin_sentence=pinyin_sentence.replace("4",",SI,")
    # if('5' in pinyin_sentence):
    #   pinyin_sentence=pinyin_sentence.replace("5",",WU,")
    # if('6' in pinyin_sentence):
    #   pinyin_sentence=pinyin_sentence.replace("6",",LIU,")
    # if('7' in pinyin_sentence):
    #   pinyin_sentence=pinyin_sentence.replace("7",",QI,")
    # if('8' in pinyin_sentence):
    #   pinyin_sentence=pinyin_sentence.replace("8",",BA,")
    # if('9' in pinyin_sentence):
    #   pinyin_sentence=pinyin_sentence.replace("9",",JIU,")
    # if('0' in pinyin_sentence):
    #   pinyin_sentence=pinyin_sentence.replace("0",",LING,")
    #
    # pinyin_sentence = pinyin_sentence.replace(',,', ',')
    # if (pinyin_sentence[len(pinyin_sentence) - 1] == ','):
    #     pinyin_sentence = pinyin_sentence[0:len(pinyin_sentence) - 1]
    # if (pinyin_sentence[0] == ','):
    #     pinyin_sentence = pinyin_sentence[1:len(pinyin_sentence)]
    #
    # return(pinyin_sentence)


if __name__ == '__main__':
    open_dirs('C:\\Users\\User\\Desktop\\贵阳项目词库')
    # read_xlsx()
    # print(chinese_pinyin('贵阳项目词库'))
    # print(chinese_pinyin('iphone10iphone80'))