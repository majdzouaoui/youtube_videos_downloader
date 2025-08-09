from pytube import YouTube
from sys import argv
import urllib.parse as up
if len(argv) > 2:
    print("usage : python file_name url")
    exit() 
link = argv[1]
parsed = up.urlparse(link)
clean_link = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?v={up.parse_qs(parsed.query)}['v'][0]"
yt = YouTube(link)
print("title : ", yt.title)
print("view : ", yt.view)
yd = yt.streams.get_highest_resolution()
yd.download(r'C:\Users\majdz\Videos\Captures')