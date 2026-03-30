"""
    jam: .m3u/.m3u8 creation tool
    Copyright (C) 2026  greywolfcode

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA."""


import mutagen

def create_m3u(files, base_path):
    """Creates m3u file from list of paths"""

    output = ["#EXTM3U",""]

    for file in files:
        track = ["#EXTINF:"]
        track.append(str(_length_handeler(file)))
        track.append(file.name) 

        output.append(" ".join(track))
        if base_path == "":
            output.append(str(file.resolve()))
        else:
            output.append(str(file.relative_to(base_path)))
        output.append("")

    return "\n".join(output)

def _length_handeler(path):
    """input: file path
       output: length (sec)"""
    
    audio = mutagen.File(path)

    if "length" in audio.keys():
        return audio["length"]
    else:
        return audio.info.length
    #print(audio.pprint())
        