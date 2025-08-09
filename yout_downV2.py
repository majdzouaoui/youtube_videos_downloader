import yt_dlp

url = input("Enter YouTube URL: ")

with yt_dlp.YoutubeDL({}) as ydl:
    info = ydl.extract_info(url, download=False)
    print("Title:", info.get("title"))
    print("Views:", info.get("view_count"))
