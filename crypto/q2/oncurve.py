import sys

from ..utils.eeecc import on_curve

x = int(sys.argv[1])
y = int(sys.argv[2])

if on_curve((x, y)):
    print("True")
else:
    print("False")
