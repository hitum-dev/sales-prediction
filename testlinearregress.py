from numpy import *
import re

if __name__ == '__main__':
    fr=open('newtrain.csv')
    randomTrainSet=[]
    fr.readline()
    data=fr.readline()
    dataset=re.split(',',data.strip())
    
    randomData=random.random_integers(1,100)
    
    print randomData
    #data=re.split('\"',dataset[-1])
    #print dataset
