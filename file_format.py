from numpy import *
import pdb
from linearregress import *
import matplotlib.pyplot as plt
from pylab import *
import re
import csv


def trimStore(fileName):

    numFeat = len(open(fileName).readline().split(',')) #get number of fields
    dataSet = []; saleSet = [];

    storeDataSet={}

    csvFile=file('newStore.csv','wb+')
    fwStore =csv.writer(csvFile)
    
    title ="Store,StoreTypeA,StoreTypeB,StoreTypeC,StoreTypeD,AssortmentA,AssortmentB,AssortmentC,Competition Distance,CompetitionOpenSinceMonth,CompetitionSinceYear,Promo2,Promo2SinceWeek,Promo2SinceYear,promoInterval(from1-12)"
#    fwStore.writerow(wLine)
    frStore = open('store.csv')

    titleSet=re.split(',',title)

    wLine=titleSet
    fwStore.writerow(wLine)
    
    wLine=[]
    #initialize

    flag=0
    
    for line in frStore.readlines():
        if flag==0:
            flag=1
            continue
        lineData = line.strip().split(',')

        for i in range(0,25):  ## reinitial
            wLine.append('')
    
        wLine.insert(0,lineData[0])
        if lineData[1]=="\"a\"":  # write storeType
            wLine[1]=1
            wLine[2]=0
            wLine[3]=0
            wLine[4]=0
        elif lineData[1]=="\"b\"":
            wLine[1]=0
            wLine[2]=1
            wLine[3]=0
            wLine[4]=0
        elif lineData[1]=="\"c\"":
            wLine[1]=0
            wLine[2]=0
            wLine[3]=1
            wLine[4]=0
        elif lineData[1]=="\"d\"":
            wLine[1]=0
            wLine[2]=0
            wLine[3]=0
            wLine[4]=1

        if lineData[2]=="\"a\"": #write assortment
            wLine[5]=1
            wLine[6]=0
            wLine[7]=0
        elif lineData[2]=="\"b\"":
            wLine[5]=0
            wLine[6]=1
            wLine[7]=0
        elif lineData[2]=="\"c\"":
            wLine[5]=0
            wLine[6]=0
            wLine[7]=1

        wLine[8]=lineData[3] #write competitionDistance

        wLine[9]=lineData[4] #write competitionOpenSinceMonth

        wLine[10]=lineData[5] #write competitionOpenSinceYear

        wLine[11]=lineData[6] #write promo2

        wLine[12]=lineData[7] #write promo2SinceWeek

        wLine[13]=lineData[8] #write promo2SinceYear

        #identify the text of promoInterval and transfer it into another format
        for i in range(14,26):
            wLine[i]=0
            
        if lineData[9]=='\"\"':
            pass
        else:
            intervalSet=re.split('[,|\"]',lineData[9])
            for month in intervalSet:
                if month == 'Jan':
                    wLine[14]=1
                elif month == 'Feb':
                    wLine[15] =1
                elif month == 'Mar':
                    wLine[16] =1
                elif month == 'Apr':
                    wLine[17] =1
                elif month == 'May':
                    wLine[18] =1
                elif month == 'Jun':
                    wLine[19] =1
                elif month == 'Jul':
                    wLine[20]=1
                elif month == 'Aug':
                    wLine[21] =1
                elif month == 'Sep':
                    wLine[22] =1
                elif month == 'Oct':
                    wLine[23] =1
                elif month == 'Nov':
                    wLine[24] =1
                elif month == 'Dec':
                    wLine[25] =1
        fwStore.writerow(wLine)
        storeDataSet[wLine[0]]=wLine
        wLine=[]
    csvFile.close()
    frStore.close()
    return storeDataSet

def trimSaleData(filename): # new storeSaleGenerator
    csvFile= file('newtrain.csv','wb+')
    fwSale= csv.writer(csvFile) #fwSale is used for writing csv file

    frSale=open('train.csv')

    flag=0

    wLine=[]

    for line in frSale.readlines():

        if flag==0:
            flag=1
            continue

        for i in range(0,18): # initial
            wLine.append('')

        lineData=line.split(',')

        wLine[0]=lineData[0]   #write data

        if lineData[1]=='5':   #date of week
            wLine[1]=0
            wLine[2]=0
            wLine[3]=0
            wLine[4]=0
            wLine[5]=1
        elif lineData[1]=='4':
            wLine[1]=0
            wLine[2]=0
            wLine[3]=0
            wLine[4]=1
            wLine[5]=0
        elif lineData[1]=='3':
            wLine[1]=0
            wLine[2]=0
            wLine[3]=1
            wLine[4]=0
            wLine[5]=0
        elif lineData[1]=='2':
            wLine[1]=0
            wLine[2]=1
            wLine[3]=0
            wLine[4]=0
            wLine[5]=0
        elif lineData[1]=='1':
            wLine[1]=1
            wLine[2]=0
            wLine[3]=0
            wLine[4]=0
            wLine[5]=0

        date= lineData[2].split('-') #date

        wLine[6]=date[0] # year
        wLine[7]=date[1] # month
        wLine[8]=date[2] # day

        wLine[9]=lineData[4]  # customers

        wLine[10]=lineData[5] #Open

        wLine[11]=lineData[6] #promo

        if lineData[7]=="\"a\"": #stateHoliday
            wLine[12] = 1   #state
            wLine[13] = 0   #easter
            wLine[14] = 0   #christmas
            wLine[15] = 0   #none
        elif lineData[7]=="\"b\"":
            wLine[12] = 0
            wLine[13] = 1
            wLine[14] = 0
            wLine[15] = 0
        elif lineData[7]=="\"c\"":
            wLine[12] = 0
            wLine[13] =0
            wLine[14] =1
            wLine[15]=0
        elif lineData[7]=="\"0\"":
            wLine[12] =0
            wLine[13] =0
            wLine[14] =0
            wLine[15] =1

        data=re.split('\"',lineData[-1])
        if data[1]=='0':
            wLine[16]=0
            
        elif data[1]=='1':
            wLine[16]=1

        wLine[17]=lineData[3] # sales
        fwSale.writerow(wLine)
        

        wLine=[]

    frSale.close()
    csvFile.close()
        

    
    


if __name__ == '__main__':
    #test_singleFeture()
 #   test_mutipleFeture() 
#    test('train.csv')
#storeData=trimStore('train.csv') #get store information and trim the formate of store data
    trimSaleData('abc.txt')

    
