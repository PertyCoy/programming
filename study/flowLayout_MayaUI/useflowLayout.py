
import maya.cmds as cmds



def deleteSample(strDelete,*agre):
    cmds.deleteUI(strDelete)

if cmds.window('samplesss_a',q=True,exists=True):
    cmds.deleteUI('samplesss_a')
if cmds.windowPref('samplesss_a',exists=True):
    cmds.windowPref('samplesss_a',remove=True)


cmds.window('samplesss_a')
#cmds.columnLayout('col_layout',adjustableColumn=True)
cmds.scrollLayout('scro_layout',width=400,height=450,childResizable=True)

cmds.flowLayout('flow_main',height = 1000,columnSpacing=1,wrap=True,vertical=False,p='scro_layout')

for i in range(100):
    cmds.button('sa'+str(i),p='flow_main',width = 60,height = 60,c=partial(deleteSample,'sa'+str(i)))




cmds.showWindow('samplesss_a')
