import os
from zipfile import ZipFile
from tqdm import tqdm
train_data = "./data/bridge_train.zip"
val_data = "./data/bridge_val.zip"

out_train = "./data"
out_val = "./data"

def unzip(in_file, out_path):
    with ZipFile(in_file, 'r') as target: 
        file_list = target.namelist()

        with tqdm(total = len(file_list), unit='file', desc="Extracting") as pbar:
            for file in file_list:
                target.extract(file, path=out_path)
                pbar.update(1)


def unzip2(in_file, out_path):
    with ZipFile(in_file, 'r') as target: 
        target.extractall(out_path)
        
unzip2(train_data, out_train)
unzip2(val_data, out_val)