#!/usr/bin/env python

import sys
if len(sys.argv) < 2:
    print("Please provide at least one string!")
    quit()

inString = sys.argv[1:]
for inStr in inString:
    # remove space
    inStr = inStr.strip()

    # output
    print( str(len(inStr)))
# end