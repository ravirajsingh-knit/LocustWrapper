import os
import pandas as pd
import random
class DataProviderUtility():
    '''Will read Data from CSV file and Provide them to testing framework'''

    def __init__(self, location,fileName="ALL"):
        self.location=location
        self.fileList=[]
        self.dataDict={}
        try:
            if fileName=="ALL":
                for fileAtLoc in os.listdir(location):
                    filePath=os.path.join(location,fileAtLoc)
                    if os.path.isfile(filePath) and fileAtLoc.split(".")[-1]=="csv":
                        self.fileList.append(fileAtLoc)
            else:
                filePath=os.path.join(location,fileName)
                if os.path.isfile(filePath) and fileName.split(".")[-1]=="csv":
                    self.fileList.append(fileName)
        except Exception as ex:
            print(ex)
    
    def readData(self):
        '''Read Data from Csv file and store it in dataDict'''
        try:
            for i in range(self.fileList):
                path=os.path.join(self.location,self.fileList[i])
                dataFrame=pd.read_csv(path)
                key=self.fileList[i]
                key=''.join(key.split(".")[:-1])
                self.dataDict[key]=dataFrame
        except Exception as ex:
            print(ex)
        return self.dataDict
    
    def giveData(self,key="None",method="rand",index="-1"):
        ''' Provide one data randomly or linearly
            key="CSV file name from which you want to take data"
        '''
        if key is None:
            print("No File name is specified")
            pass
        try:    
            data=self.dataDict["key"]
            if method=="rand":
                index=random.randint(0,len(data))
                return data[index]
            elif method=="ind":
                return data[index]
        except Exception as ex:
            print(ex)
    



