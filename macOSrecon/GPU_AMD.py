"""Functions relating to AMD GPUs"""
import json
import os
import plistlib

ROOT = "/System/Library/Extensions/"


def gatherAMDexts():
    """Find all of the AMD related kexts"""
    return [f.split(".kext")[0] for f in os.listdir(ROOT) if f[0:3] == "AMD"]


def inspectAMDplist(kext, filePath):
    """Extract the PCI IDs supported by a given AMD plist, if any"""
    try:
        plist = plistlib.readPlist(filePath)
    except IOError:
        return {}
    cards = {}
    for key in plist["IOKitPersonalities"]:
        try:
            cards[kext + "_" + key] = \
                plist["IOKitPersonalities"][key]["IOPCIMatch"].split()
        except KeyError:
            pass
    return cards


def gatherAMDcards():
    """Find all the AMD kexts and inspect them for PCI info"""
    data = []
    for kext in gatherAMDexts():
        kextPath = os.path.join(ROOT, kext + ".kext", "Contents/Info.plist")
        cards = inspectAMDplist(kext, kextPath)
        for key in cards:
            card = '\n'.join(cards[key])
            data.append((key, card))
    return data


def dumpAMDcards(dirPath):
    """Gather info about all AMD kexts and write them to files"""
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    data = gatherAMDcards()
    for card in data:
        filePath = os.path.join(dirPath, card[0] + ".txt")
        with open(filePath, "w") as fp:
            fp.write(card[1])
