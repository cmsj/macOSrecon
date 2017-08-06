"""Functions relating to board-id gathering"""
import os
import objc


class attrdict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


ServerInformation = attrdict()
bundle_path = '/System/Library/PrivateFrameworks/ServerInformation.framework'
ServerInformation_bundle = objc.loadBundle('ServerInformation',
                                           ServerInformation,
                                           bundle_path=bundle_path)


def gatherPlistFiles(filePath):
    """Gather a list of plist files in a path, removing the .plist suffix"""
    # This should only be used for directories that contain exclusively plists
    return sorted([f.split(".plist")[0] for f in os.listdir(filePath)])


def dumpListToFile(dataList, filePath):
    """Write out a list to a file, separated by newlines"""
    with open(filePath, "w") as fp:
        fp.write('\n'.join(dataList))


def gatherX86():
    """Gather board-id values for recent X86 machines"""
    plistPath = "/System/Library/Extensions/IOPlatformPluginFamily.kext/" \
                "Contents/PlugIns/X86PlatformPlugin.kext/Contents/Resources/"
    return gatherPlistFiles(plistPath)


def mapBoardsToModels(boardList):
    """Map board-id values to model names"""
    boardModelMap = []
    for boardID in boardList:
        for modelID in ServerInformation.ServerInformationComputerModelInfo.modelPropertiesForBoardIDs_([boardID]):
            if boardID not in modelID:
                boardModelMap.append("%s - %s" % (boardID, modelID))
            else:
                boardModelMap.append("%s - Unknown" % boardID)

    return boardModelMap


def dumpX86(filePath):
    """Gather and dump board-id values to a file"""
    dumpListToFile(mapBoardsToModels(gatherX86()), filePath)


def gatherACPI_SMC():
    """Gather board-id values for older ACPI_SMC machines"""
    plistPath = "/System/Library/Extensions/IOPlatformPluginFamily.kext/" \
                "Contents/PlugIns/ACPI_SMC_PlatformPlugin.kext/" \
                "Contents/Resources/"
    return gatherPlistFiles(plistPath)


def dumpACPI_SMC(filePath):
    """Gather and dump board-id values to a file"""
    dumpListToFile(gatherACPI_SMC(), filePath)
