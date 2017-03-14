"""Functions relating to Intel GPUs"""
import os
import plistlib

ROOT = "/System/Library/Extensions/"


def gatherIntelexts():
    """Find all of the Intel related kexts"""
    return [f.split(".kext")[0]
            for f in os.listdir(ROOT)
            if (f[5:10] == "Intel" and "Graphics" in f)]


def inspectIntelplist(kext, filePath):
    """Extract the PCI IDs supported by a given Intel plist, if any"""
    try:
        plist = plistlib.readPlist(filePath)
    except IOError:
        return {}
    cards = {}
    for key in plist["IOKitPersonalities"]:
        try:
            cards[kext + "_" + key] = \
                plist["IOKitPersonalities"][key]["IOPCIPrimaryMatch"].split()
        except KeyError:
            pass
    return cards


def gatherIntelcards():
    """Find all the Intel kexts and inspect them for PCI info"""
    data = []
    for kext in gatherIntelexts():
        kextPath = os.path.join(ROOT, kext + ".kext", "Contents/Info.plist")
        cards = inspectIntelplist(kext, kextPath)
        for key in cards:
            card = '\n'.join(cards[key])
            data.append((key, card))
    return data


def dumpIntelcards(dirPath):
    """Gather info about all Intel kexts and write them to files"""
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    data = gatherIntelcards()
    for card in data:
        filePath = os.path.join(dirPath, card[0] + ".txt")
        with open(filePath, "w") as fp:
            fp.write(card[1])
