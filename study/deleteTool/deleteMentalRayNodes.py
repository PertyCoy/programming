import maya.cmds as cmds

mentalRay_nodesList = ['miDefaultOptions','miContourPreset','Draft','DraftMotionBlur','DraftRapidMotion','Preview','PreviewMotionblur','PreviewRapidMotion','PreviewCaustics','PreviewGlobalIllum',
                       'PreviewFinalGather','Production','ProductionMotionblur','ProductionRapidMotion','ProductionFineTrace','ProductionRapidFur','ProductionRapidHair','miDefaultFramebuffer',
                       'mentalrayItemsList']

class sceneCleanup(object):

    def deleteNode(nodeName):
        if cmds.objExists(nodeName):
            try:
                cmds.delete(nodeName)
                print nodeName + ' was deleted.'
            except:
                print nodeName + ' could not be deleted...'

if __name__ == '__main__':
    for mr_nodes in mentalRay_nodesList:
        sc = sceneCleanup()
        sc.deleteNode(mr_nodes)