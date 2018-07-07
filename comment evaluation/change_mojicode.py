# -*- coding: utf-8 -*-
#ユーザが指定したリプライのカウントを行うプログラム
import sys,re,codecs,json,os,glob

filepath = sys.argv[1]
inputfilepath = filepath + "\\*"
filelist = glob.glob(inputfilepath)

txt_filelist = []
pattern = r'.txt'
for file in filelist:
    if re.search(pattern,file):
        txt_filelist.append(file)
    else:
        continue

for file in txt_filelist:
    # Shift_JIS ファイルのパス
    shiftjis_csv_path = file

    # UTF-8 ファイルのパス
    utf8_csv_path = file

    # 文字コードを utf-8 に変換して保存
    fin = codecs.open(shiftjis_csv_path, "r", "Shift_JISx0213")
    tmp = []
    for row in fin:
        tmp.append(row)
    fin.close()

    fout_utf = codecs.open(utf8_csv_path, "w", "utf-8")
    for row in tmp:
        fout_utf.write(row)
    fout_utf.close()
    