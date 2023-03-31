import os
from zipfile import ZipFile

extract = ''
directories = os.listdir(extract)
for folder in directories:
    with ZipFile(folder, 'r') as toExtract:
        toExtract.extractall(extract + '/')