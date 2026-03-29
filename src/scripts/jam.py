import mutagen


def create_m3u(files, base_path):
    """Creates m3u file from list of paths"""

    output = ["#EXTM3U",""]

    for file in files:
        track = ["#EXTINF:"]
        track.append(str(_length_handeler(file)))
        track.append(file.name) 

        output.append(" ".join(track))
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
        