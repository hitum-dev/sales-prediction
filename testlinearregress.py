from numpy import *
import re

if __name__ == '__main__':
    fr=open('train.csv')
    fr.readline()
    data=fr.readline()
    dataset=data.split(',')
    data=re.split('\"',dataset[-1])
    print data
