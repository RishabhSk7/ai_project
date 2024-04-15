# This file checks which folders in dataset decrease acuracy in SVM
import itertools
import os
import psutil
import pprint
from skimage.io import imread
from SVM import generate_model
import json

import sys
import gc

gc.set_threshold(0)


dir = "OutputFiles/Moods and Moments"
Categories = os.listdir(dir)
combination = []


# trying to track memory usage
def sizeof_fmt(num, suffix="B"):
    """by Fred Cirera,  https://stackoverflow.com/a/1094933/1870254, modified"""
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, "Yi", suffix)


# using a json file, dont need to deal with string formatting in normal txt
# we will use this list to check if the combination has already been done before,
# so as to not waste time and resources if it has previously crashed
try:            #try statement since json gives error on empty file
    with open("results.json", "r", encoding="UTF-8") as file:
        predone = json.load(file)
except json.decoder.JSONDecodeError:
    predone = {}


# creating combinations of all possible for size 2 to n
for i in range(8, len(Categories)):
    combination.append(list(itertools.combinations(Categories, i)))

results = {}

for i in combination:
    print("\n\nCombination: ", combination.index(i)+2)
    input_arr, output_arr = [], []
    for j in i:
        if " ".join(j) in predone.keys():         #ensuring we are not processing already computed combinations
            print("\tSkipping", j, "since it has already been computed.")
            continue

        print("\n\tCurrently working on: ", end = "")
        print(*j, sep=",")
        print("\tMoemry usage(GB):", psutil.virtual_memory()[3]/1000000000)

        # trying to track memory usage
        for name, size in sorted(((name, sys.getsizeof(value)) for name, value in list(
                          locals().items())), key= lambda x: -x[1])[:10]:
            print("{:>30}: {:>8}".format(name, sizeof_fmt(size)))

        for k in j:
            print("\t\t\t loading: ", k)
            path = os.path.join(dir, k)
            LIMITER = 0
            for a in os.listdir(path):
                if LIMITER == 50:
                    break
                LIMITER+=1
                img = imread(os.path.join(path, a))
                input_arr.append(img.flatten())
                output_arr.append(j.index(k))
                del img     #memory management

            del path        #memory management
        print("\t\tgenerating model...")
        train, test = generate_model(input_arr, output_arr)
        print("\t\tTraining accuracy: ", train, "Testing accuracy: ", test)
        results[j] = (train, test)
        print("\t\tDone with ", end = "")
        print(*j, sep=",")

        predone[" ".join(j)] = (train, test)        #keys must be str, int, float, bool or None, not tuple

        with open("results.json", 'w', encoding="UTF-8") as file:
            json.dump(predone, file, indent=4)

        gc.collect()            #trying to conserve memory

pprint.pprint(results)
