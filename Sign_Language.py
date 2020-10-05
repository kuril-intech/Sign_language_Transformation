
import os
import json
import shutil
import pandas as pd
import pathlib
# os.mkdir('/root/.kaggle/')
os.mkdir('kaggle')
os.mkdir('kaggle/raw_file')
os.mkdir('kaggle/raw_file/ASL')
os.mkdir('kaggle/raw_file/MNIST')
os.mkdir('kaggle/raw_file/ASLDS')
os.mkdir('kaggle/Train')
os.mkdir('kaggle/Valid')
DATA_RAW_FOLDER='/content/kaggle/raw'
# touch /root/kaggle/kaggle.json
with open('/root/.kaggle/kaggle.json','w') as file:
  json.dump({"username":"dangnguyenhoang","key":"93f2479dbfed13ba73154f234d80f94f"},file)
# cp /root/kaggle/kaggle.json /content/kaggle/kaggle.json
# chmod600 /root/.kaggle/kaggle.json
# ls
kaggle datasets download -d datamunge/sign-language-mnist -p /content/kaggle/raw_file/MNIST
kaggle datasets download -d grassknoted/asl-alphabet -p /content/kaggle/raw_file/ASL
kaggle datasets download -d ayuraj/american-sign-language-dataset -p /content/kaggle/raw_file/ASLDS