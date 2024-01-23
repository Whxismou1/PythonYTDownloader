from pytube import YouTube
from pytube import Playlist
import os

def printMenu():
    print("Welcome to the YouTube Downloader")
    print("Please select an option:")
    print("1. Download a video")
    print("2. Download a playlist")
    print("3. Exit")
    option = int(input("Enter your option: "))
    return option



def menu(option):
    if option == 1:
        print("Enter the URL of the video you want to download: ")
        url = input()
        downloadSingleVideo(url)
    elif option == 2:
        print("Enter the URL of the playlist you want to download: ")
        url = input()
        downloadPlaylist(url)
    elif option == 3:
        print("Exiting app...")
    else:
        print("Invalid option")


def downloadSingleVideo(url):
    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        
        if not os.path.exists("./videosDownloaded"):
            os.makedirs("./videosDownloaded")
        
        file_path = os.path.join("./videosDownloaded", f"{video.title}.mp4")
        
        print(f"Downloading video: {video.title}...")
        stream.download(output_path="./videosDownloaded", filename=video.title)
        print(f"Video downloaded successfully. Saved to: {file_path}")
    except Exception as e:
        print(f"Error: {e}")


def downloadPlaylist(url):
    playlist = Playlist(url)
    print("Downloading playlist...")
    
    if not os.path.exists("./videosDownloaded"):
        os.makedirs("./videosDownloaded")
    file_path = os.path.join("./videosDownloaded", f"{playlist.title}")
    for video in playlist.videos:
        print(f"Downloading video: {video.title}...")
        video.streams.get_highest_resolution().download(output_path="./videosDownloaded", filename=video.title)
        print(f"Finished downloading video: {video.title}. Saved to:{file_path}")
        
    print("Playlist downloaded successfully")

if __name__ == "__main__":
    option = 0;
    
    while option != 3:
        option = printMenu()
        menu(option)
        
    
    
    
    