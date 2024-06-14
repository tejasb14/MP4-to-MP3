# MP4 to MP3 Converter

This Python script converts MP4 videos to MP3 audio files without using FFmpeg. Inputs are located in the `MP4` folder, and outputs will be saved in the `MP3` folder.

## Usage

1. **Requirements:**
   - Python 3.x

2. **Installation:**
   - Install the required Python packages:
     ```bash
     pip install moviepy
     ```

3. **Running the Script:**
   - Place your MP4 videos in the `MP4` directory.
   - Run the script:
     ```bash
     python mp4tomp3.py
     ```

4. **Output:**
   - The script will create an `MP3` directory if it doesn't exist.
   - The extracted audio files will be saved in the `MP3` directory with the same name as the original video file, but with the `.mp3` extension.

5. **Note:**
   - Make sure you have read/write permissions in the directories where the script is run and where the videos and audios are stored.

6. **Customization:**
   - You can modify the script to change the input/output directories or customize the conversion process based on your requirements.
