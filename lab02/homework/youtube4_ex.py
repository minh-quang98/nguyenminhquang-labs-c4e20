from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch',
    'max_download': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=jTmAkIFeaOw'])