#!/usr/bin/env python3
import sys

print(sys.argv)

print(sys.argv[1])

for x in sys.argv:
    print(x)

print(sys.argv[1] + sys.argv[2])

print( int(sys.argv[1]) + int(sys.argv[2]) )
