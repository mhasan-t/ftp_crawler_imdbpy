
def take_name(s):
    y = []
    le = len(s)
    z = 0
    x = 0
    for i in range(-1, -le - 1, -1):
        if s[i] == '/':
            z = i
            break

    for i in range(z - 1, -le - 1, -1):
        if s[i] == '/':
            x = i
            break

    for i in range(z - 1, x, -1):
        y.append(s[i])

    yo = "".join(y)

    yo = yo[::-1]
    return yo

# s = 'http://moviepoka.com/data/disk1/disk1/New Bengali Movies/Interstellar (2014)/Agantuk.aka.The Stranger.1991.720p.WEB-DL.x264 [DDN].mp4'
# print(take_name(s))
# movie_data = getMovieDatabyName(take_name(s))
# print(movie_data)