import maya.cmds as cmds


def deleteNS():
    sel_namespace = cmds.ls(sl=True)[0]
    NS = sel_namespace.rsplit(':',1)[0]
    if not cmds.namespace(ex=NS):
        raise Exception('Namespace "'+NS+'" does not exist!')
    cmds.namespace(mv=[NS,':'],f=True)
    cmds.namespace(rm=NS)

def helloWorld():
	print 'HelloWorld'
'''
def cc():
	print 'cc'
'''
=======


def aa():
	test_list = ['aa_1','aa_2','aa_3']
	for key in test_list:
		print key

<<<<<<< HEAD
>>>>>>> test
if __name__ == '__main__':
	deleteNS()
	helloWorld()



	kokkokokokk