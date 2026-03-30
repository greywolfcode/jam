# jam

jam ( **j**am **A**rranges **m**3u) is a tool for creating .m3u and .m3u8 playlists

## Supported audio formats

All audio formats supported by [mutagen](https://github.com/quodlibet/mutagen) can be parsed by this tool. However, this does not guarantee your audio player will be able to handle them.

## Installation

```
git clone https://github.com/greywolfcode/jam
cd jam
pip install -r requirements.txt
```
Python 3.12 is recommended.

## Usage

```
cd src
main.py folder_path playlist_name -n -t -a -f folder_name1 folder_name2 -m wav ogg flac
```

Default output is .m3u

### Minimal command

This is the simplest allowed command to generate .m3u

```
main.py folder_path playlist_name
```

### Arguments

- folder_path
  - Path to folder contianing music files
- playlist_name
  - Name of playlist to output. extension is not required
- -n, --non_recursive
  - Does not check subdirectories for music files
- -t, --type
  - Specify .m3u or .m3u8 output
  - Options: .m3u or .msu8
- -a -- absolute
  - Uses absolute paths for music paths
- -f, --folder
  - Specify music containing folder(s) to search for in all directories
- -m --music_type
  - Specify what music files to search for. The '.' must be included
  -Defaults: .mp3, .aac, .m4a, .wav, .flac, .aiff, .ogg

## Dependencies
- [mutagen](https://github.com/quodlibet/mutagen)

