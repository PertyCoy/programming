import maya.cmds as cmds
from functools import partial

def sample(strYaya,*agre):
    cmds.deleteUI('layout_'+strYaya.split('saww')[1])
    
    main_column_num = cmds.layout('main_layout',q=True,numberOfChildren=True)
    for d in range(main_column_num):
        rowlayoutNum = cmds.rowLayout('sadw'+str(d),q=True,numberOfChildren=True)
        if rowlayoutNum<12 or rowlayoutNum>0:
            for i in range(12 - int(rowlayoutNum)):
                try:
                    layPos = cmds.layout('sadw'+str(int(d)+1),q=True,childArray=True)
                    cmds.columnLayout(layPos[0] ,e=True,parent='sadw'+str(d)) 
                except:
                    pass

if cmds.window('samplesss_a',q=True,exists=True):
    cmds.deleteUI('samplesss_a')
if cmds.windowPref('samplesss_a',exists=True):
    cmds.windowPref('samplesss_a',remove=True)
cmds.window('samplesss_a')
cmds.columnLayout('main_layout')
for j in range(12):
    cmds.rowLayout('sadw'+str(j),numberOfColumns=12)
    for i in range(12):
        cmds.columnLayout('layout_'+str(i)+'_'+str(j))
        cmds.button('saww'+str(i)+'_'+str(j),width=60,height=60,l='sa_'+str(i)+'_'+str(j),c=partial(sample,'saww'+str(i)+'_'+str(j)))
        cmds.setParent('..')
    cmds.setParent('..')
cmds.setParent('..')
cmds.showWindow('samplesss_a')
