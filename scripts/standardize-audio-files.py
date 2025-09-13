import os
import subprocess
from collections import defaultdict

def get_music_files():
    """Get a list of all music files in the current directory."""
    music_extensions = ['.mp3', '.flac', '.wav', '.ogg', '.aac']
    return [f for f in os.listdir('.') if os.path.splitext(f)[1].lower() in music_extensions]

def remove_duplicates(files):
    """Remove duplicate files, keeping .flac or .wav if available."""
    file_dict = defaultdict(list)
    for file in files:
        name, ext = os.path.splitext(file)
        file_dict[name].append(ext)

    to_remove = []
    for name, exts in file_dict.items():
        if len(exts) > 1:
            if '.flac' in exts:
                exts.remove('.flac')
            elif '.wav' in exts:
                exts.remove('.wav')
            to_remove.extend([name + ext for ext in exts])

    for file in to_remove:
        os.remove(file)
        print(f"Removed duplicate: {file}")

def convert_to_ogg(files):
    """Convert all compressed files to .ogg format."""
    for file in files:
        name, ext = os.path.splitext(file)
        if ext.lower() not in ['.flac', '.wav', '.ogg']:
            ogg_file = f"{name}.ogg"
            subprocess.run(['ffmpeg', '-i', file, '-c:a', 'libvorbis', ogg_file])
            os.remove(file)
            print(f"Converted {file} to {ogg_file}")

def main():
    music_files = get_music_files()
    remove_duplicates(music_files)
    music_files = get_music_files()  # Refresh list after removing duplicates
    convert_to_ogg(music_files)

if __name__ == "__main__":
    main()
