"""Functions relating to board-id gathering"""
import os


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


def dumpX86(filePath):
    """Gather and dump board-id values to a file"""
    dumpListToFile(gatherX86(), filePath)


def gatherACPI_SMC():
    """Gather board-id values for older ACPI_SMC machines"""
    plistPath = "/System/Library/Extensions/IOPlatformPluginFamily.kext/" \
                "Contents/PlugIns/ACPI_SMC_PlatformPlugin.kext/" \
                "Contents/Resources/"
    return gatherPlistFiles(plistPath)


def dumpACPI_SMC(filePath):
    """Gather and dump board-id values to a file"""
    dumpListToFile(gatherACPI_SMC(), filePath)
