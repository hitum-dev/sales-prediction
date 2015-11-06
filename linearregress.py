

from numpy import *
from object_json import *
from copy import *
import pdb
import operator


class linearRegress(object):
    def __init__(self,LRDict = None,  **args):
        '''currently support OLS, ridge, LWLR           
        '''
        obj_list = inspect.stack()[1][-2]
        self.__name__ = obj_list[0].split('=')[0].strip()
        if not LRDict:
            self.LRDict = {}
        else:
            self.LRDict = LRDict
            #to Numpy matraix
            if 'OLS' in self.LRDict:
                self.LRDict['OLS'] = mat(self.LRDict['OLS'])
            if 'ridge' in self.LRDict:
                self.LRDict['ridge'][0] = mat(self.LRDict['ridge'][0])
                self.LRDict['ridge'][2] = mat(self.LRDict['ridge'][2])
                self.LRDict['ridge'][3] = mat(self.LRDict['ridge'][3])
                self.LRDict['ridge'][4] = mat(self.LRDict['ridge'][4])
        
    def jsonDumpsTransfer(self):
        '''essential transformation to Python basic type in order to
        store as json. dumps as objectname.json if filename missed '''
        #pdb.set_trace()
        if 'OLS' in self.LRDict:
            self.LRDict['OLS'] = self.LRDict['OLS'].tolist()
        if 'ridge' in self.LRDict:
                self.LRDict['ridge'][0] = self.LRDict['ridge'][0].tolist()
                self.LRDict['ridge'][2] = self.LRDict['ridge'][2].tolist()
                self.LRDict['ridge'][3] = self.LRDict['ridge'][3].tolist()
                self.LRDict['ridge'][4] = self.LRDict['ridge'][4].tolist()

    def jsonDumps(self, filename=None):
        '''dumps to json file'''
        self.jsonDumpsTransfer()
        if not filename:
            jsonfile = self.__name__+'.json'
        else: jsonfile = filename
        objectDumps2File(self, jsonfile)
        
    def jsonLoadTransfer(self):      
        '''essential transformation to object required type, such as numpy matrix
        call this function after newobject = objectLoadFromFile(jsonfile)'''
        #pdb.set_trace()
        if 'OLS' in self.LRDict:
            self.LRDict['OLS'] = mat(self.LRDict['OLS'])
        if 'ridge' in self.LRDict:
            self.LRDict['ridge'][0] = mat(self.LRDict['ridge'][0])
            self.LRDict['ridge'][2] = mat(self.LRDict['ridge'][2])
            self.LRDict['ridge'][3] = mat(self.LRDict['ridge'][3])
            self.LRDict['ridge'][4] = mat(self.LRDict['ridge'][4])

    def solver_OLS(self, xMat, yMat):
        x0Mat = mat(ones((xMat.shape[0],1)))
        xMat = hstack((x0Mat, xMat))#extend x0=1 for each sample
        xTx = xMat.T*xMat
        if linalg.det(xTx) == 0.0:
            print "This matrix is singular, cannot do inverse"
            #raise
        else:
            self.LRDict['OLS'] = xTx.I * (xMat.T*yMat)
    
    
    def solver_ridge(self, xMat, yMat, **args):
        lam = args['lam']
        yMean = mean(yMat,0)
        yMat = yMat - yMean     #to eliminate X0 take mean off of Y
        #regularize X's
        xMeans = mean(xMat,0)   #calc mean then subtract it off
        xVar = var(xMat,0)      #calc variance of Xi then divide by it
        xMat = (xMat - xMeans)/xVar
        x0Mat = mat(ones((xMat.shape[0],1)))
        xMat = hstack((x0Mat, xMat))#extend x0=1 for each sample
        #pdb.set_trace()
        xTx = xMat.T*xMat
        I = eye(shape(xMat)[1])
        I[0][0] = 0;#w0 has no punish factor
        denom = xTx + I*lam
        if linalg.det(denom) == 0.0:
            print "This matrix is singular, cannot do inverse"
            #raise()
        else:
            paraList = []
            ws = denom.I * (xMat.T*yMat)
            paraList.append(ws)
            paraList.append(lam)
            paraList.append(xMeans)
            paraList.append(xVar)
            paraList.append(yMean)
            self.LRDict['ridge'] = paraList
        
    def regress(self, xInMat, yInMat, solver = 'OLS', **args):
        ''' create regression moel according to solver, the default solover is OLS
            parameters:
              xMat: (m,n) matrix or list, m represents sample count, n represents feture count
              yMat: (m,1) matrix or list, m represents sample count
              **args represents additional parameters of solver, such as lambda of ridge slover
        '''
        xMat = mat(xInMat)
        yMat = mat(yInMat).T
        if solver == 'OLS':
            self.solver_OLS(xMat, yMat)
        elif solver == 'ridge':
            self.solver_ridge(xMat, yMat, **args)
        else:
            print '%s solver not support'%solver
            #raise()
            
    def __predict(self, x2predict, ws):
        ''' '''
        tmpX = mat(x2predict)
        x0Mat = mat(ones((tmpX.shape[0],1)))
        xMat =  hstack((x0Mat, tmpX))#extend x0=1 for each testvector
        return (mat(xMat)*ws).T.getA()[0]#return predict array
     

    def predict(self, x2predict, solver = 'OLS'):
        x2predict = mat(x2predict)
        if solver == 'OLS':
            ws = self.LRDict['OLS']
            return self.__predict(x2predict, ws)
        elif solver == 'ridge':
            ws = self.LRDict['ridge'][0]
            xMean = self.LRDict['ridge'][2]
            xVar = self.LRDict['ridge'][3]
            x2predict = (x2predict - xMean)/xVar
            yMean = self.LRDict['ridge'][-1]
            #pdb.set_trace()
            return self.__predict(x2predict, ws)+yMean.getA()[0].tolist()[0]
        else:
            print '%s solver not support'%solver
            #raise()
            return None
          

if __name__ == "__main__":
    pass
 
    
