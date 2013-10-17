import os

eg_path = ['D:/sample/sample.ma']
class contPath():
    def __init__(self):
        pass
    def getfileName(self,getPaths):
        fileName_list=[]
        for getPath in getPaths:
            file_name = os.path.basename(getPath)
            #print file_name
            
            fileName_list.append(file_name)
        return fileName_list
if __name__ == '__main__':
    cp = contPath()
    print cp.getfileName(eg_path)
