import maya.cmds as cmds


def deleteNS():
    sel_namespace = cmds.ls(sl=True)[0]
    NS = sel_namespace.rsplit(':',1)[0]
    if not cmds.namespace(ex=NS):
        raise Exception('Namespace "'+NS+'" does not exist!')
    cmds.namespace(mv=[NS,':'],f=True)
    cmds.namespace(rm=NS)


if __name__ == '__main__':
	deleteNS()
