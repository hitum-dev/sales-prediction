from numpy import *
import pdb
from linearregress import *
import matplotlib.pyplot as plt
from pylab import *
import re
import csv

   
def loadDataSet(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields 
    dataMat = []; labelMat = []
    dataList = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr[1:])
        dataList.extend(lineArr[1:])
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat,dataList

def loadDataSet_mul(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split(',')) - 1 #get number of fields
    dataMat = []; labelMat = []
    print "start-0"
    print numFeat
    fr = open(fileName)
    print "start-1"
    line = fr.readlines()
    print "start-2"
    print line
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        print "start-3"
        print curLine
        print "start-4"
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        print lineArr
        labelMat.append(float(curLine[-1]))
        print float(curLine[-1])
    return dataMat,labelMat

def test_singleFeture():
    xArray, yArray,xList = loadDataSet('ex0.txt')
    testLR = linearRegress()
    
    testLR.regress(xArray, yArray, solver = 'OLS')
    predicted = testLR.predict(xArray,solver = 'OLS')
    predicted_r =  predicted

    testLR.regress(xArray, yArray, solver = 'ridge', **{'lam':0.1})
    predicted_r = testLR.predict(xArray,solver = 'ridge')

    cor = corrcoef(mat(predicted),mat(yArray))

    print 'cor: ',cor
    #pdb.set_trace()

    figure(1)
    subplot(211)  
    plt.scatter(array(yArray), predicted)
    plt.plot([min(yArray),max(yArray)],[min(predicted),max(predicted)],'--k')
    plt.axis('tight')
    plt.xlabel('True value')
    plt.ylabel('Predicted value')
    #plt.show()

    subplot(212)  
    plt.scatter(array(yArray), predicted_r)
    plt.plot([min(yArray),max(yArray)],[min(yArray),max(yArray)],'--k')
    plt.axis('tight')
    plt.xlabel('True value')
    plt.ylabel('Predicted value')
    plt.show()

    figure(2)
    subplot(211)  
    plt.scatter(array(xList), array(yArray))
    plt.plot([min(xList),max(xList)],[min(yArray),max(yArray)],'--k')
    plt.axis('tight')
    plt.xlabel('feture value')
    plt.ylabel('True value')

    subplot(212)  
    plt.scatter(array(xList), array(predicted_r))
    plt.plot([min(xList),max(xList)],[min(predicted_r),max(predicted_r)],'--k')
    plt.axis('tight')
    plt.xlabel('feture value')
    plt.ylabel('Predicted value')
    
    plt.show()

def rssError(yArr,yHatArr): #yArr and yHatArr both need to be arrays
    return ((yArr-yHatArr)**2).sum()

def test_mutipleFeture():
    #xArray, yArray = loadDataSet_mul('abalone.txt')
    xArray, yArray = test('train.csv')
    testLR = linearRegress()
    print "xArray"
    print xArray
    print "yArray"
    print yArray

def test(fileName):

    numFeat = len(open(fileName).readline().split(',')) #get number of fields
    dataSet = []; saleSet = [];

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
        wLine=[]
    csvFile.close()
    frStore.close()
    return dataSet,saleSet

if __name__ == '__main__':
    #test_singleFeture()
 #   test_mutipleFeture() 
#    test('train.csv')
    test('train.csv')
    
