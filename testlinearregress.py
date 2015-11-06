from numpy import *
import re

if __name__ == '__main__':
     wLine=[]
     line="1,2,3,4,"
     lineData=re.split('[,|\"]',line)
     print lineData
     line="1,2,3"
     lineData=re.split('[,|\"]',line)
     print lineData
     
