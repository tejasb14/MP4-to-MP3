# run  'pip install moviepy pydub' in the terminal
import os
from moviepy.editor import VideoFileClip

def convert_videos_to_mp3(video_folder, output_folder_mp3):
    if not os.path.exists(output_folder_mp3):
        os.makedirs(output_folder_mp3)

    for filename in os.listdir(video_folder):
        if filename.endswith('.mp4'):
            video_path = os.path.join(video_folder, filename)
            video_clip = VideoFileClip(video_path)
            
            # Extract audio as mp3
            audio_mp3_path = os.path.join(output_folder_mp3, filename.replace('.mp4', '.mp3'))
            video_clip.audio.write_audiofile(audio_mp3_path, codec='libmp3lame')
            
            print(f"Converted {filename} to {audio_mp3_path}")

# Files input and output directory
# Change the directory location according to your file location
video_folder = r'MP4'
output_folder_mp3 = r'MP3'

convert_videos_to_mp3(video_folder, output_folder_mp3)
