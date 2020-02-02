from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
from urllib.parse import unquote
files = []
errors = []


def take_url_tv(file):
    le = len(file)
    z = 0
    x = 0
    for i in range(-1, -le - 1, -1):
        if file[i] == '/':
            z = i
            break

    for i in range(z - 1, -le - 1, -1):
        if file[i] == '/':
            x = i
            break

    sliceobj = slice(0, x, 1)
    return file[sliceobj]


def read_url_tv(url):
    url = url.replace(" ", "%20")
    req = Request(url)
    a = urlopen(req).read()
    soup = BeautifulSoup(a, 'html.parser')
    x = (soup.find_all('a'))
    for i in x:
        try:
            file_name = i.get("href")
            url_new = url + file_name
            url_new = unquote(url_new)

            if file_name[-1] == '/' and file_name[0] != '.':
                read_url_tv(url_new)

            if url_new.endswith(".mp4") or url_new.endswith(".mkv"):
                # print("GOT URL "+url_new)
                files.append(url_new)
                print("FOUND - "+url_new)

        except:
            file_name = i.get("href")
            url_new = url + file_name
            errors.append(url_new)

    series = [take_url_tv(s) for s in files]
    return series, errors


# print(read_url_tv("http://dhakaftp.com/Data/Disk9/English%20TV%20Series/"))