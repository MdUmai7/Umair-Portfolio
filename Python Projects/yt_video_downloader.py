# first download pytube module to make our life easy
# and to makte youtube video downloading possible

from pytube import YouTube
import tkinter as tk
# tkinter is a built in module in python to create GUI applications
from tkinter import filedialog
# filedialog is a module in tkinter to open file dialog to select folder
# filedialog in simply a window to select files or folders

def download_video(url,save_path):
    # use try and except to handle errors
    # as there can be many errors like invalid url, network error, etc while downloading video
    try:
        yt = YouTube(url)
        # create YouTube object with the url
        
        streams=yt.streams.filter(progressive=True,file_extension='mp4')
        # filter the streams to get only mp4 videos with both audio and video (progressive=True)
        # progressive=True means the video has both audio and video
        # file_extension='mp4' means we want only mp4 videos

        # the general format of the above line is
        # streams = yt.streams.filter(<filter_conditions>)
        # filter_conditions can be multiple conditions like file_extension, progressive, resolution, etc
        # 

        highest_res_stream = streams.get_highest_resolution()
        # get the stream with highest resolution from the filtered streams
        highest_res_stream.download(output_path=save_path)
        # download the video to the specified save_path
        print("Download completed!")
    except Exception as e:
        print(e)

# url="https://youtube.com/shorts/NfQG4Dktdco?si=WApRv1Vn_JGnvUr7"
# save_path="C:/Users/Md_um/Desktop/Python_projects"

# download_video(url,save_path)
# up isnt user friendly

def open_file_dialog():
    folder=filedialog.askdirectory()
    # above line opens the file dialog to select folder and returns the selected folder path
    if folder:
        print(f"Selected folder: {folder} ")
    return folder


    
if __name__ == "__main__":
     # this block will run only if this script is run directly
    #  if we dont have this block then the below lines will run even if we import this script as a module in another script
    root = tk.Tk()
# this instantiates the tk module and create a tk window
root.withdraw()
# hide the root window
video_url = input("Enter the YouTube video URL: ")
save_path = open_file_dialog()
if  save_path:
    print("Downloading video...")
    download_video(video_url, save_path)
else:
    print("Invalid  save location")
    