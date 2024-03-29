#!/usr/bin/env python
"""macOS recon. Released under the MIT license"""

import macOSrecon.boardIDs as boardIDs
import macOSrecon.GPU_AMD as GPU_AMD
import macOSrecon.GPU_Intel as GPU_Intel
import macOSrecon.kernel as kernel
import macOSrecon.kexts as kexts
import macOSrecon.USB as usb
import macOSrecon.GraphicsPWM as gfxpwm

OUTPUT = "data/"


def main():
    """Main entry point"""
    boardIDs.dumpX86(OUTPUT + "boardIDs-x86.txt")
    boardIDs.dumpACPI_SMC(OUTPUT + "boardIDs-ACPI_SMC.txt")

    kernel.dumpVers(OUTPUT + "kernel.txt")
    kexts.dumpExts(OUTPUT + "kexts.txt")

    GPU_AMD.dumpAMDcards(OUTPUT + "GPU_AMD/")
    GPU_Intel.dumpIntelcards(OUTPUT + "GPU_Intel/")

    usb.dumpEHCI(OUTPUT + "models-usb-ehci.txt")
    usb.dumpXHCI(OUTPUT + "models-usb-xhci.txt")

    gfxpwm.dumpModels(OUTPUT + "models-gfxpwm.txt")


if __name__ == "__main__":
    main()
