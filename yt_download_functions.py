from pytube import YouTube

def download_video_multiple(num_downloads):
    """Downloads user specified number of videos from YouTube prompitng user to enter each URL

    Args:
        num_downloads (int): specifies how many videos to download
    """
    try:        
        videos = []
        
        for i in range(num_downloads):
        
            url = input('Enter youtube URL: ')

            yt = YouTube(url)

            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

            videos.append(stream)
        
        for stream in videos:
        
            stream.download()

        print("Download completed")
        
    except Exception as e:
        print(f'Error: {e}')
        
def download_video(url):
    """Downloads YouTube video specified by the URL

    Args:
        url (string): specifies the YouTube URL to download
    """
    try:        
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download()
        print("Download completed")
            
    except Exception as e:
        print(f'Error: {e}')