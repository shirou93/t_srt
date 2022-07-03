#!/usr/bin/python3
#pip install googletrans==4.0.0rc1

from googletrans import Translator
import re
import time
import sys
import os

def trans(file,source_l,dest_l):
    if os.path.isfile(f'{file}-{dest_l}.srt'):
        os.remove(f'{file}-{dest_l}.srt')
    with open(file, 'r', encoding='utf8') as srt:
        for l in srt:
            file=file.replace('.srt','')
            if re.match('^[0-9]',l):
                with open(f'{file}-{dest_l}.srt','a', encoding='utf8') as tr:
                    l=l.replace('\n','')
                    tr.write(l+'\n')
                    print(l)
            else:
                if re.match('^.',l):
                    translator = Translator()
                    l=str(l)
                    t=translator.translate(l, src=source_l,dest=dest_l)
                    l=l.replace('\n','')
                    print(f'{l} >>> {t.text}')
                    with open(f'{file}-{dest_l}.srt','a', encoding='utf8') as tr:
                        tr.write(t.text+'\n\n')

if __name__ == "__main__":
    try:
        trans(sys.argv[1],sys.argv[2],sys.argv[3])
        print(f'Translate file {sys.argv[1]} from {sys.argv[2]} to {sys.argv[3]}. Completed.' )
    except:
        print('./t_srt.py file.srt source_language destiny_language')