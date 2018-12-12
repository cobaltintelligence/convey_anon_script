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
    reverse_lookup = dict()

    print("\nRenaming:")
    for filename in listdir(path):
        
        filename_components = filename.split('_')

        # extract name component
        name = str(filename_components[1]).lower()
        
        # replace name with 6 digit integer
        new_name = "_" + str(random.randint(1000000000,9999999999)) + "_"

        # check if already hashed
        if name in reverse_lookup:
            new_name = reverse_lookup[name]
            
        filename_components[1] = new_name
        new_filename = "".join(filename_components)
        print("\t%s \t --->  %s" % (filename, new_filename))
        lookup[join(path, new_filename)] = join(path, filename)
        reverse_lookup[name] = new_name

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