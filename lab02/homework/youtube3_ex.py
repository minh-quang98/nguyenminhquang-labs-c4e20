from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch',
    'max_download': 1,
}
dl = YoutubeDL(options)
dl.download(['Cổ điển'])