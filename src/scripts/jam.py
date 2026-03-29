import wave

def create_m3u(files, base_path):
    """Creates m3u file from list of paths"""

    output = ["#EXTM3U",""]

    for file in files:
        track = ["#EXTINF:"]
        track.append(str(_wav_handeler(file)))
        track.append(file.name) 

        output.append(" ".join(track))
        output.append(str(file.relative_to(base_path)))
        output.append("")

    return "\n".join(output)

def _wav_handeler(path):
    """input: file path
       output: frame rate"""
    
    with wave.open(str(path), "r") as audio:
        frame_rate = audio.getframerate()
        total_frames = audio.getnframes()

        length = total_frames / float(frame_rate)
    return length
        
    
        
