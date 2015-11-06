
import json
import inspect 
import pdb

def object2dict(obj):   
    #convert object to a dict   
    d = {'__class__':obj.__class__.__name__, '__module__':obj.__module__}   
    d.update(obj.__dict__)   
    return d

def objectDumps2File(obj, jsonfile):
    objDict = object2dict(obj)
    with open(jsonfile, 'w') as f:
        f.write(json.dumps(objDict))
    
def dict2object(d):   
    '''convert dict to object, the dict will be changed'''    
    if'__class__' in d:   
        class_name = d.pop('__class__')   
        module_name = d.pop('__module__')   
        module = __import__(module_name)   
        #print 'the module is:', module   
        class_ = getattr(module,class_name)   
        args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args  
        #print 'the atrribute:', repr(args)
        #pdb.set_trace()
        inst = class_(**args) #create new instance   
    else:   
        inst = d   
    return inst

def objectLoadFromFile(jsonFile):
    '''load json file and generate a new object instance whose __name__ filed
    will be 'inst' '''
    with open(jsonFile) as f:
        objectDict =json.load(f)
    obj = dict2object(objectDict)
    return obj

#test function   
if __name__  == '__main__':

    class Person(object):   
        def __init__(self,name,age, **args):
            obj_list = inspect.stack()[1][-2]
            self.__name__ = obj_list[0].split('=')[0].strip()#object instance name
            self.name = name   
            self.age = age
            
        def __repr__(self):   
            return 'Person Object name : %s , age : %d' % (self.name,self.age)

        def say(self):
            #d = inspect.stack()[1][-2]
            #print d[0].split('.')[0].strip()
            return self.__name__

        def jsonDumps(self, filename=None):
            '''essential transformation to Python basic type in order to
            store as json. dumps as objectname.json if filename missed '''
            if not filename:
                jsonfile = self.__name__+'.json'
            else: jsonfile = filename
            objectDumps2File(self, jsonfile)
        
        def jsonLoadTransfer(self):#TBD
            '''essential transformation to object required type,such as
            numpy matrix.call this function after newobject = objectLoadFromFile(jsonfile)'''
            pass


    p = Person('Aidan',22)     
    #json.dumps(p)#error will be throwed
    
    #objectDumps2File(p,'Person.json')
    p.jsonDumps()
    p_l = objectLoadFromFile('p.json')
      
    print 'the decoded obj type: %s, obj:%s' % (type(p_l),repr(p_l))
    
