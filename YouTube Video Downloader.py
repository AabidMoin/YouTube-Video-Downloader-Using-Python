from pytube import YouTube

link = input("Enter Youtube video Link:  ")
youtube_1 = YouTube(link)

print("Title of the given video link is ",youtube_1.title)

print("Thumbnail url of the given video link is ",youtube_1.thumbnail_url)

videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("Enter : "))
videos[strm].download()

print("Successfully Download ")