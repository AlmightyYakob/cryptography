import sys

from utils import on_curve

x = int(sys.argv[1])
y = int(sys.argv[2])

if on_curve((x, y)):
    print("True")
else:
    print("False")
