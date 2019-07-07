"""Functions relating to Mac USB controllers"""
import os
import plistlib

ROOT = '/System/Library/Extensions/IOUSBHostFamily.kext/Contents/PlugIns/AppleUSB{bus}PCI.kext/Contents/Info.plist'


def gatherBus(bus):
    """Find all of the models supporting a particular USB bus type"""
    try:
        plist = plistlib.readPlist(ROOT.format(bus=bus))
    except IOError:
        return
    models = []
    for key in plist["IOKitPersonalities"]:
        if "model" in plist["IOKitPersonalities"][key]:
            models.append(plist["IOKitPersonalities"][key]["model"])
    return sorted(models)


def dumpBus(filePath, bus):
    """Gather info about all AMD kexts and write them to files"""
    models = gatherBus(bus)
    dirPath = os.path.dirname(filePath)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    with open(filePath, "w") as fp:
        fp.write('\n'.join(models))


def dumpEHCI(filePath):
    """Find all of the models supporting EHCI"""
    dumpBus(filePath, "EHCI")


def dumpXHCI(filePath):
    """Find all of the models supporting XHCI"""
    dumpBus(filePath, "XHCI")

