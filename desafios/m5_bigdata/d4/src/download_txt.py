import pandas as pd
import wget
import glob
import shutil
import os
from pathlib import Path

df = pd.read_csv('libros.csv', delimiter='\t')

for libro in df['http']:
    wget.download(libro)
    print(libro)

folder = "./richardson_clarissa/"
Path(folder).mkdir(parents=True, exist_ok=True)

for i, file in enumerate(glob.glob('*.txt')):
    renamed = 'clarissa_%s.txt' % (i+1)
    os.rename(file, renamed)
    print('done ' + renamed)
