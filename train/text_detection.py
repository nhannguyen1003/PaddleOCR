import os
import numpy as np
from tqdm import tqdm
import pandas as pd
import json
import glob
import codecs
 
root_path = glob.glob('./vietnamese/labels/*')
 
train_label = codecs.open("train_label.txt","w", "utf-8")
test_label = codecs.open("test_label.txt","w", "utf-8")
useen_label = codecs.open("useen_label.txt","w", "utf-8")
for file in root_path:
    f = open(file,encoding="utf-8")
    content = f.readlines()
    f.close()
    content = [x.strip() for x in content]
    text = []
    for i in content:
      label = {}
      i = i.split(',',8)
      label['transcription'] = i[-1]
      label['points'] = [[i[0],i[1]],[i[2],i[3]], [i[4],i[5]],[i[6],i[7]]]
      text.append(label)
 
    content = []
    text = json.dumps(text, ensure_ascii=False)
 
    img_name = os.path.basename(file).split('.')[0].split('_')[1]
    int_img = int(img_name)
    img_name = 'im' + "{:04n}".format(int(img_name)) + '.jpg'
    if int_img >= 1500:
      useen_label.write( img_name+ '\t'+f'{text}' + '\n')
    elif int_img >= 1200:
      test_label.write( img_name+ '\t'+f'{text}' + '\n')
    else:
      train_label.write( img_name+ '\t'+f'{text}' + '\n')