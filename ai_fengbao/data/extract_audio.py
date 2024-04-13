import os
import tqdm
from moviepy.editor import VideoFileClip


audio_save_dir_path = "audio"
video_save_dir_path = "videos"
os.makedirs(audio_save_dir_path, exist_ok=True)


for root, dirs, files in os.walk(video_save_dir_path):
    for file in tqdm.tqdm(files):
        if file.endswith(".mp4"):
            video_path = os.path.join(root, file)
            try:
                # Load the video file
                video = VideoFileClip(video_path)
                # Extract audio
                audio = video.audio
                # Define the path for the extracted audio
                audio_path = os.path.join(audio_save_dir_path, os.path.splitext(file)[0] + '.mp3')
                # Write audio file
                audio.write_audiofile(audio_path)
                # Close the video and audio to free resources
                audio.close()
                video.close()
            except Exception as e:
                print(f"Error processing {video_path}: {e}")