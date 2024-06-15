from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError
from tqdm import tqdm

# FIXME: Add function that downloads a playlist of videos

def download_video(url):
    """Downloads YouTube video specified by the URL

    Args:
        url (str): specifies the YouTube URL to download
    """
    global pbar
    try:        
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download()
        print(f"Download completed for: '{yt.title}'")
            
    except Exception as e:
        print('Error. Could not download video.')
        # For Debug purposes
        # print(f'Error: {e}')
        
def main():
    while True:
        try:
            num_videos = int(input('Enter the number of videos to download: '))
        except ValueError as e:
            print('Error. Please enter an integer.')
            continue
        
        videos = []
        
        for video in range(num_videos):
            # Nested while loop for error handling
            while True:
                url = input(f'Enter YouTube URL {video + 1}: ')
                if not url:
                    print("Please enter a URL.")
                    continue
                else:
                    try:
                        yt = YouTube(url)
                        videos.append(url)
                        break
                    except (VideoUnavailable, RegexMatchError):
                        print("The video is unavailable. Please enter a valid URL.")
        
        # FIXME: Add progress bar for each video downloaded
        for video in tqdm(videos):
            download_video(video)
        break
   
if __name__ == "__main__":
    main()