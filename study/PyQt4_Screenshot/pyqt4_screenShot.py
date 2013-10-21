'''

 *  studioenv.cpp
 *  studioenv
 *
 *  Created by EriLee on 10/18/13.
 *  Copyright 2013 __MyCompanyName__. All rights reserved.
    
    Screenshot tool for PyQt4

'''
from PyQt4 import QtGui

pixmap = QtGui.QPixmap()
pixmap = QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId(), x = 0, y = 0, width = -1, height = -1)
pixmap.save('E:\\def.jpg')