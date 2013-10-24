import maya.cmds as cmds
import pymel as pm

class clean_scene(object):
    def __init__(self):
        pass

    def del_unknownNode(self):
        typeList = ['unknown','unknownDag','unknownTransform']
        sel_allNode_List = cmds.ls(type=typeList)
        cmds.delete(sel_allNode_List)
        return sel_allNode_List
    
    def del_unknown_RefNode(self):
        deleteList = list()
        refNode_List = cmds.ls(type='reference')
        for refNode in refNode_List:
            try:
                cmds.referenceQuery(refNode,filename=True)
            except RuntimeError:
                deleteList.append(refNode)
                cmds.lockNode(refNode,lock=False)
                cmds.delete(refNode)
         return deleteList


if __name__ == '__main__':
    cs = clean_scene()
    cs.del_unknown_RefNode()