import os 
import random

data_dir = '/home/jupyter/Data/train/train'
data_dir_valid = '/home/jupyter/Data/train/valid'

files = os.listdir('/home/jupyter/Data/train/train')
files_mv = random.sample(files,k=len(files)//10)

for file_n in files_mv:
  os.rename(data_dir + '/' + file_n, data_dir_valid + '/' + file_n)