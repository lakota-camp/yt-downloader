# YouTube Video Downloader CLI Application

This command-line application downloads YouTube videos specified by the user. It uses the `pytube` library to fetch and download the videos.

## 🌟 Features
- Downloads YouTube videos in mp4 format
- Allows downloading multiple videos in one go
- Robust error handling for invalid URLs and unavailable videos

## 🚀 Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/lakota-camp/yt-downloader.git
cd yt-downloader
```

2. **Set up a virtual environment and activate it:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. **Install the dependencies:**
```bash
pip install -r requirements.txt
```
4. **Run the application:**
```bash
python3 app.py
```

## 🛠️ CLI Command Alias Setup To simplify running the YouTube video downloader, you can set up command aliases in your shell configuration file (.bashrc, .zshrc, etc.):

1. **Open your shell configuration file:**
```bash
nano ~/.zshrc # or ~/.bashrc depending on your shell
```
2. **Add the following alias definitions:**
```bash
alias yt-dl='source /path/to/dir/yt-downloader/.venv/bin/activate && python3 /path/to/dir/yt-downloader/app.py'
```
4. **Apply the changes:**
```bash
source ~/.bashrc  # or ~/.zshrc depending on your shell
```

## 📄 Usage Example

**Download videos:**

1. Run the command alias to start the application:
    ```bash
    yt-dl
    ```

2. Follow the prompts:

    - Enter the number of videos to download:
      ```plaintext
      Enter the number of videos to download: 3
      ```

    - Enter the URLs for each video one by one:
      ```plaintext
      Enter YouTube URL 1: https://www.youtube.com/watch?v=example_video_id1
      Enter YouTube URL 2: https://www.youtube.com/watch?v=example_video_id2
      Enter YouTube URL 3: https://www.youtube.com/watch?v=example_video_id3
      ```

3. The application will then download the specified videos.

## 🚧 Future Enhancements
* Add a function to download a playlist of videos
* Add a progress bar to show detailed download progress

## 📄 License

This project is licensed under the MIT License.

