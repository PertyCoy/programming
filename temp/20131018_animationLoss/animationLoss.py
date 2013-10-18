import maya.cmds as cmds



#### select reference node,add to the sel_object List
sel_object = cmds.ls(sl=True)[0]
animCurve_Node_list = cmds.listConnections(source=True,d=False,sh=False,type= 'animCurve')###select connecting the animation curve node
unConnNodeList=[]
for animCurve_Node in animCurve_Node_list:
    try:
        splitList = animCurve_Node.rsplit('_',1) # split the animCurve Node name
        cmds.connectAttr(animCurve_Node+'.output',splitList[0]+'.'+splitList[1])### connect attributes
    except RuntimeError:
        unConnNodeList.append(animCurve_Node)


##### Secondary circulation

for unConnNode in unConnNodeList:
    splitList_b = unConnNode.rsplit('_',2)
    cmds.connectAttr(unConnNode+'.output',splitList_b[0]+'.'+splitList_b[1]+'_'+splitList_b[2])
    
########################################################################################


selAnimCVs = cmds.ls(sl=True)

for selAnimCV in selAnimCVs:
    try:
        splitList_c = selAnimCV.rsplit('_',1)
        cmds.connectAttr(selAnimCV+'.output',splitList_c [0]+'.'+splitList_c[1])
    except RuntimeError:
        print selAnimCV