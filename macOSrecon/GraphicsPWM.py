"""Functions relating to Mac graphics power management"""
import os
import plistlib

ROOT = '/System/Library/Extensions/AppleGraphicsPowerManagement.kext/Contents/Info.plist'


def gatherModels():
    """Find all of the models listed in GraphicsPowerManagement.kext"""
    try:
        plist = plistlib.readPlist(ROOT)
    except IOError:
        return
    models = []
    for key in plist["IOKitPersonalities"]["AGPM"]["Machines"]:
        models.append(key)
    return sorted(models)


def dumpModels(filePath):
    """Gather info"""
    models = gatherModels()
    dirPath = os.path.dirname(filePath)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    with open(filePath, "w") as fp:
        fp.write('\n'.join(models))
