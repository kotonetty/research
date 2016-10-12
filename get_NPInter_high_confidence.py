
#データ作成のプログラム
import csv
import re
import codecs


def change_csv(): #NPInter3のファイルをCSVファイルに変換する関数
    fp = open("../interaction_NPInter.csv","w")

    #データの読み込み
    f = codecs.open("../interaction_NPInter[v3.0].txt",encoding="utf-8",errors="ignore")
    lines = f.readlines()
    f.close()

    for line in lines:
        row = re.split('\t',line) #行ごとにリスト化
        row[-1] = row[-1].rstrip('\n')
        w = csv.writer(fp,delimiter=',')
        w.writerow(row)
    fp.close()


with open('../interaction_NPInter.csv',newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter='')
    for row in cscreader:
        
    if line.find("RNA-Protein") >= 0:
    print (line[:-1])



