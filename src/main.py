import argparse
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
parser.add_argument("-f", "--folder", type=str, default="",nargs="+",
                    help="only specified folder will be check for in subdirectories")

def main(): 
    args = parser.parse_args()

    path = pathlib.Path(args.folder_path)


    folder = args.folder
    if folder != "":
        #include any sub directories of provided folder
        folder += os.sep + "**" + os.sep 

    if args.nonRecursive:
        music_paths = path.glob(folder + "*.wav")
    else:
        music_paths = path.glob("**/" + folder + "*.wav")

    #mke relative paths
    
    file = jam.create_m3u(music_paths, path)

    name = args.playlist_name
    extension = args.type
    if args.playlist_name[-len(extension):] != extension:
        name += extension

    with open(os.path.join(args.folder_path, name), "w") as output:
        output.write(file)

if __name__ == "__main__":
    main()