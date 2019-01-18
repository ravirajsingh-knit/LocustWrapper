import os
import pandas as pd
import random
class DataProviderUtility():
    '''Will read Data from CSV file and Provide them to testing framework'''
    def __init__(self, location):
        self.location=location
        self.SingleFile=None
        self.fileList=[]
        self.dataDict={}
        try:
            if location.split(".")[-1]!="csv" and os.path.isdir(location):
                for fileAtLoc in os.listdir(location):
                    filePath=os.path.join(location,fileAtLoc)
                    if os.path.isfile(filePath) and fileAtLoc.split(".")[-1]=="csv":
                        self.fileList.append(fileAtLoc)
            elif os.path.isfile(location) and location.split(".")[-1]=="csv":
                    self.fileList.append(location.split('/')[-1])
                    self.SingleFile=location.split("/")[-1]
                    self.location=location[:-1*len(self.fileList[0])]
            else:
                print("file Not Found")
        except Exception as ex:
            print(ex)
    
    def readData(self):
        '''Read Data from Csv file and store it in dataDict'''
        try:
            for i in range(len(self.fileList)):
                path=os.path.join(self.location,self.fileList[i])
                dataFrame=pd.read_csv(path)
                key=self.fileList[i]
                key=''.join(key.split(".")[:-1])
                self.dataDict[key]=dataFrame
        except Exception as ex:
            print(ex)
        return self.dataDict
    
   

    def getData(self,key=None,method="rand",index="-1"):
        ''' Provide one data randomly or linearly
            key="CSV file name from which you want to take data"
        '''
        try:
            if key is None and self.SingleFile is None:
                print("Provide File name without extension")
            elif key is None and self.SingleFile is not None:
                key="".join(self.SingleFile.split(".")[:-1]) 
            data=self.dataDict[key]
            if method=="rand":
                index=random.randint(0,len(data)-1)
            return data.to_dict(orient='records')[index]
        except Exception as ex:
            print(ex)