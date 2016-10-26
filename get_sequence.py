import csv
import re
import codecs
import urllib.request
import requests
from bs4 import BeautifulSoup
import lxml.html
from io import StringIO
import Bio
from Bio import SeqIO

def get_sequence(): #配列取得
   
    url_miRBase = 'http://www.mirbase.org/' #miRBase url
    url_RefSeq = 'https://www.ncbi.nlm.nih.gov/refseq/' #RefSeq url
    url_uniprot = 'http://www.uniprot.org/' #uniprot url
    f_r = open('/home/slab/kikuchik/research/dataset/NPInter_wholedata/data_python/miRBase1026.fasta','w') #RNAデータを書き込むfastaファイル
    f_p = open('/home/slab/kikuchik/research/dataset/NPInter_wholedata/data_python/protein1020.fasta','w') #Proteinデータを書き込むfastaファイル
 
    with open('/home/slab/kikuchik/research/dataset/NPInter_wholedata/data_python/miRBase_data1020_2.csv','r') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        for row in reader:
            if row[0].find("miRBase") >= 0:
                target_url_m = url_miRBase + 'cgi-bin/mirna_entry.pl?acc=' + row[1]
                target_html_m = urllib.request.urlopen(target_url_m).read()
                root_m = BeautifulSoup(target_html_m,'lxml')
                rnas = root_m.findAll("table",class_="data")
                for rna in rnas:
#                target_html_m = requests.get(target_url_m)
#                root_m = lxml.html.fromstring(target_html_m.text)
#                rnas = root_m.xpath("//div[contains(@class,'data')]")
#                for rna in rnas:
                    rna_name = rna.find('h2').text
                    if rna_name.find(row[2]) >= 0:
                        rna_id = rna.find('td',class_="right").text.strip()
                        seq_url = url_miRBase + 'cgi-bin/get_seq.pl?acc=' + rna_id
                        seq_html = urllib.request.urlopen(seq_url).read()
                        root_seq = BeautifulSoup(seq_html,'lxml')
                        seq = root_seq.find('pre').text
                        f_r.write(seq)
#            if row[3].find("RefSeq") >= 0:
#                url = url_RefSeq + '' + row[4]
#            if row[3].find("UniProt") >= 0:
#                target_url_u = url_uniprot + 'uniprot/' + row[4]+ '.fasta'
#                target_html_u = requests.get(target_url_u).text
#`                f_p.write(target_html_u)
#                root_u = lxml.html.fromstring(target_html_u)
#                print (root_u)
#                seq = root_u.xpath("//")
#                print (seq)
#                for record in SeqIO.parse(StringIO(target_html_u.text),"fasta"):
#                    print (record)
#                root_u = lxml.html.fromstring(target_html_u.text)
#                print(root_u.xpath('pre'))
#                print(p_seq)
get_sequence()
