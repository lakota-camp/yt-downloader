from pytube import YouTube
try:
    
    num_videos = int(input('Enter the number of videos to download: '))
    
    videos = []
    
    for i in range(num_videos):
    
        url = input('Enter youtube URL: ')

        yt = YouTube(url)

        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        videos.append(stream)
    
    for stream in videos:
    
        stream.download()

    print("Download completed")
    
except Exception as e:
    print(f'Error: {e}')