"""
*  Created by EriLee on 10/18/13.
*  Copyright 2013 __MyCompanyName__. All rights reserved.
"""


import maya.cmds as cmds
import maya.mel as mel



selObj = cmds.ls(sl=True)
create_PM = cmds.createNode('proxyManager')
cmds.connectAttr(create_PM+".proxyList[0]",selObj[0]+".proxyMsg" )

cmds.connectAttr (create_PM + ".proxyList[1]",selObj[1]+ ".proxyMsg" )

cmds.connectAttr (selObj[0]+ ".proxyMsg",create_PM + ".sharedEditsOwner")

shared_refNode = cmds.createNode('reference')

cmds.connectAttr (shared_refNode + ".sharedReference",selObj[0]+ ".sharedReference" )
cmds.connectAttr (shared_refNode + ".sharedReference",selObj[1]+ ".sharedReference" )

mel.eval("sceneEditor -edit -rr $gReferenceEditorPanel;")

cmds.file(ur=selObj[0])
mel.eval("proxySwitch(\""+selObj[1]+"\")")

#cmds.sceneEditor( "$gReferenceEditorPanel",edit=True,rr=True )
#cmds.connectAttr (create_PM+".activeProxy",create_PM + ".proxyList[0]")

