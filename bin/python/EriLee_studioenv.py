"""
 *  studioenv.cpp
 *  studioenv
 *
 *  Created by EriLee on 10/18/13.
 *  Copyright 2013 __MyCompanyName__. All rights reserved.
 *
 
Studio Environment module for setting up the studio environment

This is a very basic module that will just ensure that the studio package
is added to the PYTHONPATH so that other scripts or an interactive python
session can easily access the studio code.
"""
__version__ = "studioenv,Created on 10/18/13"
__author__ = "EriLee"
__source__ = "//EriLee/FrameSoul_Programming/bin"

import os, sys
import maya.cmds as cmds
import maya.mel as mel

class studioenv():
    currFile_Path=os.path.abspath(os.path.dirname(__file__))
    systemName='MyStudio'

    def getEnv(self):
        self.mayaVer = cmds.about(v=1).split()[0]
        self.mayaX64 = cmds.about(is64=1)
        self.user = os.getenv('USERNAME')
        self.isMayaGUI = 0
        try:
            mainWindow=mel.eval('$tmp=$gMainWindow')
            if mainWindow=='MayaWindow':
                isMayaGUI = 1
        except:
            pass

    def config_studio_env(self):
        if 'ERILEE_SystemDevelop_EnvPath' not in os.environ:
            os.environ['ERILEE_SystemDevelop_EnvPath']=os.path.join(os.path.split(self.currFile_Path)[0].replace('\\', '/'))
            studio_env = os.environ['ERILEE_SystemDevelop_EnvPath']
            if studio_env not in sys.path:
                sys.path.append(studio_env)
    
    def config_sitePackages(self):
        config_PyQt_env=os.path.join(self.currFile_Path,'site-packages').replace('\\', '/')
        if config_PyQt_env not in sys.path:
            sys.path.append(config_PyQt_env)

    def config_studio(self):
        config_studio_env=os.path.join(self.currFile_Path,'studio').replace('\\', '/')
        if config_studio_env not in sys.path:
            sys.path.append(config_studio_env)

    def config_studio_plug(self):
        MAYA_PLUG_IN_PATH = os.path.join( os.environ['ERILEE_SystemDevelop_EnvPath'], 'plug-ins').replace('\\', '/')
        if MAYA_PLUG_IN_PATH not in os.environ['MAYA_PLUG_IN_PATH'].split(';'):
            PluginPath=os.environ['MAYA_PLUG_IN_PATH']+';'+MAYA_PLUG_IN_PATH
            os.environ['MAYA_PLUG_IN_PATH']=PluginPath

    def loadPlug(self):
        if not pluginInfo('FrameSoul_Studio', q=1, l=1):
            loadPlugin( "FrameSoul_Studio.py")

    def do_it(self):
        self.config_studio_env()
        self.config_sitePackages()
        self.config_studio()
        self.config_studio_plug()
        #self.loadPlug()
        # from studio.shelfToolWindow import createStudioShelf
        # from studio.systemMenu import systemMenuItem
        # systemMenuItem.systemMenuItems(self.systemName)
        # createStudioShelf.createStudioShelfs(self.systemName)



#icons_envs=[os.path.join(os.path.split(self.currFile_Path)[0],'icons').replace('\\', '/')]
# #print os.environ['ERILEE_PROGRAMMING_DIR']

# if 'XBMLANGPATH' in os.environ:
#     studio_python_path = os.path.join(os.environ['XBMLANGPATH'],'python')
# else:
#     studio_python_path = ''
    
# if studio_python_path not in sys.path:
#     sys.path.append(studio_python_path)

# currFile_Path=os.path.abspath(os.path.dirname(__file__))
# icons_envs=[os.path.join(os.path.split(currFile_Path)[0],'icons').replace('\\', '/')]
# print icons_envs
# print os.path.split(currFile_Path)[0].replace('\\', '/')