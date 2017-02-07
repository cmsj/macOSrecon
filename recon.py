#!/usr/bin/env python
"""macOS recon. Released under the MIT license"""

import macOSrecon.boardIDs as boardIDs

OUTPUT = "data/"


def main():
    """Main entry point"""
    boardIDs.dumpX86(OUTPUT + "boardIDs-x86.txt")
    boardIDs.dumpACPI_SMC(OUTPUT + "boardIds-ACPI_SMC")


if __name__ == "__main__":
    main()
