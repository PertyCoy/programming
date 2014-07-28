#-----------------------------------------------------------------
######  Copyright 2013 FrameSoul. All rights reserved.
######  SCRIPT:EriLee_studioenv.py
######  AUTHOR:EriLee(td.EriLee@gmail.com)
######  DATE:January 31, 2013
######  VERSION:2013.1
#-----------------------------------------------------------------
"""
Studio Environment module for setting up the studio environment

This is a very basic module that will just ensure that the studio package
is added to the PYTHONPATH so that other scripts or an interactive python
session can easily access the studio code.
"""


import maya.cmds as cmds


def deleteNS():
    sel_namespace = cmds.ls(sl=True)[0]
    NS = sel_namespace.rsplit(':',1)[0]
    if not cmds.namespace(ex=NS):
        raise Exception('Namespace "'+NS+'" does not exist!')
    cmds.namespace(mv=[NS,':'],f=True)
    cmds.namespace(rm=NS)

def aa():
	test_list = ['aa_1','aa_2','aa_3']
	for key in test_list:
		print key

if __name__ == '__main__':
	deleteNS()

#####helloWorld
You are Brach Render