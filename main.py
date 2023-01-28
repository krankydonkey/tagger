import os
import shutil
import re
import eyed3

folder = "C:/Users/Damian/Music/Zouk/PJ2"


def tags(destination, renamed_dest=""):
    if renamed_dest == "":
        renamed_dest = destination
    for root, _dirs, files in os.walk(destination):
        for filename in files:
            if filename.find("-") != -1:
                name = os.path.splitext(filename)
                splits = name[0].split("-", 1)
                artist = splits[0].strip()
                title = splits[1].strip()
                artists = re.split(',|feat.|ft.', artist, flags=re.I)
                artists = [x.strip() for x in artists]

                # Ask for confirmation
                confirm = input(title + " by " + str(artists) + "? (y/n): ")
                if confirm == 'y':
                    print("confirm = True")
                    path = os.path.join(root, filename)
                    f = eyed3.load(path)
                    print(path)
                    print(f)
                    #print(f.tag.title)
                    #"""
                    f.tag.title = title
                    f.tag.artits = "; ".join(artists)
                    f.tag.save()
                    #"""

tags(folder)
