
#データ作成のプログラム
import csv
import re
import codecs
import pandas as pd
import numpy as np

def change_csv(): #NPInter3のファイルをCSVファイルに変換する関数
    fp = open("interaction_NPInter.csv","w")

    #データの読み込み
#    dataset = pd.read_table("interaction_NPInter[v3.0].txt",encoding='cp037')
#    dataset.to_csv("test.txt",sep="\t")
#    dataset.to_csv("test.txt",sep="\t")
    f = codecs.open("interaction_NPInter[v3.0].txt",encoding="utf-8",errors="ignore")
    lines = f.readlines()
    f.close()

    for line in lines:
        row = re.split('\t',line) #行ごとにリスト化
        if row[12].find('ncRNA-protein') >= 0 or row[0].find('interactionID') >= 0:
#            row[-1] = row[-1].rstrip('\n') #行末の改行を削除
            del row[6:9]
            del row[8:]
            w = csv.writer(fp,delimiter=',')
            w.writerow(row)
    fp.close()
change_csv()
#データの中からRNA-Proteinの相互作用のデータのみ抜き出す
#f_csv = open("../interaction_NPInter.csv",'r')
#f_csv_w = open("../interaction_NPInter2.csv",'w')
#csvreader = csv.reader(f_csv)
#header = next(reader)
#w = csv.writer(f_csv_w,delimiter=',')
#w.writerow(header) #headerのみ先に書き込む

#for row in csvreader: #データの行でncRNA-proteinとなっている行のみ抜き出して書き込む
#    if row[12].find('ncRNA-protein') >= 0:
#        w.writerow(row)
