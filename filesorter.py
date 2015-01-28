'''
Run using move.bat with directory your files are in.
Dumps a list of MKV as a list.
Uses a dictionary to store the key with the value being a list of episodes
in the folder.

Sort episode by their names. Makes a folder in destination directory,
copies the episode to the destination then deletes it in the original
directory.

Program can be extended to files other than MKVs and other names
with a specific format.
'''

import os
import shutil
import fileinput
import re
import time

def separate(src_name):
    """Return the name from the original filename"""
    start = src_name.find("]")+1 # find range of src_name within the brackets
    end = src_name[1:].find("[")
    src_name = src_name.replace("_", " ")
    # remove _ then return src_name in range of start and end
    #returns as src_name - NN
    return(src_name[start+1:end])

def sort_filenames(filename):
    """Return an iterator for key, value pairs"""
    name_list = {}

    for original_filename in filename:
        # Match filename with format of
        # [XXXXXXX] Name - NN [NNNp].mkv
        if re.search("\[.*\].*[\s_]-[\s_][0-9]+",
                     original_filename.strip("\n")):
            name = separate(original_filename).split(" -")[0]
            if (name not in name_list):
                name_list[name] = list()
            name_list[name].append(original_filename.strip("\n"))

    return name_list.iteritems()

def make_directory(path):
    """Make directory in destination"""
    if not os.path.isdir(path):
        os.mkdir(path)
        print("Created: " + path)
        log.append("Created: " + path)
    else:
        print("Dir " + path + " already exists")
        log.append("Dir " + path + " already exists")

if __name__ == "__main__":
    log = []
    now = time.strftime("%c")
    print("Move started on: %s"  % now)
    log.append("Move started on: %s"  % now)
    src = "C:\\Users\\Jerry\\Downloads\\"
    dst = "J:\\Anime\\"

    filename = iter(fileinput.input())
    next(filename)
    next(filename)
    
    name_pairs = sort_filenames(filename)

    for key, value in name_pairs:
        path = dst + key
        make_directory(path)
        for episode in value:
            print("Moving " + episode + " to " + path)
            log.append("Moving " + episode + " to " + path)
            shutil.copy2(src + episode, path)
            
            print("Deleting " + episode)
            log.append("Deleting " + episode)            
            os.remove(src + episode)

    count = 0
    while (os.path.isfile(src + "log" + str(count) + ".txt")):
        count = count + 1
    f = open("log" + str(count) + ".txt", "w")
    f.write("\n".join(log))
    f.close()