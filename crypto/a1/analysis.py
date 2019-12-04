import math


def entropy(frequencies):
    e = -1*sum([x*math.log(x, 2) for x in frequencies])
    return e


with open("frequency.txt", "r") as frequencyFile:
    chunks = frequencyFile.read().split("\n\n")


english_lines = [float(x)/100 for x in chunks[0].split("\n") if x]
german_lines = [float(x)/100 for x in chunks[1].split("\n") if x]

print("Entropy of English =", entropy(english_lines))
print("Entropy of German =", entropy(german_lines))
