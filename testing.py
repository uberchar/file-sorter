# Use dictionary for sorting filenames
#
#

import os
import shutil
import fileinput
import re
import time

def separate(s):
    """Parse input of a formated string"""
    a = s.find("]")+1
    t = s[1:].find("[")
    s = s.replace("_", " ")
    return(s[a+1:t])


def mkalldir(s):
    """Make all directories"""
    for dir in s:
        if not os.path.isdir(dst+dir):
            os.mkdir(dst + dir)
            print("Created: " + dst + dir)
            log.append("Created: " + dst + dir)
        else:
            print("Dir " + dst + dir + " already exists")
            log.append("Dir " + dst + dir + " already exists")
        time.sleep(0.5)

if __name__ == "__main__":
    log = []
    now = time.strftime("%c")
    print("Move started on: %s"  % now)
    log.append("Move started on: %s"  % now)
    src = "C:\\Users\\Jerry\\Downloads\\"
    dst = "X:\\Anime\\"
    b = []
    d = []
    toDel = []
    lines = iter(fileinput.input())
    next(lines)
    next(lines)
    # Parse a list of files from txt file
    # for making directories
    for line in lines:
        d.append(line.strip("\n"))
        if re.search("\[.*\].*[\s_]-[\s_][0-9]+", line.strip("\n")):
            a = separate(line).split(" -")[0]
            if a not in b and len(a) > 1:
                b.append(a)

    mkalldir(b)
    ff = ""

    for titles in b:
        title = titles.split(" ")
        for episodes in d:
            count = 0
            for name in title:
                if name in episodes:
                    count = count + 1
            if count == len(title):
                shutil.copy2(src+episodes, dst+titles)
                print("Moving " + episodes + " to " + dst+titles)
                ff = episodes
                log.append("Moving " + episodes + " to " + dst+titles)
                toDel.append(src + episodes)
        d.remove(ff)

    for dl in toDel:
        print("Deleting " + dl)
        os.remove(dl)
        log.append("Deleting " + dl)

    cnt = 0
    while (os.path.isfile(src + "log" + str(cnt) + ".txt")):
        cnt = cnt + 1
    f = open("log" + str(cnt) + ".txt", "w")
    f.write("\n".join(log))
    f.close()