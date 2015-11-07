from numpy import *
import re

if __name__ == '__main__':
    fr=open('newtrain.csv')
    fr.readline()
    data=fr.readline()
    dataset=re.split(',',data.strip())
    #data=re.split('\"',dataset[-1])
    print dataset
