from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
from urllib.parse import unquote
files = []
errors = []


def read_url(url):
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

            if (file_name[-1] == '/' and file_name[0] != '.'):
                read_url(url_new)

            if url_new.endswith(".mp4") or url_new.endswith(".mkv"):
                # print("GOT URL "+url_new)
                files.append(url_new)
                print("FOUND - "+url_new)

        except:
            file_name = i.get("href")
            url_new = url + file_name
            errors.append(url_new)

    return files, errors

