# app.py
import os 
import sys
from os.path import isfile, join
from os import listdir
import random 

LOOKUP_FILEPATH = "lookup.csv"

def main(argv):
    print("Location: %s" % argv[1])
    path = argv[1]

    lookup = dict()

    print("\nRenaming:")
    for filename in listdir(path):
        
        filename_components = filename.split('_')

        # replace name with 6 digit integer
        filename_components[1] = "_" + str(random.randint(1000000000,9999999999)) + "_"
        new_filename = "".join(filename_components)
        print("\t%s \t --->  %s" % (filename, new_filename))
        lookup[join(path, new_filename)] = join(path, filename)

        # rename file
        os.rename(join(path, filename), join(path, new_filename))


    # save CSV file for descriptions
    csv_text ="\n".join([k+','+ v for k,v in lookup.items()]) 


    print("\nSaving lookup to %s" % LOOKUP_FILEPATH)
    with open(LOOKUP_FILEPATH, "w") as file:
        file.write(csv_text)

    print("\n$ ls %s" % path)
    for filename in listdir(path):
        print("\t-  %s" % (filename))

    print('\nDone')


if __name__=="__main__":
    main(sys.argv)