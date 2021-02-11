"""Functions relating to Kernel extensions"""
import os
import platform

def dumpVers(filePath):
    """Gather a list of kexts and write it to a file"""
    dirPath = os.path.dirname(filePath)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    with open(filePath, "w") as fp:
        fp.write(platform.version())
