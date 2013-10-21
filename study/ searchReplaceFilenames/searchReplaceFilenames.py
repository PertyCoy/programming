'''
 *  searchReplaceFilenames.py
 *  
 *
 *  Created by EriLee on 10/18/13.
 *  Copyright 2013 __MyCompanyName__. All rights reserved.
 *
 
This commandline Python script renames all files of specified type (png, jpg and jpeg)
based on a search and replace formula in the textfile fileRenameMatrix.txt.

Example contents of fileRenameMatrix.txt:
hello=hi
version=v

Would rename the following files accordingly:
hello.jpeg -> hi.jpeg
image_version_001.png -> image_v_001.png
hello_version.jpg -> hi_v.jpg
'''


import os 


#Open text file and read contents into list

with open('D:/fileRenameMatrix.txt', 'r') as textFile:
#textFile1 = open('D:/fileRenameMatrix.txt','r')
#These two methods are the same
    myList = [line.strip() for line in textFile]
### myList This list is stored in the variable: the document is to read each line of information.

'''
## Determine the hard disk file exists.
path = 'D:/fileRenameMatrix1.txt'
print os.path.isfile(path)
'''

files = [file for file in os.listdir('.') if os.path.isfile(file)]

'''
eg_1:
files=[]    
for file in os.listdir('E:/mov'):
    #print file
    if os.path.isfile('E:/mov/'+file):
        files.append(file)
eg_2:        
files2 = [file for file in os.listdir('E:/mov') if os.path.isfile('E:/mov/'+file)]
return ['tanh_a.mov','tanh_b.mov','tanh_c.mov','tanh_d.mov']
'''

# eg:filess=['tanh_a.mov','tanh_b.mov','tanh_c.mov','tanh_d.mov']

files = [file for file in os.listdir('.') if os.path.isfile(file)]

# Parse list of files...
for file in files:
        if ('.png' in file) or ('.jpg' in file) or ('.jpeg' in file):
                print 'Processing ' + file
                for item in myList:
                        delimiter = '='
                        oldString = item[:item.rfind(delimiter)]
                        newString = item[item.rfind(delimiter)+1:]
                        if oldString in file:
                                print 'Found match of ' + oldString
                                print 'Renaming ' + file + ' to ' + file.replace(oldString, newString)
                                try:
                                        os.rename(file, file.replace(oldString, newString))
                                        print 'Rename successful.'
                                except:
                                        print 'Error: unable to rename ' + file
                                print '\n'

        else:
                print 'Skipped ' + file