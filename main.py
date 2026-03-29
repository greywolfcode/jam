import argparse
import pathlib

import scripts.jam as jam

parser = argparse.ArgumentParser(
                prog="jam",
                description="Creates .m3u/.m3u8 files from directory",
                epilog="Currently only support .wav files")

#positional arguments
parser.add_argument("folder_path")

#optional arguments
parser.add_argument("-n", "--nonRecursive", action="store_true",
                    help="choose to not search all subdirectories")
parser.add_argument("-t", "--type", choices=[".m3u", ".m3u8"],

                    help="choose to output .m3u or .m3u8, .m3u is default")

def main(): 
    args = parser.parse_args()

    path = pathlib.Path(args.folder_path)

    








if __name__ == "__main__":
    main()