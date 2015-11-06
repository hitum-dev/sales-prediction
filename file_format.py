from numpy import *
import pdb
from linearregress import *
import matplotlib.pyplot as plt
from pylab import *
   
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
    dataSet = []; saleSet = []
    
    return dataSet,saleSet

if __name__ == '__main__':
    #test_singleFeture()
 #   test_mutipleFeture() 
#    test('train.csv')
    test_mutipleFeture()
    
