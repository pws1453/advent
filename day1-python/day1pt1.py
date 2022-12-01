import numpy as np

elflist = []
vals = []
prev = 0
with open("elves") as f:
    calct = f.read().splitlines()
    print(calct)
    for cal in range(len(calct)):
        if calct[cal].isdigit():
            prev = prev + int(calct[cal])
            if cal == (len(calct)-1):
                print("HIT")
                elflist.append(prev)
        else:
            elflist.append(prev)
            prev = 0
for _ in range(3):
    bigelf = max(elflist)
    vals.append(bigelf)
    elflist.remove(bigelf)
print(sum(vals))
print(vals)