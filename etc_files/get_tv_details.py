from urllib.parse import unquote
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def get_seasons(url):
    url = url.replace(" ", "%20")
    req = Request(url)
    a = urlopen(req).read()
    soup = BeautifulSoup(a, 'html.parser')
    links = (soup.find_all('a'))

    seasons = []
    for link in links:
        season = link.string
        season_link = link.get('href')
        season_link = url+'/'+season_link
        seasons.append([season, season_link])

    # print(seasons[1:])
    return seasons[1:]


def get_episodes(url):
    url = url.replace(" ", "%20")
    req = Request(url)
    a = urlopen(req).read()
    soup = BeautifulSoup(a, 'html.parser')
    links = (soup.find_all('a'))

    episodes = []
    for link in links:
        episode = link.get('href')
        episode_link = url+episode
        # episode_link = unquote(episode_link)

        if episode_link.endswith(".mp4") or episode_link.endswith(".mkv"):
            episodes.append([episode, episode_link])

    # print(episodes)
    return episodes

# get_seasons("http://dhakaftp.com/Data/Disk9/English%20TV%20Series/Game%20of%20Thrones/")
# get_episodes("http://dhakaftp.com/Data/Disk9/English%20TV%20Series/Game%20of%20Thrones/Season 08/")