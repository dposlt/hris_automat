#!/usr/bin/python env

## head main.py ##


__author__ = 'David Poslt'
__version__ = '1.0.0'
__date__ = '17.3.2020'


import ini,os,log
from checkFolder import checkFolder

CONST_ZIP = ini.zipFile()
CONST_TARGET = ini.target()
CONST_DEPLOY = ini.deploy()

def isFull(const_path):
    if checkFolder(const_path):
        count = len(os.listdir(const_path))
        print(count)
        if count > 0:
             print('uzip file')
             log.info('unzip file')
        else:
            exit() ## neprodukcni, bude nutne zmeninit na sys.exit(0)



if __name__ == '__main__':

    isFull(CONST_ZIP)

