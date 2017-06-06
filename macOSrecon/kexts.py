"""Functions relating to Kernel extensions"""
import os

ROOT = "/System/Library/Extensions/"


def gatherExts():
    """Find all kexts"""
    kexts = []
    for root, dirs, files in os.walk(ROOT):
        if root[-5:] == ".kext":
            kexts.append(root.split('/')[-1][:-5])
    return sorted(kexts)


def dumpExts(filePath):
    """Gather a list of kexts and write it to a file"""
    dirPath = os.path.dirname(filePath)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    data = gatherExts()
    with open(filePath, "w") as fp:
        fp.write('\n'.join(data))
