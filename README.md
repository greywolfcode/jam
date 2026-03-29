# jam

jam ( **j**am **A**rranges **m**3u) is a tool for creating .m3u and .m3u8 playlists

## Installation

```
git clone https://github.com/greywolfcode/jam
```
Python 3.12 is recommended.

## Usage

> [!NOTE]
> Only .wav files are currently supported.

```
cd jam
main.py folder_path playlist_name -n -t -f folder_name
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
- -n, --nonRecursive
  - Does not check subdirectories for music files
- -t, --type
  - Specify .m3u or .m3u8 output
  - Options: .m3u or .msu8
- -f, --folder
  - Specify folder to searh for in all directories
    - Will ignore all folders in directories without specified foler name 
