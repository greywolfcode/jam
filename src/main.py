import argparse
import itertools
import os
import pathlib

import scripts.jam as jam

parser = argparse.ArgumentParser(
                prog="jam",
                description="Creates .m3u/.m3u8 files from directory",
                epilog="Currently only supports .wav files")

#positional arguments
parser.add_argument("folder_path")
parser.add_argument("playlist_name")

#optional arguments
parser.add_argument("-n", "--nonRecursive", action="store_true",
                    help="choose to not search all subdirectories")
parser.add_argument("-t", "--type", choices=[".m3u", ".m3u8"],
                    default=".m3u",
                    help="choose to output .m3u or .m3u8, .m3u is default")
parser.add_argument("-f", "--folders", nargs="+",
                    help="only specified folder will be check for in subdirectories")
parser.add_argument("-a", "--absolute", action="store_true",
                    help="use absolute paths")
parser.add_argument("-m", "--music_types", nargs="*",
                    help="select which file extensions to search")

default_file_types=[".mp3", ".aac", ".m4a", ".wav", ".flac", ".aiff", ".ogg"]

def main(): 
    args = parser.parse_args()

    path = pathlib.Path(args.folder_path)

    if args.music_types == None:
        music_exts = default_file_types
    else:
        music_exts = args.music_types
    music_exts.sort()

    paths = []
    folders = args.folders
    if folders == None:
        folders = [""] #ensure there is at least 1 folder
    folder.sort()
    for folder in folders:
        if folder != "":
            #include any sub directories of provided folder
            folder += os.sep + "**" + os.sep 
        for ext in music_exts:
            if args.nonRecursive:
                paths.extend(list(path.glob(folder + "*" + ext)))
            else:
                paths.extend(list(path.rglob(folder + "*" + ext)))
    
    if args.absolute:
        path = ""

    file = jam.create_m3u(paths, path)

    name = args.playlist_name
    extension = args.type
    if args.playlist_name[-len(extension):] != extension:
        name += extension

    with open(pathlib.Path(os.path.join(args.folder_path, name)), "w") as output:
        output.write(file)

if __name__ == "__main__":
    main()