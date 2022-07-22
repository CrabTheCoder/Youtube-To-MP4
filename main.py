from pytube import YouTube
import os
from pathlib import Path
print("""
\ \   / / __ \| |  | |__   __| |  | |  _ \|  ____| |__   __/ __ \  |  \/  |  __ \| || |  
  \ \_/ / |  | | |  | |  | |  | |  | | |_) | |__       | | | |  | | | \  / | |__) | || |_ 
   \   /| |  | | |  | |  | |  | |  | |  _ <|  __|      | | | |  | | | |\/| |  ___/|__   _|
    | | | |__| | |__| |  | |  | |__| | |_) | |____     | | | |__| | | |  | | |       | |  
    |_|  \____/ \____/   |_|   \____/|____/|______|    |_|  \____/  |_|  |_|_|       |_|  
                                                                                          
                                                                                          
""")
link = input("Enter link here: ")

url = YouTube(link)

print("downloading....")

video = url.streams.get_highest_resolution()

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

video.download(path_to_download_folder)
print("Video downloaded successfully!")