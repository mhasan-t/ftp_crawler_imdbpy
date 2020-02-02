
def take_name_tv(s):
    y = []
    le = len(s)
    z = 0
    x = 0
    c = 0
    for i in range(-1, -le - 1, -1):
        if s[i] == '/':
            z = i
            break

    for i in range(-1, z, -1):
        y.append(s[i])

    yo = "".join(y)

    yo = yo[::-1]
    return yo





# s = "http://dhakaftp.com/Data/Disk9/English TV Series/Game of Thrones"
# print(take_name_tv(s))
# movie_data = getMovieDatabyName(take_name(s))
# print(movie_data)

